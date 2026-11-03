
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from transformers import pipeline

app = FastAPI(
    title="Sentiment Analysis API",
    description="English sentiment classification using DistilBERT"
)

MODEL_NAME = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

classifier = pipeline(
    "text-classification",
    model=MODEL_NAME
)


class TextInput(BaseModel):
    text: str = Field(min_length=1)


@app.get("/")
def home():
    return {
        "message": "Sentiment Analysis API",
        "model": MODEL_NAME
    }


@app.get("/health")
def status():
    return {"status": "ok"}


@app.post("/predict")
def predict(data: TextInput):
    if not data.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Input text cannot be empty"
        )

    try:
        result = classifier(
            data.text,
            truncation=True,
            max_length=512
        )[0]

        return {
            "text": data.text,
            "sentiment": result["label"],
            "confidence": round(result["score"], 4)
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Model inference failed"
        )
