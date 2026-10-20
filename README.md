ML Application — Machine Learning & Data Analysis

A web-based machine learning application developed as part of a university Software Engineering project. The application provides an interactive environment for exploring datasets, visualizing data, selecting relevant features, and comparing classification algorithms.

Built with Python, Streamlit, and scikit-learn, the project aims to make common machine learning workflows more accessible through a graphical user interface.

Table of Contents
Overview
Features
Technology Stack
Project Structure
Requirements
Getting Started
1. Clone the Repository
2. Create a Virtual Environment
3. Install Dependencies
4. Run the Application
Running with Docker
Using the Application
Machine Learning Algorithms
Development and Maintenance
Troubleshooting
Future Improvements
Contributing
License
Acknowledgements
Overview

Machine learning involves several steps, including understanding a dataset, preparing data, identifying useful features, training models, and evaluating their performance. Performing these tasks often requires knowledge of multiple libraries and tools.

This project brings key parts of that workflow into a single interactive application. Users can explore data, visualize its characteristics, perform feature selection, and compare classification methods in a graphical environment.

The project was developed for educational purposes as part of a Software Engineering course, with an emphasis on combining machine learning functionality with an accessible web interface.

Project Goals
Provide an interactive interface for working with datasets.
Support data exploration and visualization.
Enable feature selection as part of the machine learning workflow.
Facilitate experimentation with classification algorithms.
Provide a reproducible way to run the application using Docker.
Demonstrate the integration of Python-based data science tools in a software project.
Features
Dataset Loading

Load datasets into the application for exploration and machine learning experiments.

Data Visualization

Explore datasets visually using plotting and visualization libraries. Visual representations can help reveal patterns, distributions, relationships, and potential data quality issues.

Feature Selection

Investigate feature selection to identify relevant input variables for classification tasks. Selecting appropriate features can help simplify models and improve interpretability.

Classification Algorithms

Experiment with classification methods, including:

K-Nearest Neighbors (KNN): Classifies observations based on the labels of nearby observations.
Support Vector Machine (SVM): Learns a decision boundary that separates classes, with support for different configurations depending on the implementation.
Interactive Web Interface

The application uses Streamlit to provide a browser-based interface for interacting with the machine learning workflow.

Containerized Execution

A Dockerfile is provided to package the application and its dependencies, making it easier to run in a consistent environment.

Technology Stack

The repository's dependency list includes the following technologies:

Technology	Purpose
Python	Main programming language
Streamlit	Interactive web application
scikit-learn	Machine learning algorithms and tools
NumPy	Numerical computation
Matplotlib	Data visualization
Seaborn	Statistical visualization
OpenCV	Image processing utilities
Pillow	Image handling
UMAP / umap-learn	Dimensionality reduction
streamlit-option-menu	Navigation components for Streamlit
Docker	Application containerization
Make	Development and task automation
LaTeX / BibTeX	Project report and bibliography

The dependencies are listed in requirements.txt.

Project Structure

The repository is organized around the application source code, project documentation, and development configuration.

sw-project/
├── docs/               # Project documentation and report files
├── src/                # Application source code
│   └── app.py          # Streamlit application entry point
├── Dockerfile          # Docker image configuration
├── Makefile            # Development and report automation
├── requirements.txt    # Python dependencies
├── .gitignore          # Files excluded from version control
└── README.md           # Project documentation


Additional files may exist within the src/ and docs/ directories.

Requirements

Before running the application locally, ensure that you have:

Python installed.
pip, Python's package installer.
Git for cloning the repository.
A modern web browser.

To use the containerized setup, you will also need Docker installed and running.

Check your Python installation with:

python --version


Check pip with:

python -m pip --version


Depending on your operating system, the Python executable may be named python3 instead of python.

Getting Started
1. Clone the Repository

Open a terminal and run:

git clone https://github.com/inf2021090/sw-project.git
cd sw-project

2. Create a Virtual Environment

A virtual environment keeps the project's dependencies separate from other Python projects.

Windows:

python -m venv venv
venv\Scripts\activate


Linux / macOS:

python3 -m venv venv
source venv/bin/activate


After activation, commands that install packages will use the environment's Python installation.

3. Install Dependencies

Install the dependencies declared by the project:

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

4. Run the Application

Start the Streamlit application from the repository root:

streamlit run src/app.py


Streamlit will provide a local URL in the terminal. Open the displayed address in your browser. The default address is usually:

http://localhost:8501

To stop the application, press Ctrl+C in the terminal.

Running with Docker

Docker provides an alternative to installing the application's Python dependencies directly on your machine.

1. Build the Image

From the root directory of the repository, run:

docker build -t ml-app .


This builds a Docker image named ml-app using the repository's Dockerfile.

2. Start the Container

Run:

docker run --rm -p 8501:8501 ml-app


The port mapping makes the application's port 8501 available on your local machine.

3. Open the Application

Navigate to:

http://localhost:8501

4. Stop the Container

Press Ctrl+C in the terminal. The --rm option automatically removes the stopped container.

If the application cannot be reached, verify that the container started successfully and that the Dockerfile configures Streamlit to listen on port 8501 and on an address accessible from outside the container.

Using the Application

