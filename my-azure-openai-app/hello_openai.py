import openai
import os

openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_type = "azure"
openai.api_version = "2023-05-15"

response = openai.Completion.create(
    engine="gpt-35-turbo",
    prompt="Say Hello, World!",
    max_tokens=10
)

print(response.choices[0].text.strip())
