import reflex as rx
from ..templates.template import base_template


class RoomState(rx.State):
    """The room state."""
    room_number: str = ""
    price_per_semester: float = 0.0
    room_type: str = "DOUBLE"
    bathroom: bool = False
    balcony: bool = False
    capacity: int
    hostel_id: int = 0  # This should be passed from the previous page

    @rx.event
    async def create_room(self, form_data: dict):
        """Create a new room."""

        return rx.redirect("/search")


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




@rx.page(route="/create/room", title="Create Room")
def create_room() -> rx.Component:
    """Create Room page."""
    return base_template(
        content=rx.flex(
            rx.card(
                rx.form(
                    rx.vstack(
                        rx.center(
                            rx.image(
                                src="/logo.jpg",
                                width="2.5em",
                                height="auto",
                                border_radius="25%",
                            ),
                            rx.heading(
                                "Create a Room",
                                size="6",
                                as_="h2",
                                text_align="center",
                                width="100%",
                            ),
                            direction="column",
                            spacing="5",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.text(
                                "Room Number",
                                size="3",
                                weight="medium",
                                text_align="left",
                                width="100%",
                            ),
                            rx.input(
                                placeholder="Room Number",
                                name="room_number",
                                required=True,
                                width="100%",
                            ),
                            justify="start",
                            spacing="2",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.text(
                                "Room Price per Semester",
                                size="3",
                                weight="medium",
                                text_align="left",
                                width="100%",
                            ),
                            rx.input(
                                placeholder="Price per Semester",
                                name="price_per_semester",
                                type="number",
                                required=True,
                                width="100%",
                            ),
                            justify="start",
                            spacing="2",
                            width="100%",
                        ),

                        rx.vstack(
                            rx.text(
                                "Room Type",
                                size="3",
                                weight="medium",
                                text_align="left",
                                width="100%",
                            ),
                            rx.select(
                                ["SINGLE", "DOUBLE"],
                                placeholder="Room Type",
                                name="room_type",
                                required=True,
                                width = "100%",
                            ),
                            justify="start",
                            spacing="2",
                            width="100%",
                        ),

                        rx.vstack(

                            rx.text(
                                "Room Amenities",
                                size="3",
                                weight="medium",
                                text_align="left",
                                width="100%",
                            ),

                            rx.hstack(
                                rx.checkbox("Has Bathroom", name="bathroom"),
                                rx.checkbox("Has Balcony", name="balcony"),
                            ),
                            justify="start",
                            spacing="2",
                            width="100%",
                        ),

                        rx.vstack(
                            rx.text(
                                "Room Capacity",
                                size="3",
                                weight="medium",
                                text_align="left",
                                width="100%",
                            ),
                            rx.input(
                                placeholder="Capacity",
                                name="capacity",
                                type="number",
                                value=2,
                                required=True,
                                width="100%",
                            ),
                            justify="start",
                            spacing="2",
                            width="100%",
                        ),

                        rx.vstack(
                            rx.text(
                                "Upload an Image",
                                size="3",
                                weight="medium",
                                text_align="left",
                                width="100%",
                            ),
                            upload_form(),
                        ),
                        rx.button(
                            "Create Room",
                            type="submit",
                            width="100%",
                            size="3",
                        ),
                        spacing="6",
                        width="100%",
                    ),
                    on_submit=RoomState.create_room,  # on_submit goes on the form
                    reset_on_submit=True,
                ),
                size="4",
                max_width="50em",
                width="100%",
            ),
            title="Create Room",
            spacing="4",
            justify="center",
        ),

    )



