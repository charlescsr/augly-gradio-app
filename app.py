import os
import gradio as gr
from numpy import asarray
from augly.image import aug_np_wrapper, overlay_emoji
PATH = os.getenv('MAIN_PATH_TMP')

emoji_list = ["Heart Eyes", "Grinning with sweat", "Tears of Joy", "Scream", "Disappointed"]

def emoji(img, emoji, emoji_size, opacity, x_coordinate, y_coordinate):
    np_aug_img = None
    if emoji == "Heart Eyes":
        np_aug_img = aug_np_wrapper(asarray(img), overlay_emoji, **{'emoji_size': emoji_size, 'opacity': opacity, 'y_pos': y_coordinate, 'x_pos': x_coordinate})

    elif emoji == "Grinning with sweat":
        np_aug_img = aug_np_wrapper(asarray(img), overlay_emoji, **{'emoji_path': os.path.join(PATH, 'grinning_face_with_sweat.png'), 'emoji_size': emoji_size, 'opacity': opacity, 'y_pos': y_coordinate, 'x_pos': x_coordinate})

    elif emoji == "Tears of Joy":
        np_aug_img = aug_np_wrapper(asarray(img), overlay_emoji, **{'emoji_path': os.path.join(PATH, 'face_with_tears_of_joy.png'), 'emoji_size': emoji_size, 'opacity': opacity, 'y_pos': y_coordinate, 'x_pos': x_coordinate})

    elif emoji == "Scream":
        np_aug_img = aug_np_wrapper(asarray(img), overlay_emoji, **{'emoji_path': os.path.join(PATH, 'face_screaming_in_fear.png'), 'emoji_size': emoji_size, 'opacity': opacity, 'y_pos': y_coordinate, 'x_pos': x_coordinate})

    else:
        np_aug_img = aug_np_wrapper(asarray(img), overlay_emoji, **{'emoji_path': os.path.join(PATH, 'disappointed_face.png'), 'emoji_size': emoji_size, 'opacity': opacity, 'y_pos': y_coordinate, 'x_pos': x_coordinate})

    return np_aug_img

iface = gr.Interface(emoji, 
        inputs=[gr.inputs.Image(shape=(200, 200)), gr.inputs.Dropdown(emoji_list, default="Heart Eyes"), gr.inputs.Slider(0.1, 1), gr.inputs.Slider(0.1, 1), gr.inputs.Slider(0.1, 1), gr.inputs.Slider(0.1, 1)], 
        outputs=["image"])
iface.launch()