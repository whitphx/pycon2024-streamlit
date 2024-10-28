import gradio as gr

# Core logic function
def process_data(number, text):
    transformed_number = number * 2
    uppercased_text = text.upper()
    return transformed_number, uppercased_text

# Create and launch Gradio Interface
demo = gr.Interface(
    fn=process_data,
    inputs=[
        gr.Number(label="Enter a number"),
        gr.Textbox(label="Enter some text"),
    ],
    outputs=[
        gr.Textbox(label="Transformed Number"),
        gr.Textbox(label="Uppercased Text")
    ],
    title="Data Processor",
)

demo.launch()
