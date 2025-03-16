import numpy as np
import pickle
from tensorflow.keras.models import load_model
from sqlalchemy.orm import Session
from crud import get_latest_student


def load_models(model_path: str):
    """Load the trained model."""
    return load_model(model_path)


def prepare_features(latest_entry):
    """Extract and preprocess features from the latest student entry."""
    if not latest_entry:
        return None
    
    raw_features = {
        "Gender": latest_entry.Gender,
        "Age": latest_entry.Age,
        "Attendance_Percentage": latest_entry.academic_details.Attendance_Percentage,
        "Midterm_Score": latest_entry.academic_details.Midterm_Score,
        "Final_Score": latest_entry.academic_details.Final_Score,
        "Assignments_Avg": latest_entry.academic_details.Assignments_Avg,
        "Quizzes_Avg": latest_entry.academic_details.Quizzes_Avg,
        "Participation_Score": latest_entry.academic_details.Participation_Score,
        "Projects_Score": latest_entry.academic_details.Projects_Score,
        "Study_Hours_per_Week": latest_entry.study_habits.Study_Hours_per_Week or 0,
        "Extracurricular_Activities": latest_entry.extracurriculars.Extracurricular_Activities or 0,
        "Internet_Access_at_Home": latest_entry.family_background.Internet_Access_at_Home or 0,
        "Family_Income_Level": latest_entry.family_background.Family_Income_Level or 0,
        "Stress_Level": latest_entry.study_habits.Stress_Level or 0,
        "Sleep_Hours_per_Night": latest_entry.study_habits.Sleep_Hours_per_Night or 0
    }
    
    return raw_features


def preprocess_features(features, final_columns, scaler):
    """Ensure the feature order matches training data and apply preprocessing."""
    import pandas as pd

    # Convert dictionary to DataFrame
    df = pd.DataFrame([features])

    # One-hot encode categorical columns (if needed)
    df = pd.get_dummies(df)

    # Ensure all required columns exist and maintain order
    for col in final_columns:
        if col not in df.columns:
            df[col] = 0  # Assign 0 to missing one-hot encoded categories

    df = df[final_columns]  # Ensure correct column order

    # Apply scaling
    scaled_features = scaler.transform(df)

    return scaled_features


def predict_total_score(db: Session, model_path: str):
    """Predict the total score of the latest student."""
    latest_entry = get_latest_student(db)

    if not latest_entry:
        return {"error": "No data available"}

    # Prepare raw features
    raw_features = prepare_features(latest_entry)

    # Load preprocessing metadata (column order + scaler)
    with open("final_columns.pkl", "rb") as f:
        final_columns = pickle.load(f)

    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)

    # Preprocess the new student's features
    processed_features = preprocess_features(raw_features, final_columns, scaler)

    # Load the model
    model = load_models(model_path)

    # Make prediction
    prediction = model.predict(processed_features)

    return {"predicted_total_score": float(prediction[0][0])}
