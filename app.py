import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()
st.set_page_config(page_title="PR Writer")
st.title("Azizi Developments Press Release Writer")


def generate_response(input_text):
    input_prompt = f"Write a press release about '{input_text}'"

    article = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-0125:fahnub:azizi-developments:9Hd0fE7k",
        messages=[
            {
                "role": "system",
                "content": "Your role is to write Press Releases for Azizi Developments, a real estate company in Dubai.",
            },
            {"role": "user", "content": input_prompt},
        ],
    )

    input_prompt2 = f"Here is text from a press release: '{article.choices[0].message.content}. Format it for me. Don't re-write or add anything, just apply formatting and structure. Don't explain anything, just start writing the press release."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Your role is to ensure proper punctuation, sentence structure, commas, periods, and new lines for new paragraphs within the provided text.",
            },
            {"role": "user", "content": input_prompt2},
        ],
        stream=True,
    )

    st.write_stream(response)


with st.form("form"):
    text = st.text_area(
        "Press Release title:",
        "Azizi Developments launches new project in Palm Jumeirah",
    )
    submitted = st.form_submit_button("Write")

    if submitted:
        generate_response(text)
