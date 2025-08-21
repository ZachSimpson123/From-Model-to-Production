from flask  import Flask, request, jsonify
import joblib
import pandas as pd
from datetime import datetime

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Step 1: Receive JSON from sensor
    data = request.get_json()

    # ✅ Step 2: Extract values from JSON
    temperature = data.get('temperature')
    humidity = data.get('humidity')
    sound = data.get('sound')

    # ✅ Step 3: Create a DataFrame with column names
    features = pd.DataFrame([{
        "temperature": temperature,
        "humidity": humidity,
        "sound": sound
    }])

    # ✅ Step 4: Clean/Validate inputs
    '''
    In a production system, we would validate and clean the incoming data (e.g., check types, handle out-of-range values).
    In this simulation scenario, we assume the incoming data is correctly formatted and within expected ranges.
    However, a minimal check is recommended even during development.
    '''
    try:
        temperature = float(temperature)
        humidity = float(humidity)
        sound = float(sound)
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid data type provided.'}), 400

    # ✅ Step 5: Get prediction
    score = model.decision_function(features)[0]
    label = model.predict(features)[0]

    # More readable label
    score_status = "Anomaly Detected" if label == -1 else "Normal"

    # ✅ Step 6: Store the result locally
    record = {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": temperature,
        "humidity": humidity,
        "sound": sound,
        "score": score,
        "score_status": score_status
    }

    # Save to CSV (append if file exists)
    df_record = pd.DataFrame([record])
    df_record.to_csv('anomaly_log.csv', mode='a', index=False, header=not pd.io.common.file_exists('anomaly_log.csv'))

    # ✅ Step 7: Trigger alert system (optional)
    '''
    This step allows integration with external alerting mechanisms.

    If an anomaly is detected, the application can trigger alerts via:
    - Email (e.g., using SMTP)
    - SMS (e.g., via Twilio)
    - MQTT (to activate alarms or IoT devices)
    - Webhooks (to notify other systems or dashboards)
    - Factory control systems (e.g., triggering a siren or shutdown)
    
    This can be tailored to the factories requirements and is not needed for this specific project.
    '''

    # ✅ Step 8: Send response
    return jsonify({
        'Anomaly_Score': float(score),
        'Score_Status': score_status,
        'Date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

if __name__ == '__main__':
    app.run(port = 5000)