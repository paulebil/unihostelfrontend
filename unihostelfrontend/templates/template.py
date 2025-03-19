import reflex as rx
from ..components.navbar import navbar  # Import the navbar component

def base_template(content: rx.Component, title: str = "UniHostel") -> rx.Component:
    """Base template with a navbar and page-specific content."""
    return rx.vstack(
        rx.box(
            rx.heading(title, size="3", color="white"),  # Use a valid size ('1' to '9')
            bg="blue.500",
            padding="1rem",
            position="fixed",
            top="0",
            width="100%",
            z_index="1000",
        ),
        navbar(),  # Include the navbar below the title bar
        rx.box(
            content,  # Page-specific content
            padding_top="8rem",  # Padding to avoid overlap with the fixed navbar
            width="100%",
        ),
        spacing="0",
        align_items="center",
        min_height="100vh",
    )