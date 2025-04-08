import reflex as rx
from ..templates.template import base_template
from datetime import datetime


class HostelState(rx.State):
    """The hostel state."""
    name: str = ""
    image_url: str = ""
    description: str = ""
    location: str = ""
    average_price: int = 0
    available_rooms: int = 0
    rules_and_regulations: str = ""
    amenities: str = ""

    @rx.event
    async def create_hostel(self, form_data: dict):
        """Create a new hostel."""
        # Get the image URL from the upload component
        image_url = UploadExample.image  # Access the image URL from upload state

        # Add image URL to form data
        form_data["image_url"] = image_url

        api = ""

        # Make API call to your backend
        # try:
        #     response = await api.post("/hostels/", json=form_data)
        #     if response.status_code == 200:
        #         return rx.redirect("/create/room", is_external=True)
        #     else:
        #         return rx.window_alert("Failed to create hostel")
        # except Exception as e:
        #     return rx.window_alert(f"Error: {str(e)}")

        return rx.redirect("/create/room", is_external=False)


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


@rx.page(route="/create/hostel", title="Create Hostel")
def create_hostel() -> rx.Component:
    """Create Hostel page."""
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
                                "Create a Hostel",
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
                                "Hostel Name",
                                size="3",
                                weight="medium",
                                text_align="left",
                                width="100%",
                            ),
                            rx.input(
                                placeholder="Hostel Name",
                                name="name",
                                required=True,
                                size="3",
                                width="100%",
                            ),
                            justify="start",
                            spacing="2",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.text(
                                "Description",
                                size="3",
                                weight="medium",
                            ),
                            rx.text_area(
                                placeholder="Description",
                                name="description",
                                required=True,
                                min_height="100px",
                                width="100%",
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.text(
                                "Location (comma separated)",
                                size="3",
                                weight="medium",
                                text_align="left",
                                width="100%",
                            ),
                            rx.input(
                                placeholder="Location (comma separated)",
                                name="location",
                                required=True,
                                width="100%",
                            ),
                            justify="start",
                            spacing="3",
                            width="100%",
                        ),

                        rx.vstack(
                            rx.text(
                                "Average Price",
                                size="3",
                                weight="medium",
                                text_align="left",
                                width="100%",
                            ),
                            rx.input(
                                placeholder="Average Price",
                                name="average_price",
                                type="number",
                                required=True,
                                width="100%",
                            ),
                            justify="start",
                            spacing="3",
                            width="100%",
                        ),

                        rx.vstack(
                            rx.text(
                                "Available Rooms",
                                size="3",
                                weight="medium",
                                text_align="left",
                                width="100%",
                            ),
                            rx.input(
                                placeholder="Available Rooms",
                                name="available_rooms",
                                type="number",
                                required=True,
                                width="100%",
                            ),
                            justify="start",
                            spacing="3",
                            width="100%",
                        ),

                        rx.vstack(
                            rx.text(
                                "Rules and Regulations (comma separated)",
                                size="3",
                                weight="medium",
                                text_align="left",
                                width="100%",
                            ),
                            rx.text_area(
                                placeholder="Rules and Regulations (comma separated)",
                                name="rules",
                                required=True,
                                width="100%",
                                min_height="100px"
                            ),
                            justify="start",
                            spacing="3",
                            width="100%",
                        ),

                        rx.vstack(
                            rx.text(
                                "Ammenities (comma separated)",
                                size="3",
                                weight="medium",
                                text_align="left",
                                width="100%",
                            ),
                            rx.text_area(
                                placeholder="Amenities (comma separated)",
                                name="rules",
                                required=True,
                                width="100%",
                                min_height="100px"
                            ),
                            justify="start",
                            spacing="3",
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
                            "Create Hostel",
                            type="submit",
                            width="100%",
                            size="3",
                        ),
                        spacing="6",
                        width="100%",
                    ),
                    on_submit=HostelState.create_hostel,  # on_submit goes on the form
                    reset_on_submit=True,
                ),
                size="4",
                max_width="50em",
                width="100%",
            ),
            title="Create Hostel",
            spacing="4",
            justify="center",
        ),

    )

