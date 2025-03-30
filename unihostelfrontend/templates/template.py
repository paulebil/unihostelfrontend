import reflex as rx
from ..components.navbar import navbar  # Import the navbar component

def base_template(content: rx.Component, title: str = "UniHostel") -> rx.Component:
    """Base template with a navbar and page-specific content."""
    return rx.vstack(

        navbar(),  # Include the navbar below the title bar
       rx.box(
            content,  # Page-specific content
            padding_top="8rem",  # Padding to avoid overlap with the fixed navbar
            width="100%",
        ),
        rx.color_mode.button(position="bottom-left"),
        spacing="0",
        align_items="center",
        min_height="100vh",
    )