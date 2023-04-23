# Importing the necessary libraries
import openai
import gradio as gr

# OpenAI API key goes here
openai.api_key = "Secret OpenAI API key"

# Define the initial message
messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]

# Define the chat function for handling user input and generating responses 
def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

# Gradio interface
inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
             description="Ask anything you want",
             theme="compact").launch(share=True)
