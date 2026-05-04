import gradio as gr
import ollama

MEMORY = []


def to_text(content):
   if isinstance(content, str):
       return content
   if isinstance(content, dict):
       if "text" in content:
           return str(content["text"])
       return str(content)
   if isinstance(content, list):
       return " ".join(
           str(part["text"]) if isinstance(part, dict) and "text" in part else str(part)
           for part in content
       )
   return str(content)


def chatbot(question,temperature=0.1, model='gemma3:1b'):
   # Send the full conversation (memory + current question) to Ollama.
   messages = []

   for item in MEMORY:
       messages.append(
           {
               "role": item["role"],
               "content": to_text(item["content"]),
           }
       )

   messages.append({'role': 'user', 'content': to_text(question)})

   response = ollama.chat(
       model=model,
       messages=messages,
       options=ollama.Options(temperature=temperature)
   )

   # Save both user and assistant messages for next turns.
   answer = response['message']['content']
   MEMORY.append({'role': 'user', 'content': to_text(question)})
   MEMORY.append({'role': 'assistant', 'content': to_text(answer)})

   return answer


def main():
   demo = gr.Interface(
       fn=chatbot,
       inputs=[
           gr.Textbox(label="Question", lines=2, placeholder="Type your message here..."),
           gr.Slider(label="Temperature", minimum=0.0, maximum=1.0, step=0.01, value=0.7),
           gr.Dropdown(label="Model", choices=["gemma3:1b", "gemma3:4b"], value="gemma3:1b"),
       ],
       outputs=gr.Textbox(label="Response", lines=20),
       title="Ollama Chatbot",
       description="A simple chatbot interface using Ollama models with adjustable temperature and model selection."
   )

   demo.launch()


if __name__ == "__main__":
   main() 