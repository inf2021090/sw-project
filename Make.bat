# Default target
.PHONY: all
all: activate

# create virtual environment
.PHONY: venv
venv:
    python -m venv venv

#  activate virtual environment
.PHONY: activate
activate:
    @echo "Activating virtual environment. Use 'deactivate' to exit."
    @cmd /k "venv\Scripts\activate"

# Install dependencies
.PHONY: install
install: venv
    venv\Scripts\pip install -r requirements.txt

# Run streamlit app
.PHONY: run
run: activate
    venv\Scripts\streamlit run app.py

# clean up venv
.PHONY: clean
clean:
    @echo "Cleaning up virtual environment and other generated files."
    @IF EXIST venv rmdir /s /q venv
