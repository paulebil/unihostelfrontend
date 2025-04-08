import reflex as rx

from unihostelfrontend.states.hostel_state import HostelState, Hostel

# In your cards.py file:
def image_card() -> rx.Component:
    return rx.flex(
        rx.foreach(
            HostelState.hostels,
            show_hostel
        ),
        spacing="4",
        align_items="stretch",
        justify_content="space-between",  # Spreads cards across the width
        flex_wrap="wrap",
        width="100%",
        gap="2em",
        padding="1em",
        max_width="1400px"  # Maximum width to maintain readability
    )


def show_hostel(hostel: Hostel) -> rx.Component:
    return rx.link(
        rx.card(
            rx.vstack(
                rx.inset(
                    rx.image(
                        src=hostel.image_url,
                        width="100%",
                        height="150px",
                        object_fit="cover",
                    ),
                    side="top",
                    pb="current",
                ),
                rx.vstack(
                    rx.heading(
                        hostel.name,
                        size="3",
                        color=rx.color("accent", 9),
                        margin_bottom="0.5em",
                    ),
                    rx.hstack(
                        rx.icon("map-pin"),
                        rx.text(
                            hostel.location,
                            color="gray",
                            font_size="0.9em",
                        ),
                        spacing="2",
                    ),
                    padding="0",
                    width="100%",
                    align_items="start",
                ),
                spacing="0",
                width="100%",
            ),
            size="3",
            hover_shadow="lg",
            background_color="white",
            border_radius="xl",
            width="300px",
            height="250px",
            transition="all 0.2s ease-in-out",
            _hover={
                "transform": "translateY(-5px)",
            },
        ),
        href=f"/hostel/{hostel.id}",  # Add dynamic link to hostel details page
        text_decoration="none",
    )