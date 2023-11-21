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
	python ./pytools/cli/load_env.py

clear_cache:
	python ./pytools/cli/clear_cache.py

clear_logs:
	python ./pytools/cli/clear_logs.py