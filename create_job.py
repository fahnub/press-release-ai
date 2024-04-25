from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

client.fine_tuning.jobs.create(
    training_file="file-yaoAIXZUnVIUcQOAqXRb8qZl",
    model="gpt-3.5-turbo",
    suffix="azizi-developments",
)
