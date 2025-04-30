import google.generativeai as genai
import os
import gradio as gr
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
initial_prompt = "Você é um consultor de desenvolvimento de projetos."
model = genai.GenerativeModel("gemini-1.5-flash",
                              system_instruction=initial_prompt)
chat = model.start_chat()
def gradio_wrapper(message, _history):
    response = chat.send_message(message)
    return response.text
chat_interface = gr.ChatInterface(gradio_wrapper)
chat_interface.launch()
