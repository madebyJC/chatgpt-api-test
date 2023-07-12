# EXAMPLE 1

import openai

openai.api_key = "YOUR_API_KEY"

user_content = "Write an essay about Siberian Husky"
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                          messages=[{"role": "user", "content": user_content}])

print(completion.choices[0].message.content)

# ----------------------------------------------------------------------------------------------------------------------
# EXAMPLE 2

# import openai
#
# openai.api_key = "YOUR_API_KEY"
#
# messages = []
# system_msg = input("What type of chatbot would you like to create?\n")
# messages.append({"role": "system", "content": system_msg})
#
# print("You can start chatting with the chatbot now.")
# while input != "quit()":
#     message = input()
#     messages.append({"role": "user", "content": message})
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages)
#     reply = response["choices"][0]["message"]["content"]
#     messages.append({"role": "assistant", "content": reply})
#     print("\n" + reply + "\n")

# ----------------------------------------------------------------------------------------------------------------------
# EXAMPLE 3

# import openai
# import gradio
#
# openai.api_key = "YOUR_API_KEY"
#
# messages = [{"role": "system", "content": "Hello, how are you?"}]
#
#
# def custom_chatgpt(user_input):
#     messages.append({"role": "user", "content": user_input})
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages)
#     chatgpt_reply = response["choices"][0]["message"]["content"]
#     messages.append({"role": "assistant", "content": chatgpt_reply})
#     return chatgpt_reply
#
#
# demo = gradio.Interface(fn=custom_chatgpt, inputs="text", outputs="text", title="Custom ChatGPT")
#
# demo.launch(share=False)
