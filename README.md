# Sentiment Analysis API

A REST API built with **FastAPI** and **Hugging Face DistilBERT** to classify English text as **POSITIVE** or **NEGATIVE**.

## Student Information

- **Name:** Đặng Nguyễn Yến Phương
- **Student ID:** 25127230
- **Course:** Computational Thinking

## Model

- **Model:** [DistilBERT SST-2](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english)
- **Task:** Sentiment Analysis
- **Output:** Sentiment label and confidence score (JSON)

## Project Structure

```text
lab2-sentiment-analysis-api/
├── main.py
├── test_api.py
├── requirements.txt
└── README.md
```

## Installation & Usage

**Create and activate a virtual environment (macOS/Linux):**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Run the API:**

```bash
uvicorn main:app --reload
```

Open Swagger UI: http://127.0.0.1:8000/docs


## 5. API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API information |
| GET | `/health` | Application status |
| POST | `/predict` | Sentiment prediction |

**Example Request (`POST /predict`):**

```json
{
  "text": "This dress is gorgeous!"
}
```

**Example Response:**

```json
{
  "text": "This dress is gorgeous",
  "sentiment": "POSITIVE",
  "confidence": 0.9998
}
```

## 6. Testing

With the API server running, execute:

```bash
python test_api.py
```

## 7. Demo Video

**Link:** https://youtu.be/vYLrOMeBWJ0
