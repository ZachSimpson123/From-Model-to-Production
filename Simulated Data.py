import random, time
import requests

#This is the url that we use to send the simulated stream data  to our flask app
url = 'http://127.0.0.1:5000/predict'
while True:
    if random.random() < 0.01: # 1% chance to generate and anomaly
    # Generate anomaly with out-of-range values
        continuous_data = {
        "temperature": random.uniform(80, 100),  # way above normal
        "humidity": random.uniform(10, 30),  # below normal
        "sound": random.uniform(80, 100),  # above normal
        }
    # Step 1: Simulate non-anomaly sensor readings
    else:
        continuous_data = {
        # in °C
        "temperature": random.gauss(70,2),
        # in %
        "humidity": random.gauss(45, 2),
        # in dB
        "sound": random.gauss(65,  2),
    }

    # Step 2: Send data to Flask API
    response = requests.post(url, json=continuous_data)
    print(f"Sent: {continuous_data} → Received: {response.json()}")

    # Step 3: Wait for next reading
    time.sleep(1)





