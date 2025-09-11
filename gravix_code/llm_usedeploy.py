#/home/rakesh/geminiadkteaching/gravix_code/gravix/bin/python
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
  api_key=os.getenv("GRAVIXLAYER_API_KEY"),
  base_url = "https://api.gravixlayer.com/v1/inference"
)

completion = client.chat.completions.create(
  model="qwen2-5-vl-3b-instruct-duuxg6",
  messages=[{"role": "user", "content": "Tell me a joke"}],
  temperature=0.7,
  max_tokens=2048,
  top_p=1,
  seed=0,
  stream=False
)

print(completion.choices[0].message)
