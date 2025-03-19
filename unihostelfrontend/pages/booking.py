import reflex as rx
from ..templates.template import base_template

@rx.page(route="/booking", title="My Bookings")
def booking() -> rx.Component:
    """Booking page for students to view their bookings."""
    return base_template(
        content=rx.container(
            rx.heading("My Bookings", size="7"),
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("Hostel Name"),
                        rx.table.column_header_cell("Room Type"),
                        rx.table.column_header_cell("Check-In Date"),
                        rx.table.column_header_cell("Check-Out Date"),
                    ),
                ),
                rx.table.body(
                    rx.table.row(
                        rx.table.cell("UniHostel A"),
                        rx.table.cell("Single Room"),
                        rx.table.cell("2023-11-01"),
                        rx.table.cell("2023-12-01"),
                    ),
                    rx.table.row(
                        rx.table.cell("UniHostel B"),
                        rx.table.cell("Shared Room"),
                        rx.table.cell("2023-10-15"),
                        rx.table.cell("2023-11-15"),
                    ),
                ),
                variant="surface",
                size="3",
                width="100%",
            ),
            spacing="4",
            justify="center",
            min_height="85vh",
        ),
        title="My Bookings",
    )