import openai
import gradio
from config import *

openai.api_key = OPENAI_API_KEY

messages = []



def CustomChatGPT(system_msg,user_msg):
    messages.append({"role": "system", "content": system_msg})
    messages.append({"role": "user", "content": user_msg})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply

demo = gradio.Interface(fn=CustomChatGPT, 
                        inputs=[gradio.Textbox(lines=2, placeholder="What type of chatbot would you like to create?",label="System Message"),
                                gradio.Textbox(lines=2, placeholder="Type your message here.",label="User Message")],
                        outputs="text", 
                        title="Custom ChatBot", 
                        description="Create your own chatbot with GPT-3.",
                        theme=gradio.themes.Soft())
demo.launch(share=True)