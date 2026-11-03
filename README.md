# Sentiment Analysis API

A REST API built with **FastAPI** and **Hugging Face DistilBERT** to classify English text as **POSITIVE** or **NEGATIVE**.

## Student Information

- **Name:** [Your Name]
- **Student ID:** [Your Student ID]
- **Course:** Computational Thinking – Lab 2

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

*The model downloads automatically on the first run.*

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

*Confidence score is illustrative.*

## 6. Testing

With the API server running, execute:

```bash
python test_api.py
```

The script tests API endpoints, positive/negative inputs, and input validation using `requests`.

## 7. Demo Video

**Link:** [Add your video link here]

The video demonstrates the model, source code, application startup, and API testing with at least two inputs.

**Duration:** Maximum 5 minutes.