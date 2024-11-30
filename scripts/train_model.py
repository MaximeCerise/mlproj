import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import joblib
import json


data = pd.read_csv("data/cifar10_emb.csv")


data['embedding'] = data['embedding'].apply(lambda x: np.array(json.loads(x)))
X = np.vstack(data['embedding'].values) 
y = data["target"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))


ref_data = pd.DataFrame({
    'embedding': [json.dumps(embedding.tolist()) for embedding in X_test], 
    'target': y_test.values,
    'prediction': y_pred
})


ref_data.to_csv("data/ref_data.csv", index=False)


joblib.dump(model, "artifacts/model.pkl")
print("Modèle sauvegardé dans artifacts/model.pkl")