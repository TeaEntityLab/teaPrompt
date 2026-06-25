.PHONY: test validate all

PLANS = reflective-prompt-library/plans

test:
	python3 -m pytest $(PLANS)/tests/ -v

validate:
	python3 $(PLANS)/validate_links.py
	python3 $(PLANS)/lint_skills.py
	python3 $(PLANS)/validate_governance.py
	python3 $(PLANS)/validate_project_knowledge.py
	python3 $(PLANS)/route_paraphrase_eval.py
	python3 $(PLANS)/route_paraphrase_eval.py $(PLANS)/route-002-holdout-eval.yaml

all: test validate
