# ML Application - SW

This is a machine learning application developed as part of a school project. The app allows users to load datasets, visualize data, perform feature selection, and compare different classification algorithms (such as K-Nearest Neighbors and Support Vector Machine). 

## Running the Application

To run the application, you can use the provided **Docker** setup. This ensures all dependencies are handled smoothly. Follow the steps below:

### Steps:
1. **Clone the repository**:
   ```bash
   https://github.com/inf2021090/sw-project.git
   cd sw-project
The app will be available at [http://localhost:8501](http://localhost:8501) on your browser.

2.  ** Build nad run using docker
   ```bash
      docker build -t ml-app .
   ```
   ```bash
      docker run -p 8501:8501 ml-app
```


## Additional Shortcuts

Feel free to use the provided **Makefile** to automate common tasks like setting up a virtual environment, running tests, or cleaning up. You can enhance the **Makefile** to shorten tasks further.
