import reflex as rx
from ..templates.template import base_template
from datetime import datetime

# Hostel Model
class Hostel(rx.Model):
    """Model representing a hostel in the database."""
    id: int
    name: str
    image_url: str | None
    description: str
    location: str
    owner_id: int
    average_price: int
    available_rooms: int
    rules_and_regulations: str | None
    amenities: str | None
    created_at: datetime
    updated_at: datetime | None




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
        with rx.session() as session:
            new_hostel = Hostel(
                name=form_data["name"],
                image_url=form_data["image_url"],
                description=form_data["description"],
                location=form_data["location"],
                average_price=int(form_data["average_price"]),
                available_rooms=int(form_data["available_rooms"]),
                rules_and_regulations=form_data["rules"],
                amenities=form_data["amenities"],
                owner_id=1  # You'll need to get this from your auth system
            )
            session.add(new_hostel)
            session.commit()

        return rx.redirect("/create/room")  # Redirect to room creation


@rx.page(route="/create/hostel", title="Create Hostel")
def create_hostel() -> rx.Component:
    """Create Hostel page."""
    return base_template(
        content=rx.flex(

            rx.vstack(
                rx.heading("Create New Hostel", size="7", margin_bottom="1em"),
                rx.card(
                    rx.form(
                        rx.vstack(
                            rx.input(
                                placeholder="Hostel Name",
                                name="name",
                                required=True,
                                width="100%",  # Make inputs full width
                            ),
                            rx.input(
                                placeholder="Image URL",
                                name="image_url",
                                width="100%",
                            ),
                            rx.text_area(
                                placeholder="Description",
                                name="description",
                                required=True,
                                width="100%",
                                min_height="100px",  # Taller text area
                            ),
                            rx.input(
                                placeholder="Location",
                                name="location",
                                required=True,
                                width="100%",
                            ),
                            rx.input(
                                placeholder="Average Price",
                                name="average_price",
                                type="number",
                                required=True,
                                width="100%",
                            ),
                            rx.input(
                                placeholder="Available Rooms",
                                name="available_rooms",
                                type="number",
                                required=True,
                                width="100%",
                            ),
                            rx.text_area(
                                placeholder="Rules and Regulations (comma separated)",
                                name="rules",
                                width="100%",
                                min_height="100px",
                            ),
                            rx.text_area(
                                placeholder="Amenities (comma separated)",
                                name="amenities",
                                width="100%",
                                min_height="100px",
                            ),
                            rx.button(
                                "Create Hostel",
                                type="submit",
                                width="100%",
                                bg="blue.500",  # Style button
                                color="white",
                                margin_top="1em",
                            ),
                            spacing="4",
                            width="100%",
                            padding="2em",
                        ),
                        on_submit=HostelState.create_hostel,
                        width="100%",
                    ),
                    width="90%",
                  # Limit form width
                    bg="white",  # Add background
                    border_radius="lg",  # Round corners
                    box_shadow="lg",  # Add shadow
                    padding="2em",
                ),
                width="100%",
                min_height="100vh",  # Full height
                spacing="4",
                padding="2em",
            ),
            width="100%",
            min_height="100vh",  # Full height
            bg="gray.50",  # Light background
            align_items="stretch",
            justify_content="space-between",  # Spreads cards across the width
            align="center",  # Add alignment to flex
            justify="center",  # Add justification to fle

        ),
        title="Create Hostel",
    )