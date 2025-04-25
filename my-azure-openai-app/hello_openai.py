import openai
import os

openai.api_key = os.getenv("AZURE_OPENAI_API_KEY", "DmtkfvD5rEipl79evhq1JW4TGIFOYz7Jri36XEiJbmls4H8f1MyRJQQJ99BDACYeBjFXJ3w3AAABACOGZCsq")  
openai.api_base = os.getenv("ENDPOINT_URL", "https://baltest.openai.azure.com/")  
openai.api_type = "azure"
openai.api_version = "2023-05-15"

response = openai.Completion.create(
    engine="gpt-35-turbo",
    prompt="Say Hello, World!t",
    max_tokens=10
)

print(response["choices"][0]["text"].strip())
