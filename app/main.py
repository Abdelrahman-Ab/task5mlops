import gradio as gr
import ollama

MODEL_NAME = "codellama:7b-instruct"

def generate_code(prompt):
    """
    Sends the prompt to the local model and returns the response text.
    """
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']

with gr.Blocks() as demo:
    gr.Markdown("## Local AI Coding Assistant")
    
    prompt_input = gr.Textbox(
        label="Enter your coding prompt",
        placeholder="Write Python code to ...",
        lines=5
    )
    
    output_box = gr.Textbox(label="Model Output", lines=15)
    
    submit_btn = gr.Button("Generate")
    submit_btn.click(fn=generate_code, inputs=prompt_input, outputs=output_box)

if __name__ == "__main__":
    demo.launch()
