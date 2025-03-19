import reflex as rx
from ..templates.template import base_template

@rx.page(route="/admin/users", title="User Management")
def admin_users() -> rx.Component:
    """Admin page for managing users."""
    return base_template(
        content=rx.container(
            rx.heading("User Management", size="7"),
            rx.box(  # Replaced rx.table_container with rx.box
                rx.table(
                    rx.thead(
                        rx.tr(
                            rx.th("User ID"),
                            rx.th("Name"),
                            rx.th("Role"),
                            rx.th("Status"),
                        )
                    ),
                    rx.tbody(
                        rx.tr(
                            rx.td("1"),
                            rx.td("John Doe"),
                            rx.td("Student"),
                            rx.td("Active"),
                        ),
                        rx.tr(
                            rx.td("2"),
                            rx.td("Jane Smith"),
                            rx.td("Custodian"),
                            rx.td("Inactive"),
                        ),
                    ),
                ),
                width="100%",  # Ensure the box spans the full width
                border="1px solid #e2e8f0",  # Optional: Add a border for better visibility
                padding="1rem",  # Optional: Add padding for spacing
                overflow_x="auto",  # Enable horizontal scrolling for small screens
            ),
            spacing="4",
            justify="center",
            min_height="85vh",
        ),
        title="User Management",
    )

@rx.page(route="/admin/hostels", title="Hostel Approval")
def admin_hostels() -> rx.Component:
    """Admin page for approving hostels."""
    return base_template(
        content=rx.container(
            rx.heading("Hostel Approval", size="7"),
            rx.box(  # Use a box to group content for better layout control
                rx.text("List of pending hostel approvals."),
                rx.table(
                    rx.thead(
                        rx.tr(
                            rx.th("Hostel Name"),
                            rx.th("Owner"),
                            rx.th("Location"),
                            rx.th("Approval Status"),
                        )
                    ),
                    rx.tbody(
                        rx.tr(
                            rx.td("UniHostel A"),
                            rx.td("John Doe"),
                            rx.td("City Center"),
                            rx.td("Pending"),
                        ),
                        rx.tr(
                            rx.td("UniHostel B"),
                            rx.td("Jane Smith"),
                            rx.td("Suburb"),
                            rx.td("Approved"),
                        ),
                    ),
                ),
                width="100%",
                border="1px solid #e2e8f0",
                padding="1rem",
                overflow_x="auto",
            ),
            spacing="4",
            justify="center",
            min_height="85vh",
        ),
        title="Hostel Approval",
    )

@rx.page(route="/admin/reports", title="Reports")
def admin_reports() -> rx.Component:
    """Admin page for viewing reports."""
    return base_template(
        content=rx.container(
            rx.heading("Reports", size="7"),
            rx.box(  # Use a box to group content for better layout control
                rx.text("View booking statistics and revenue insights."),
                rx.table(
                    rx.thead(
                        rx.tr(
                            rx.th("Metric"),
                            rx.th("Value"),
                        )
                    ),
                    rx.tbody(
                        rx.tr(
                            rx.td("Total Bookings"),
                            rx.td("150"),
                        ),
                        rx.tr(
                            rx.td("Revenue (USD)"),
                            rx.td("$30,000"),
                        ),
                    ),
                ),
                width="100%",
                border="1px solid #e2e8f0",
                padding="1rem",
                overflow_x="auto",
            ),
            spacing="4",
            justify="center",
            min_height="85vh",
        ),
        title="Reports",
    )