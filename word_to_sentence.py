import openai

def word_to_text(a):

  openai.api_key = "api_key"



  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are an engish tutor , convert this discrete words to a complete sentence  and give me a single correct answer inside the double quotes: "},
      {"role": "user", "content": a}
    ]
  )
  return response.choices[0].message['content']
