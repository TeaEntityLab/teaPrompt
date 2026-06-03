#!/usr/bin/env python3
"""
Prompt/Skill Index Generator for TeaPrompt

Generates a JSON index with:
- File metadata (path, type, category)
- Frontmatter data (name, description, license)
- Dependencies (ref_file, ref_snippet references)
- Categories and hierarchy
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime


class IndexGenerator:
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root).resolve()
        self.index = {
            "version": "1.0",
            "generated_at": datetime.now().isoformat(),
            "repo_root": ".",  # Use relative path to avoid exposing absolute paths
            "categories": {},
            "prompts": [],
            "skills": [],
            "total_files": 0
        }
    
    def generate(self) -> Dict:
        """Generate the complete index."""
        # Process prompt library
        prompt_library = self.repo_root / "reflective-prompt-library"
        if prompt_library.exists():
            self.process_directory(prompt_library, "prompt-library")
        
        # Process skills
        skills_dir = prompt_library / "skills"
        if skills_dir.exists():
            self.process_skills_directory(skills_dir)
        
        # Calculate totals
        self.index["total_files"] = len(self.index["prompts"]) + len(self.index["skills"])
        
        return self.index
    
    def process_directory(self, directory: Path, category: str):
        """Process a directory of prompts."""
        if not directory.exists():
            return
        
        # Add category if not exists
        if category not in self.index["categories"]:
            self.index["categories"][category] = {
                "path": str(directory.relative_to(self.repo_root)),
                "subcategories": {}
            }
        
        # Process subdirectories
        for item in directory.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                subcategory = item.name
                self.index["categories"][category]["subcategories"][subcategory] = {
                    "path": str(item.relative_to(self.repo_root)),
                    "files": []
                }
                
                # Process markdown files in subdirectory
                for md_file in item.glob("*.md"):
                    if md_file.name != "SKILL.md":  # Skills are processed separately
                        prompt_data = self.process_prompt_file(md_file, category, subcategory)
                        if prompt_data:
                            self.index["prompts"].append(prompt_data)
                            self.index["categories"][category]["subcategories"][subcategory]["files"].append(md_file.name)
    
    def process_skills_directory(self, skills_dir: Path):
        """Process the skills directory separately."""
        skills_category = "skills"
        if skills_category not in self.index["categories"]:
            self.index["categories"][skills_category] = {
                "path": str(skills_dir.relative_to(self.repo_root)),
                "subcategories": {}
            }
        
        # Process skill subdirectories
        for item in skills_dir.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                skill_name = item.name
                skill_file = item / "SKILL.md"
                
                if skill_file.exists():
                    skill_data = self.process_skill_file(skill_file, skills_category, skill_name)
                    if skill_data:
                        self.index["skills"].append(skill_data)
                        
                        if skill_name not in self.index["categories"][skills_category]["subcategories"]:
                            self.index["categories"][skills_category]["subcategories"][skill_name] = {
                                "path": str(item.relative_to(self.repo_root)),
                                "files": []
                            }
                        self.index["categories"][skills_category]["subcategories"][skill_name]["files"].append("SKILL.md")
    
    def process_prompt_file(self, file_path: Path, category: str, subcategory: str) -> Dict:
        """Process a single prompt file."""
        try:
            content = file_path.read_text(encoding='utf-8')
            relative_path = file_path.relative_to(self.repo_root)
            
            # Extract frontmatter if present
            frontmatter = self.extract_frontmatter(content)
            
            # Extract dependencies
            dependencies = self.extract_dependencies(content)
            
            # Extract headings as structure
            structure = self.extract_structure(content)
            
            return {
                "path": str(relative_path),
                "type": "prompt",
                "category": category,
                "subcategory": subcategory,
                "name": frontmatter.get("title", file_path.stem),
                "description": frontmatter.get("description", ""),
                "frontmatter": frontmatter,
                "dependencies": dependencies,
                "structure": structure,
                "line_count": len(content.splitlines()),
                "char_count": len(content)
            }
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return None
    
    def process_skill_file(self, file_path: Path, category: str, skill_name: str) -> Dict:
        """Process a single skill file."""
        try:
            content = file_path.read_text(encoding='utf-8')
            relative_path = file_path.relative_to(self.repo_root)
            
            # Extract frontmatter
            frontmatter = self.extract_frontmatter(content)
            
            # Extract dependencies
            dependencies = self.extract_dependencies(content)
            
            # Extract structure
            structure = self.extract_structure(content)
            
            # Extract prompt sources if present
            prompt_sources = self.extract_prompt_sources(content)
            
            return {
                "path": str(relative_path),
                "type": "skill",
                "category": category,
                "subcategory": skill_name,
                "name": frontmatter.get("name", skill_name),
                "description": frontmatter.get("description", ""),
                "license": frontmatter.get("license", ""),
                "frontmatter": frontmatter,
                "dependencies": dependencies,
                "prompt_sources": prompt_sources,
                "structure": structure,
                "line_count": len(content.splitlines()),
                "char_count": len(content)
            }
        except Exception as e:
            print(f"Error processing skill {file_path}: {e}")
            return None
    
    def extract_frontmatter(self, content: str) -> Dict:
        """Extract YAML frontmatter from content."""
        if not content.startswith('---'):
            return {}
        
        try:
            frontmatter_end = content.find('---', 3)
            if frontmatter_end == -1:
                return {}
            
            frontmatter_text = content[3:frontmatter_end].strip()
            return self.parse_simple_yaml(frontmatter_text)
        except Exception:
            return {}
    
    def parse_simple_yaml(self, text: str) -> dict:
        """Simple YAML parser for basic key-value pairs."""
        result = {}
        for line in text.split('\n'):
            line = line.strip()
            if ':' in line and not line.startswith('#'):
                key, value = line.split(':', 1)
                result[key.strip()] = value.strip()
        return result
    
    def extract_dependencies(self, content: str) -> Dict:
        """Extract file dependencies from content."""
        dependencies = {
            "ref_file": [],
            "ref_snippet": [],
            "markdown_links": []
        }
        
        # Extract ref_file references
        ref_file_pattern = r'<ref_file file="([^"]+)"\s*/>'
        dependencies["ref_file"] = re.findall(ref_file_pattern, content)
        
        # Extract ref_snippet references
        ref_snippet_pattern = r'<ref_snippet file="([^"]+)" lines="(\d+-\d+)"\s*/>'
        dependencies["ref_snippet"] = re.findall(ref_snippet_pattern, content)
        
        # Extract markdown links (local only)
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        for text, url in re.findall(link_pattern, content):
            if not url.startswith(('http://', 'https://', '#', 'mailto:', 'ftp://')):
                dependencies["markdown_links"].append(url)
        
        return dependencies
    
    def extract_structure(self, content: str) -> List[Dict]:
        """Extract heading structure from content."""
        structure = []
        heading_pattern = r'^(#{1,6})\s+(.+)$'
        
        for line in content.split('\n'):
            match = re.match(heading_pattern, line)
            if match:
                level = len(match.group(1))
                text = match.group(2).strip()
                structure.append({
                    "level": level,
                    "text": text
                })
        
        return structure
    
    def extract_prompt_sources(self, content: str) -> List[str]:
        """Extract prompt sources from skill file."""
        sources = []
        pattern = r'- `([^`]+\.md)`'
        matches = re.findall(pattern, content)
        sources.extend(matches)
        return sources


def main():
    repo_root = Path(__file__).parent.parent.parent
    
    print(f"Generating index for: {repo_root}")
    print("=" * 60)
    
    generator = IndexGenerator(str(repo_root))
    index = generator.generate()
    
    # Save index to file
    output_file = repo_root / "reflective-prompt-library" / "index.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    
    print(f"\n📊 Index Generation Results")
    print(f"Total files indexed: {index['total_files']}")
    print(f"Prompts: {len(index['prompts'])}")
    print(f"Skills: {len(index['skills'])}")
    print(f"Categories: {len(index['categories'])}")
    
    # Print category breakdown
    for category, data in index['categories'].items():
        subcategory_count = len(data['subcategories'])
        print(f"  {category}: {subcategory_count} subcategories")
    
    print(f"\n✅ Index saved to: {output_file}")
    
    # Print sample entry
    if index['skills']:
        print(f"\n📝 Sample skill entry:")
        print(json.dumps(index['skills'][0], indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()