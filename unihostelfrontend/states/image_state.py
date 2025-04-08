from PIL import Image
import requests

import reflex as rx


class UploadExample(rx.State):
    uploading: bool = False
    progress: int = 0
    total_bytes: int = 0
    image: str = ""  # Store the image URL

    @rx.event
    async def handle_upload(
            self, files: list[rx.UploadFile]
    ):
        current_file = files[0]  # Get first file since we only allow one
        upload_data = await current_file.read()
        outfile = rx.get_upload_dir() / current_file.name

        # Save the file first
        with outfile.open("wb") as file_object:
            file_object.write(upload_data)

        # Update the image var with the proper URL
        self.image = current_file.name
        self.total_bytes = len(upload_data)

    @rx.event
    def handle_upload_progress(self, progress: dict):
        self.uploading = True
        self.progress = round(progress["progress"] * 100)
        if self.progress >= 100:
            self.uploading = False

    @rx.event
    def cancel_upload(self):
        self.uploading = False
        self.image = ""  # Clear the image preview
        return rx.cancel_upload("upload3")


class ImageState(rx.State):
    url: str = f"https://picsum.photos/id/1/200/300"
    image: Image.Image = Image.open(
        requests.get(url, stream=True).raw
    )

def image_pil_example():
    return rx.vstack(rx.image(src=ImageState.image))
