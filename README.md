
# Software Engineering Project

This project was developed as part of a university Software Engineering course. It is a machine learning application that allows users to explore datasets, visualize data, select features, and compare different classification algorithms through an interactive web interface.

## Features

* Load and explore datasets.
* Visualize data using graphs.
* Select features for machine learning.
* Use classification algorithms such as K-Nearest Neighbors (KNN) and Support Vector Machine (SVM).
* Run the application through a web interface.

## Technologies Used

* Python
* Streamlit
* Scikit-learn
* NumPy
* Matplotlib
* Seaborn
* Docker

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/inf2021090/sw-project.git](https://github.com/inf2021090/sw-project.git)
   cd sw-project

```

2. Install the required dependencies:
```bash
pip install -r requirements.txt

```


3. Run the application:
```bash
streamlit run src/app.py

```


Then open the URL provided in the terminal in your browser.

## Docker

You can also run the application using Docker:

```bash
docker build -t ml-app .
docker run --rm -p 8501:8501 ml-app

```

Then visit `http://localhost:8501`.

## Project Structure

* `src/` – Application source code.
* `docs/` – Project documentation.
* `requirements.txt` – Required Python packages.
* `Dockerfile` – Docker configuration.
* `Makefile` – Commands for running the application and managing project files.


## License

This project was created for educational purposes.


