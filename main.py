import openai

openai.api_key = "YOUR_API_KEY"

user_content = "Write an essay about Siberian Husky"
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                          messages=[{"role": "user", "content": user_content}])

print(completion.choices[0].message.content)
