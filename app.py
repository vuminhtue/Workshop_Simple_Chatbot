import gradio as gr

def hello(name):
    return "Hello " + name + "!"
def main():
    demo = gr.Interface(fn=hello,
                        inputs=gr.Textbox(lines=2),
                        outputs=gr.Textbox(lines=10))

    demo.launch()
    
if __name__ == "__main__":
    main()  