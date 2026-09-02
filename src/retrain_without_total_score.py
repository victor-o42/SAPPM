"""
Retrain models without total_score
Strictly trains models using ONLY:
- weekly_self_study_hours
- attendance_percentage
- class_participation

Ensures total_score is completely removed from features, SHAP attributions, and importance charts.
"""

import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report

print("Loading dataset...")
df = pd.read_csv("data/student_performance.csv", nrows=150000)

features = ["weekly_self_study_hours", "attendance_percentage", "class_participation"]
print(f"Features: {features}")

X = df[features]
y = df["grade"]

encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

print("\nTraining Random Forest Classifier (without total_score)...")
rf_model = RandomForestClassifier(
    n_estimators=100,
    max_depth=12,
    random_state=42,
    n_jobs=-1
)
rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)
rf_acc = accuracy_score(y_test, rf_pred)
print(f"Random Forest Accuracy: {rf_acc * 100:.2f}%")
print("RF Feature Importances:", dict(zip(features, rf_model.feature_importances_)))

print("\nTraining XGBoost Classifier (without total_score)...")
xgb_model = XGBClassifier(
    n_estimators=100,
    max_depth=6,
    learning_rate=0.1,
    eval_metric='mlogloss',
    random_state=42,
    n_jobs=-1
)
xgb_model.fit(X_train, y_train)

xgb_pred = xgb_model.predict(X_test)
xgb_acc = accuracy_score(y_test, xgb_pred)
print(f"XGBoost Accuracy: {xgb_acc * 100:.2f}%")
print("XGB Feature Importances:", dict(zip(features, xgb_model.feature_importances_)))

os.makedirs("models", exist_ok=True)

# Save Random Forest models
joblib.dump(rf_model, "models/random_forest_model.pkl")
joblib.dump(encoder, "models/label_encoder.pkl")

# Save Best Model (XGBoost / RF)
best_model = xgb_model if xgb_acc >= rf_acc else rf_model
joblib.dump(best_model, "models/best_model.pkl")
joblib.dump(encoder, "models/best_label_encoder.pkl")

print("\nAll models retrained and saved successfully without total_score!")
