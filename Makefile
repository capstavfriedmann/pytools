.PHONY: setup

COMMAND=$(firstword $(MAKECMDGOALS))

ARGS=$(wordlist 2, $(words $(MAKECMDGOALS)), $(MAKECMDGOALS))

%:
	@:

setup:
	git checkout -b temp 
	@$(foreach arg,$(ARGS),echo Merging tool $(arg); git merge origin/$(arg);)
	rm -rf .git
	pip install python-dotenv
	python ./pytools/load_env.py