# My Flask Application

This repository contains the code to a simple Flask appliation.  The goal of this appliation is to use a simple trained model to generate an anomoly score from incoming data.
In this case the data domes from another file that simulated real life data. 

pip instal

## Usage

Train the model 
```shell
python TrainModel.py
```
Once the model is trained it is now callable.

No run the FLASK application.
```shell
python FLASK.py
```
Once the FLASK application is runing. Run the simulated data. A simulated data point will then be set every secord.
```shell
python Simulated Data.py
```
