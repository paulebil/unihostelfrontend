import reflex as rx
from ..templates.template import base_template

from unihostelfrontend.components.upload_card import upload_form

from unihostelfrontend.states.room_state import RoomState




@rx.page(route="/create/room/[room_hostel_id]", title="Create Room")
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



