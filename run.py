from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

completion = client.chat.completions.create(
    model="ft:gpt-3.5-turbo-0125:fahnub:azizi-developments:9Hd0fE7k",
    messages=[
        {
            "role": "system",
            "content": "Your role is to write Press Releases for Azizi Developments, a real estate company in Dubai.",
        },
        {
            "role": "user",
            "content": "Write a Press Release about 'Azizi Developments launches new project in Palm Jumeirah'",
        },
    ],
)
print(completion.choices[0].message)
