DOCKER = $(if $(DOCKER_BINARY),$(DOCKER_BINARY),/usr/bin/docker)
BUILD_ARG = $(if $(filter  $(NOCACHE), 1),--no-cache)
BUILD_ARG_BASE = $(if $(filter $(NOCACHEBASE), 1),--no-cache)
USERID?=$(shell id -u)
GROUPID?=$(shell id -g)

.PHONY: all profile_image

profile_image:
	$(DOCKER) build $(BUILD_ARG) -t new-year-chaos:latest .
run_profile_test:
	$(DOCKER) run \
    	--rm \
    	--memory="1g" \
    	new-year-chaos:latest
