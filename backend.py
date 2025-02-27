from fastapi import FastAPI, Query
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

app = FastAPI()

# Load Titanic dataset from GitHub
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

@app.get("/")
def read_root():
    return {"message": "Titanic Chatbot API is running!"}

@app.get("/predict")
def predict(query: str = Query(..., description="Enter your question")):
    try:
        if "percentage of passengers were male" in query.lower():
            male_count = df[df["Sex"] == "male"].shape[0]
            total_count = df.shape[0]
            percentage = (male_count / total_count) * 100
            return {"answer": f"{percentage:.2f}% of passengers were male."}

        elif "histogram of passenger ages" in query.lower():
            return generate_histogram()

        elif "average ticket fare" in query.lower():
            avg_fare = df["Fare"].mean()
            return {"answer": f"The average ticket fare was ${avg_fare:.2f}"}

        elif "passengers embarked from each port" in query.lower():
            embarked_counts = df["Embarked"].value_counts().to_dict()
            return {"answer": embarked_counts}

        else:
            return {"answer": "Sorry, I don't understand that question."}

    except Exception as e:
        return {"error": str(e)}

# Function to generate histogram
def generate_histogram():
    plt.figure(figsize=(6, 4))
    sns.histplot(df["Age"].dropna(), bins=20, kde=True)
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.title("Histogram of Passenger Ages")

    # Convert plot to base64 string
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    img_str = base64.b64encode(buffer.getvalue()).decode()

    return {"image": img_str}
