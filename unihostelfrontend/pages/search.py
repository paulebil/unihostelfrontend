import reflex as rx
from ..templates.template import base_template

@rx.page(route="/search", title="Search Hostels")
def search() -> rx.Component:
    """Search page for finding hostels."""
    return base_template(
        content=rx.container(
            rx.image(src="/hostel.jpeg", width="100px", height="auto"),
            spacing="4",
            justify="center",
            min_height="85vh",


        ),
        title="Search Hostels",
    )