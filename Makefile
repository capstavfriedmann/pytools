HARD ?= 0

.PHONY: setup

COMMAND=$(firstword $(MAKECMDGOALS))

ARGS=$(wordlist 2, $(words $(MAKECMDGOALS)), $(MAKECMDGOALS))

%:
	@:

setup:
	git checkout -b temp
	@$(foreach arg,$(ARGS),echo Running command for $(arg); git merge $(arg);)
	Remove-Item -Path ".\.git" -Recurse -Force