The following workflow describes the general machine learning process supported by the project's documented features. The exact interface and available options depend on the current implementation.

Start the application. Launch it locally or through Docker and open the browser interface.
Load a dataset. Select or upload a dataset using the options available in the application.
Explore the data. Inspect the dataset and use the available visualizations to understand its structure and characteristics.
Select features. Apply the available feature selection functionality to investigate which variables are useful for the classification task.
Choose a classifier. Experiment with a supported classification algorithm, such as KNN or SVM.
Evaluate the results. Review the results and comparisons provided by the application.
Compare experiments. Investigate how different feature selections or classifier configurations affect the results.

For reliable comparisons, use the same dataset and evaluation procedure when comparing different models.

Machine Learning Algorithms
K-Nearest Neighbors (KNN)

KNN is a supervised learning algorithm that predicts a sample's class based on the classes of its nearest neighbors.

Its behavior depends on factors such as:

The number of neighbors, commonly represented by k.
The distance metric.
Feature scaling.
The distribution of the training data.

KNN is useful as a straightforward baseline for classification experiments.

Support Vector Machine (SVM)

SVM is a supervised learning algorithm that identifies a decision boundary between classes. Depending on the configuration, it can model linear or nonlinear decision boundaries.

Its performance can depend on:

The kernel function.
Regularization parameters.
Feature scaling.
The characteristics and size of the dataset.

SVM provides a useful comparison with KNN because the two algorithms approach classification differently.

Comparing Models

When comparing classifiers, consider appropriate evaluation metrics for the task and dataset. Common classification metrics include:

Accuracy: The proportion of predictions that are correct.
Precision: The proportion of positive predictions that are correct.
Recall: The proportion of actual positive cases that are identified.
F1-score: The harmonic mean of precision and recall.
Confusion matrix: A breakdown of correct and incorrect predictions by class.

These are general evaluation recommendations; the availability of each metric in the application's interface depends on its implementation.

Development and Maintenance
Running the Application

The Makefile defines a shortcut for launching the application:

make run


This target runs:

streamlit run src/app.py


Make sure the virtual environment is activated and the project dependencies have been installed before using this shortcut.

Generating the Project Report

The Makefile also defines a target for building the LaTeX project report:

make


The report target expects the following files:

inf2021090_project_report.tex
references.bib

The report build requires LaTeX and BibTeX to be installed. Check that the required files are present in the directory expected by the Makefile before running the command.

Cleaning Generated Files

To remove common LaTeX auxiliary files, run:

make clean


Review the Makefile before using other cleanup targets, especially those that delete files or directories.

Troubleshooting
The streamlit Command Is Not Found

Make sure the virtual environment is activated and the dependencies have been installed.

Alternatively, run Streamlit through Python:

python -m streamlit run src/app.py

Dependencies Fail to Install

Upgrade pip and retry:

python -m pip install --upgrade pip
python -m pip install -r requirements.txt


If a package fails to install, check your Python version, operating system compatibility, and the package's installation requirements.

Port 8501 Is Already in Use

Run Streamlit on another port:

streamlit run src/app.py --server.port 8502


Then open http://localhost:8502.

For Docker, change the host-side port mapping if necessary. For example:

docker run --rm -p 8502:8501 ml-app


Open http://localhost:8502 in your browser.

Docker Container Starts but the Application Is Unavailable

Check the container logs and verify that Streamlit is listening on 0.0.0.0 inside the container, rather than only on localhost.

Dataset or Classification Errors

Check that the selected dataset is supported by the application and contains the columns and target labels expected by the workflow. Also verify that missing values, categorical variables, and feature scaling are handled appropriately for the selected classifier.

Future Improvements

Potential directions for extending the project include:

Supporting additional classification algorithms.
Expanding data visualization and exploratory analysis.
Providing more feature selection methods.
Offering configurable train-test splits and cross-validation.
Displaying additional evaluation metrics and confusion matrices.
Improving error messages and input validation.
Adding automated unit and integration tests.
Providing example datasets and reproducible experiments.
Adding screenshots and a demonstration of the user interface.
Improving documentation for supported datasets and application workflows.

These are suggestions for future development, not a statement that these features are currently implemented.

Contributing

Contributions, suggestions, and bug reports are welcome.

To contribute:

Fork the repository.
Create a branch for your changes:
git checkout -b feature/your-feature-name

Implement and test your changes.
Commit your work:
git add .
git commit -m "Describe your changes"

Push your branch:
git push origin feature/your-feature-name

Open a pull request describing the changes and their purpose.

Please keep changes focused, follow the existing project structure, and update the documentation whenever application behavior or setup instructions change.

License

No license information has been confirmed for this repository. Unless a license is added, users should not assume that the code is available for unrestricted reuse or redistribution.

If you maintain this project, consider adding an appropriate LICENSE file.

Acknowledgements

This project uses the Python ecosystem for machine learning, data processing, visualization, and web application development.

Special thanks to the developers and maintainers of Streamlit, scikit-learn, NumPy, Matplotlib, Seaborn, OpenCV, Pillow, and UMAP, as well as the broader open-source community.

Repository: https://github.com/inf2021090/sw-project

Application entry point: src/app.py

Dependency file: requirements.txt

Container configuration: Dockerfile
