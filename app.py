import streamlit as st
import openai
import os

# Set your API key from Streamlit secrets
openai.api_key = os.getenv("OPENAI_API_KEY") or st.secrets["OPENAI_API_KEY"]

st.title("🍽️ AI Recipe Generator")

dish_name = st.text_input("Enter a dish name:")

if st.button("Get Recipe"):
    if not dish_name:
        st.warning("Please enter a dish name.")
    else:
        with st.spinner("Fetching recipe..."):
            try:
                client = openai.OpenAI()
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": f"Give me a detailed recipe for {dish_name}, including ingredients and step-by-step instructions."}
                    ],
                    max_tokens=500,
                )
                recipe = response.choices[0].message.content
                st.text_area("🍳 Recipe:", value=recipe, height=400)
            except Exception as e:
                st.error(f"Error: {e}")
