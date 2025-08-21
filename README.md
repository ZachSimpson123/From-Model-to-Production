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

Train the model
```shell
python TrainModel.py
```

Run the Flask application
```shell
python FLASK.py
```

The API will be available at:
http://127.0.0.1:5000/predict

Start sending simulated data
```shell
python SimulatedData.py
```

A simulated data point will be sent every second to the Flask API.

## Workflow

TrainModel.py → trains and saves the anomaly detection model

FLASK.py → hosts the REST API (/predict) for predictions

SimulatedData.py → generates and sends fake sensor data to the API

