import reflex as rx
from ..templates.template import base_template
from datetime import datetime
from enum import Enum

# Room Type Enum
class RoomType(str, Enum):
    SINGLE = "single"
    DOUBLE = "double"


# Room Model
class Room(rx.Model):
    """Model representing a room in the database."""
    id: int
    hostel_id: int
    room_number: str
    price_per_semester: float
    room_type: RoomType
    availability: bool = True
    capacity: int = 2
    occupancy: int = 0
    bathroom: bool = False
    balcony: bool = False
    image_url: str | None
    booked_status: bool = True
    created_at: datetime
    updated_at: datetime | None


class RoomState(rx.State):
    """The room state."""
    room_number: str = ""
    price_per_semester: float = 0.0
    room_type: str = "DOUBLE"
    bathroom: bool = False
    balcony: bool = False
    capacity: int = 2
    hostel_id: int = 0  # This should be passed from the previous page

    @rx.event
    async def create_room(self, form_data: dict):
        """Create a new room."""
        with rx.session() as session:
            new_room = Room(
                hostel_id=self.hostel_id,  # Use the hostel_id from state
                room_number=form_data["room_number"],
                price_per_semester=float(form_data["price_per_semester"]),
                room_type=form_data["room_type"],
                bathroom=bool(form_data.get("bathroom", False)),
                balcony=bool(form_data.get("balcony", False)),
                capacity=int(form_data["capacity"])
            )
            session.add(new_room)
            session.commit()

        return rx.redirect("/search")


@rx.page(route="/create/room", title="Create Room")
def create_room() -> rx.Component:
    """Create Room page."""
    return base_template(
        content=rx.container(
            rx.vstack(
                rx.heading("Add Room to Hostel", size="7"),
                rx.form(
                    rx.vstack(
                        rx.input(
                            placeholder="Room Number",
                            name="room_number",
                            required=True
                        ),
                        rx.input(
                            placeholder="Price per Semester",
                            name="price_per_semester",
                            type="number",
                            required=True
                        ),
                        rx.select(
                            ["SINGLE", "DOUBLE"],
                            placeholder="Room Type",
                            name="room_type",
                            required=True
                        ),
                        rx.hstack(
                            rx.checkbox("Has Bathroom", name="bathroom"),
                            rx.checkbox("Has Balcony", name="balcony"),
                        ),
                        rx.input(
                            placeholder="Capacity",
                            name="capacity",
                            type="number",
                            value=2,
                            required=True
                        ),
                        rx.button("Create Room", type="submit"),
                        spacing="4",
                        width="100%",
                    ),
                    on_submit=RoomState.create_room,
                ),
                spacing="5",
                width="100%",
            ),
            justify="center",
            align_items="center",
            min_height="85vh",
            max_width="800px",
            padding="2em",
        ),
        title="Create Room",
    )