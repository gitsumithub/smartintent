# SmartIntent – Conversational AI for Intent Classification

A demonstration of an end-to-end conversational AI system using NLP for intent detection and a chatbot interface.

## Features
- Ingests user queries from chat (simulated)
- Classifies intent using a trained NLP model
- Displays tailored chatbot responses

## Intents Supported
- `balance_inquiry`
- `card_lost`
- `close_account`

## Setup

```bash
pip install -r requirements.txt
python model/train_intent_model.py
streamlit run app.py
```
