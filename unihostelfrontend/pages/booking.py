import reflex as rx
from unihostelfrontend.states.room_state import Room
from unihostelfrontend.templates.template import base_template
from unihostelfrontend.states.booking_state import BookingState

from unihostelfrontend.components.booking_card import booking_form
@rx.page(route="/book/room/[room_id]", on_load=BookingState.on_load)

def book_room() -> rx.Component:
    return base_template(
        content=rx.container(
            rx.flex(
                rx.vstack(
                    rx.heading("Room Booking Application", size="7"),
                    rx.cond(
                        BookingState.selected_room != None,
                        booking_form(BookingState.selected_room),
                        rx.heading("Loading room data..."),
                    ),
                    rx.cond(
                        BookingState.error != "",
                        rx.text(
                            BookingState.error,
                            color="red",
                        ),
                    ),
                    spacing="4",
                    align_items="stretch",
                    min_height="85vh",
                ),
                max_width="800px",
                padding="2em",
                justify="center",
                spacing="4",
            ),
        ),
    )
