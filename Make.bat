# Makefile for setting up Python virtual environment and running Streamlit app

# Commands
PYTHON = python
PIP = $(VENV)\Scripts\pip
STREAMLIT = $(VENV)\Scripts\streamlit
ACTIVATE = $(VENV)\Scripts\activate

# Virtual environment name
VENV = venv

# Python requirements file
REQUIREMENTS = requirements.txt

# Streamlit app file
APP_FILE = app.py

# Default target
.PHONY: all
all: activate

# Create virtual environment
.PHONY: venv
venv:
    $(PYTHON) -m venv $(VENV)

# Command to activate virtual environment
.PHONY: activate
activate:
    @echo "Activating virtual environment. Use 'deactivate' to exit."
    @cmd /k "$(ACTIVATE)"

# Install dependencies
.PHONY: install
install: venv
    $(PIP) install -r $(REQUIREMENTS)

# Run Streamlit app
.PHONY: run
run: activate
    $(STREAMLIT) run $(APP_FILE)

# Clean up virtual environment
.PHONY: clean
clean:
    @echo "Cleaning up virtual environment and other generated files."
    @IF EXIST $(VENV) rmdir /s /q $(VENV)

