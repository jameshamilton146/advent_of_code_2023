#GLOBALS
GLOBAL_PYTHON = $(DEFAULT_PYTHON)
PYTHON_VENV_NAME = .venv 
PYTHON_INTERPRETER = $(PYTHON_VENV_NAME)/bin/python 

#COMMANDS
.PHONY: create_venv
create_venv:
	virtualenv --python=$(GLOBAL_PYTHON) $(PYTHON_VENV_NAME)
	$(PYTHON_INTERPRETER) -m pip install -U pip setuptools wheel

.PHONY: delete_venv
delete_venv:
	rm $(PYTHON_VENV_NAME)/ -r

.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

.PHONY: reqs 
reqs:
	$(PYTHON_INTERPRETER) -m pip freeze requirements.txt

.PHONY: install_reqs
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt
