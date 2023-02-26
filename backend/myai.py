import os
import openai
import dotenv
# openai.api_key = "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"

# openai.Completion.create()
# response = openai.Completion.create(
#   engine="text-davinci-003",
#   prompt="Conver 5 dollars to rupees",
#   max_tokens=15,
#   stop= None,
#   temperature=0.5
# )

# message = response.choices[0].text

# print(message)

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="How many goals does Lionel Messi have? ",
  max_tokens=100,
  temperature=0
)


print(response.choices[0].text)