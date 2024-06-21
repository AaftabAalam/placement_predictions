# Student Placement Prediction

This project aims to predict student placements using machine learning techniques. It includes a Jupyter Notebook for model creation, a Flask application for serving the model, and HTML templates for presenting the results.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Files Description](#files-description)

## Introduction

The Student Placement Prediction project leverages machine learning algorithms to predict whether a student will be placed in a job based on their academic and extracurricular profiles. This project is useful for educational institutions to help students prepare for the job market by identifying key factors influencing placement success.

## Project Structure

```
student-placement-prediction/
├── app.py
├── model/
│   └── placement_model.pkl
├── notebooks/
│   └── model_creation.ipynb
├── requirements.txt
├── templates/
│   └── index.html
├── README.md
```

## Installation

To get started with the project, follow these steps:

1. **Clone the repository**
   ```bash
   git clone https://github.com/AaftabAalam/placement_predictions
   cd placement_predictions
   ```

2. **Create a virtual environment and activate it**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Flask application**
   ```bash
   python app.py
   ```

2. **Open your web browser and navigate to**
   ```
   http://127.0.0.1:5000/
   ```

3. **Use the web interface to input student data and predict placement outcomes**

## Files Description

- **app.py**: The main Flask application file that runs the web server and handles user requests.
- **model/placement_model.pkl**: The pre-trained machine learning model for predicting student placements.
- **notebooks/model_creation.ipynb**: Jupyter Notebook containing the code for data preprocessing, model training, and evaluation.
- **requirements.txt**: List of required Python packages for the project.
- **templates/index.html**: HTML template for the web interface.

Feel free to open an issue if you have any questions or suggestions. Happy coding!
