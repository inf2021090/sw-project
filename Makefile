# Name of the Conda environment
ENV_NAME = myenv

# Conda environment file
ENV_FILE = environment.yml

# Requirements file
REQ_FILE = requirements.txt

.PHONY: all create_env install delete_env update_reqs run

# Create Conda environment
create_env:
	conda env create -f $(ENV_FILE) --name $(ENV_NAME)

# Install dependencies
install:
	conda activate $(ENV_NAME) && pip install -r $(REQ_FILE)

# Delete Conda environment
delete_env:
	conda remove --name $(ENV_NAME) --all -y

# Update requirements.txt
update_reqs:
	conda activate $(ENV_NAME) && pip freeze > $(REQ_FILE)

# Run the Streamlit app
run:
	conda activate $(ENV_NAME) && streamlit run app.py


