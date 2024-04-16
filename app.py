import openai
import streamlit as st

# Read the API key from file
with open('open_key.txt') as f:
    api_key = f.read().strip()

# Setting up the OpenAI client with the API key
openai.api_key = api_key

# Streamlit UI
st.title('AI Code Reviewer ')
st.subheader("Enter your code to fix the bugs!")

# Text input for code
prompt = st.text_area("Enter your code: ")

# Button to generate response
if st.button('Generate'):
    # Sending prompt to OpenAI's GPT-3.5 model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "You are a code bug fixer, you return the bugs in code in an ordered list and also the correct code in jupyter notebook look."},
            {"role": "user", "content": prompt}
        ]
    )

    # Displaying the response
    st.write(response['choices'][0]['message']['content'])


