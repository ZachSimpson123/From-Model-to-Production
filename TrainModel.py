from sklearn.ensemble import IsolationForest
import pandas as pd
import random
import joblib

# Simulated training data

df = pd.DataFrame ({
    "temperature":[random.gauss(70,2) for _ in range(1000)],
    "humidity":[random.gauss(45,2) for _ in range(1000)],
    "sound":[random.gauss(65,2) for _ in range(1000)],
})

model = IsolationForest(contamination=0.02, random_state = 42)
model.fit(df)


# Save the model to disk
joblib.dump(model, 'model.pkl')

print("✅ Model saved as 'model.pkl'")


