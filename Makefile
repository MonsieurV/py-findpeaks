####### Constants ########

SHELL := /bin/bash
ROOT_DIR = $(realpath $(dir $(lastword $(MAKEFILE_LIST))))
PYTHONHOME ?= ${ROOT_DIR}/venv/
ACTIVATE_VENV = source ${PYTHONHOME}bin/activate
PY_RUNNER = ${ACTIVATE_VENV} &&

####### Installation for the tests ########
up: venv dependencies

install:
	${MAKE} up

venv:
	echo "Creating virtualenv..."
	(test -d ${PYTHONHOME} || virtualenv ${PYTHONHOME})
	${MAKE} activate

activate:
	${ACTIVATE_VENV}

dependencies:
	${PYTHONHOME}bin/pip install -r test-requirements.txt

####### Run the tests ########
test:
	${PY_RUNNER} nosetests tests -v