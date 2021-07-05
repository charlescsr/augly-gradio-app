import gradio as gr
from numpy import asarray
from augly.image import aug_np_wrapper, overlay_emoji

def emoji(img, opacity, x_coordinate, y_coordinate):
    np_aug_img = aug_np_wrapper(asarray(img), overlay_emoji, **{'opacity': opacity, 'y_pos': y_coordinate, 'x_pos': x_coordinate})

    return np_aug_img

iface = gr.Interface(emoji, 
        inputs=[gr.inputs.Image(shape=(200, 200)), gr.inputs.Slider(0.1, 1), gr.inputs.Slider(0.1, 1), gr.inputs.Slider(0.1, 1)], 
        outputs=["image"])
iface.launch()