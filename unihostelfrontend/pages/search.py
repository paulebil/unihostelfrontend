import reflex as rx
from ..templates.template import base_template


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


def upload_form():
    return rx.vstack(
        rx.upload(
            rx.text(
                "Drag and drop an image here or click to select"
            ),
            id="upload3",
            border="1px dotted rgb(107,99,246)",
            padding="5em",
            max_files=1,
            accept={
                "image/png": [".png"],
                "image/jpeg": [".jpg", ".jpeg"],
                "image/gif": [".gif"],
                "image/webp": [".webp"],
            },
        ),
        rx.vstack(
            rx.foreach(
                rx.selected_files("upload3"), rx.text
            )
        ),
        # Add image preview with proper URL construction
        rx.cond(
            UploadExample.image != "",
            rx.image(
                src=rx.get_upload_url(UploadExample.image),  # Construct URL properly
                width="200px",
                height="auto",
            ),
        ),
        rx.progress(value=UploadExample.progress, max=100),
        rx.cond(
            ~UploadExample.uploading,
            rx.button(
                "Upload",
                on_click=UploadExample.handle_upload(
                    rx.upload_files(
                        upload_id="upload3",
                        on_upload_progress=UploadExample.handle_upload_progress,
                    ),
                ),
            ),
            rx.button(
                "Cancel",
                on_click=UploadExample.cancel_upload,
            ),
        ),
        rx.text(
            "Total bytes uploaded: ",
            UploadExample.total_bytes,
        ),
        align="center",
    )


@rx.page(route="/search", title="Search Hostels")
def search() -> rx.Component:
    """Search page for finding hostels."""
    return base_template(
        content=rx.container(
            upload_form(),
        ),
        title="Search Hostels",
    )


