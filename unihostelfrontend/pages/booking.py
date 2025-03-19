import reflex as rx
from ..templates.template import base_template

@rx.page(route="/booking", title="My Bookings")
def booking() -> rx.Component:
    """Booking page for students to view their bookings."""
    return base_template(
        content=rx.container(
            rx.heading("My Bookings", size="7"),
            rx.table_container(
                rx.table(
                    rx.thead(
                        rx.tr(
                            rx.th("Hostel Name"),
                            rx.th("Room Type"),
                            rx.th("Check-In Date"),
                            rx.th("Check-Out Date"),
                        )
                    ),
                    rx.tbody(
                        rx.tr(
                            rx.td("UniHostel A"),
                            rx.td("Single Room"),
                            rx.td("2023-11-01"),
                            rx.td("2023-12-01"),
                        ),
                        rx.tr(
                            rx.td("UniHostel B"),
                            rx.td("Shared Room"),
                            rx.td("2023-10-15"),
                            rx.td("2023-11-15"),
                        ),
                    ),
                ),
                width="100%",
            ),
            spacing="4",
            justify="center",
            min_height="85vh",
        ),
        title="My Bookings",
    )