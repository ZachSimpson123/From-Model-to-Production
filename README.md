# My Flask Application

This repository contains the code for a simple Flask application.
The goal of this application is to use a trained anomaly detection model to generate an anomaly score from incoming sensor data.

In this project, the sensor data is simulated to mimic real-life inputs (temperature, humidity, sound, etc.).

## Installation

Install dependencies:
```shell
pip install -r requirements.txt
```

## Usage

Train the model. Once trained a new file 'model.pkl' will be created. This is the file that contains the trained model and will be called by the flask application.
```shell
python TrainModel.py
```

Run the Flask application
```shell
python FLASK.py
```

Start sending simulated data. Each time a result is returned it is saved into a csv file (anomaly_log.csv)
```shell
python SimulatedData.py
```

A simulated data point will be sent every second to the Flask API.

## Workflow

TrainModel.py → trains and saves the anomaly detection model

FLASK.py → hosts the REST API (/predict) for predictions

SimulatedData.py → generates and sends fake sensor data to the API

