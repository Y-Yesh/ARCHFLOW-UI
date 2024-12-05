import gradio as gr 

def temp(Image) :
    
    print(Image)


    return Image['layers'][0], Image['composite']


with gr.Blocks() as app :

    with gr.Row() :
        input = gr.ImageEditor(interactive=True,show_fullscreen_button=True, type='pil')
    with gr.Row() :

        output2 = gr.Image()
        output3 = gr.Image()




    input.change(temp,inputs=[input],outputs=[output2,output3])




app.launch()

