from PIL import Image
import requests

import reflex as rx

class ImageState(rx.State):
    url: str = f"https://picsum.photos/id/1/200/300"
    image: Image.Image = Image.open(
        requests.get(url, stream=True).raw
    )

def image_pil_example():
    return rx.vstack(rx.image(src=ImageState.image))