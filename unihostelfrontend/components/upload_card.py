import reflex as rx

from unihostelfrontend.states.image_state import ImageUploadState


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
            ImageUploadState.image != "",
            rx.image(
                src=rx.get_upload_url(ImageUploadState.image),  # Construct URL properly
                width="200px",
                height="auto",
            ),
        ),
        rx.progress(value=ImageUploadState.progress, max=100),
        rx.cond(
            ~ImageUploadState.uploading,
            rx.button(
                "Upload",
                on_click=ImageUploadState.handle_upload(
                    rx.upload_files(
                        upload_id="upload3",
                        on_upload_progress=ImageUploadState.handle_upload_progress,
                    ),
                ),
            ),
            rx.button(
                "Cancel",
                on_click=ImageUploadState.cancel_upload,
            ),
        ),
        rx.text(
            "Total bytes uploaded: ",
            ImageUploadState.total_bytes,
        ),
        align="center",
    )


