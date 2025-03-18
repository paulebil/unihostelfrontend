import reflex as rx
from ..components.navbar import navbar


def layout(content: rx.Component) -> rx.Component:
    """Layout component that includes the navbar."""

    return rx.vstack(
        navbar(),  # Add the navbar at the top
        content,  # The content of the page will go here
    )
