import reflex as rx

from unihostelfrontend.states.hostel_state import HostelState, Hostel


def show_hostel(hostel: Hostel) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.grid(
                rx.inset(
                    rx.image(
                        src=hostel.image_url,
                        width="100%",
                        height="200px",
                        object_fit="cover",
                    ),
                    side="top",
                    pb="current",
                ),
                rx.inset(
                    rx.image(
                        src=hostel.image_url,
                        width="100%",
                        height="200px",
                        object_fit="cover",
                    ),
                    side="top",
                    pb="current",
                ),
                rx.inset(
                    rx.image(
                        src=hostel.image_url,
                        width="100%",
                        height="200px",
                        object_fit="cover",
                    ),
                    side="top",
                    pb="current",
                ),
                columns="3",
                spacing="2",
                width="100%",
            ),
            rx.vstack(
                # Rest of your card content remains the same
                rx.heading(
                    hostel.name,
                    size="5",
                    color="rgb(107,99,246)",
                ),
                rx.text(
                    f"📍 {hostel.location}",
                    color="gray",
                    margin_bottom="1em",
                ),
                rx.hstack(
                    rx.button(
                        "Create Rooms",
                        size="3",
                        color_scheme="indigo",
                        width="50%",
                        on_click=lambda: HostelState.handle_create_rooms(hostel.id),
                    ),
                    rx.button(
                        "View Rooms",
                        size="3",
                        variant="outline",
                        width="50%",
                        on_click=lambda: HostelState.handle_view_rooms(hostel.id),
                    ),
                    width="100%",
                    spacing="4",
                ),
                width="100%",
                padding="1em",
                spacing="2",
            ),
            width="100%",
            spacing="0",
        ),
        size="3",
        hover_shadow="lg",
        background_color="white",
        border_radius="xl",
        padding="0",
        width="100%",
    )
def image_card() -> rx.Component:
    return rx.flex(
        rx.foreach(
            HostelState.hostels,
            show_hostel
        ),
        direction="column", # Change to column direction [(1)](https://reflex.dev/docs/library/layout/flex)
        spacing="4",
        align="stretch", # Align items to stretch in the column [(1)](https://reflex.dev/docs/library/layout/flex)
        width="100%",
        padding="1em",
        max_width="1400px"
    )