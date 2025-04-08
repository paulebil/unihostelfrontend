import reflex as rx
from ..templates.template import base_template
from unihostelfrontend.components.cards import image_card

@rx.page(route="/", title="Home Page")
def index() -> rx.Component:
    """Home page for the app."""
    return base_template(
        content=rx.container(
            rx.vstack(
                rx.heading("Welcome to UniHostel", size="9"),
                rx.input(
                    rx.input.slot(rx.icon("search")),
                    placeholder="Search hostel by location or university or name ...",
                    type="search",
                    size="3",
                    width="100%"
                ),
                rx.box(
                    rx.hstack(
                        rx.heading("Top Searches", size="5", weight="bold")
                    ),
                    align_items="center",
                    bg=rx.color("accent", 3),
                    padding="1em",
                    width="100%",
                ),
                image_card(),
                spacing="5",
                width="100%",
                align="center",
            ),
            min_height="85vh",
            width="100%",
            size="4"  # Increased container size for wider content
        ),
        title="Home Page",
    )

