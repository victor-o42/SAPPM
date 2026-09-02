import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

# Load dataset
df = pd.read_csv("data/student_performance.csv")

# Features and target (strictly without total_score)
features = ["weekly_self_study_hours", "attendance_percentage", "class_participation"]
X = df[features]
y = df["grade"]

# Encode labels
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42
)

# =========================
# Random Forest Model
# =========================
rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_predictions = rf_model.predict(X_test)

rf_accuracy = accuracy_score(y_test, rf_predictions)

print("\nRandom Forest Accuracy:")
print(f"{rf_accuracy * 100:.2f}%")

# =========================
# XGBoost Model
# =========================
xgb_model = XGBClassifier(
    eval_metric='mlogloss',
    random_state=42
)

xgb_model.fit(X_train, y_train)

xgb_predictions = xgb_model.predict(X_test)

xgb_accuracy = accuracy_score(y_test, xgb_predictions)

print("\nXGBoost Accuracy:")
print(f"{xgb_accuracy * 100:.2f}%")

# =========================
# Model Comparison
# =========================
print("\nModel Comparison")
print("-------------------------")
print(f"Random Forest: {rf_accuracy * 100:.2f}%")
print(f"XGBoost:       {xgb_accuracy * 100:.2f}%")

# =========================
# Save Best Model
# =========================
if xgb_accuracy > rf_accuracy:
    best_model = xgb_model
    print("\nBest Model: XGBoost")
else:
    best_model = rf_model
    print("\nBest Model: Random Forest")

# Save best model
joblib.dump(best_model, "models/best_model.pkl")

# Save encoder
joblib.dump(encoder, "models/best_label_encoder.pkl")

print("\nBest model saved successfully.")