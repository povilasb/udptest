src_dir := udptest

python ?= python3.6
virtualenv_dir := pyenv
pip := $(virtualenv_dir)/bin/pip
linter := $(virtualenv_dir)/bin/python -m flake8
py_requirements ?= requirements/prod.txt requirements/dev.txt


.PHONY: lint
lint: $(virtualenv_dir)
	$(linter) $(src_dir)

$(virtualenv_dir): $(py_requirements)
	$(python) -m venv $@
	for r in $^ ; do \
		$(pip) install -r $$r ; \
	done
