from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

print(client.fine_tuning.jobs.list())

# client.fine_tuning.jobs.retrieve("ftjob-abc123")

# client.fine_tuning.jobs.cancel("ftjob-abc123")

# client.fine_tuning.jobs.list_events(fine_tuning_job_id="ftjob-abc123", limit=10)

# client.models.delete("ft:gpt-3.5-turbo:acemeco:suffix:abc123")