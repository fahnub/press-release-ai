from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

client.files.create(file=open("articles.jsonl", "rb"), purpose="fine-tune")
