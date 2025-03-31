import streamlit as st
from services.predict_intent import predict_intent

st.set_page_config(page_title="SmartIntent Chatbot", layout="centered")
st.title("💬 SmartIntent: AI Chatbot with Intent Classification")

user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        intent = predict_intent(user_input)
        st.write(f"🔍 Predicted Intent: **{intent}**")
        if intent == "balance_inquiry":
            st.success("Sure! Your current balance is $3,200.")
        elif intent == "card_lost":
            st.success("I've locked your card. A new one will be issued in 5-7 business days.")
        elif intent == "close_account":
            st.success("I’m sorry to hear that. Let me connect you with a specialist.")
        else:
            st.warning("I’m not sure how to help with that yet.")
