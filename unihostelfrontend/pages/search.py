import reflex as rx
from ..templates.template import base_template

@rx.page(route="/search", title="Search Hostels")
def search() -> rx.Component:
    """Search page for finding hostels."""
    return base_template(
        content=rx.container(
            rx.heading("Search Hostels", size="7"),
            rx.input(placeholder="Enter location...", width="100%"),
            rx.select(
                ["Single Room", "Shared Room", "Entire Hostel"],
                placeholder="Select Room Type",
                width="100%",
            ),
            rx.button("Search", bg="blue.500", color="white", margin_top="1rem"),
            spacing="4",
            justify="center",
            min_height="85vh",
        ),
        title="Search Hostels",
    )