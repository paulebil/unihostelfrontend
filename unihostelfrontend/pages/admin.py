import reflex as rx
from ..templates.template import base_template

@rx.page(route="/admin/users", title="User Management")
def admin_users() -> rx.Component:
    """Admin page for managing users."""
    return base_template(
        content=rx.container(
            rx.heading("User Management", size="7"),
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("User ID"),
                        rx.table.column_header_cell("Name"),
                        rx.table.column_header_cell("Role"),
                        rx.table.column_header_cell("Status"),
                    ),
                ),
                rx.table.body(
                    rx.table.row(
                        rx.table.cell("1"),
                        rx.table.cell("John Doe"),
                        rx.table.cell("Student"),
                        rx.table.cell("Active"),
                    ),
                    rx.table.row(
                        rx.table.cell("2"),
                        rx.table.cell("Jane Smith"),
                        rx.table.cell("Custodian"),
                        rx.table.cell("Inactive"),
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
        title="User Management",
    )

@rx.page(route="/admin/hostels", title="Hostel Approval")
def admin_hostels() -> rx.Component:
    """Admin page for approving hostels."""
    return base_template(
        content=rx.container(
            rx.heading("Hostel Approval", size="7"),
            rx.text("List of pending hostel approvals."),
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("Hostel Name"),
                        rx.table.column_header_cell("Owner"),
                        rx.table.column_header_cell("Location"),
                        rx.table.column_header_cell("Approval Status"),
                    ),
                ),
                rx.table.body(
                    rx.table.row(
                        rx.table.cell("UniHostel A"),
                        rx.table.cell("John Doe"),
                        rx.table.cell("City Center"),
                        rx.table.cell("Pending"),
                    ),
                    rx.table.row(
                        rx.table.cell("UniHostel B"),
                        rx.table.cell("Jane Smith"),
                        rx.table.cell("Suburb"),
                        rx.table.cell("Approved"),
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
        title="Hostel Approval",
    )

@rx.page(route="/admin/reports", title="Reports")
def admin_reports() -> rx.Component:
    """Admin page for viewing reports."""
    return base_template(
        content=rx.container(
            rx.heading("Reports", size="7"),
            rx.text("View booking statistics and revenue insights."),
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("Metric"),
                        rx.table.column_header_cell("Value"),
                    ),
                ),
                rx.table.body(
                    rx.table.row(
                        rx.table.cell("Total Bookings"),
                        rx.table.cell("150"),
                    ),
                    rx.table.row(
                        rx.table.cell("Revenue (USD)"),
                        rx.table.cell("$30,000"),
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
        title="Reports",
    )


@rx.page(route="/admin", title="Admin Login")
def admin_login() -> rx.Component:
    return base_template(
        content=rx.flex(
            rx.card(
                rx.vstack(
                    rx.center(
                        rx.image(
                            src="/logo.jpg",
                            width="2.5em",
                            height="auto",
                            border_radius="25%",
                        ),
                        rx.heading(
                            "Sign in to your Admin Account",
                            size="6",
                            as_="h2",
                            text_align="center",
                            width="100%",
                        ),
                        direction="column",
                        spacing="5",
                        width="100%",
                    ),
                    rx.vstack(
                        rx.text(
                            "Email address",
                            size="3",
                            weight="medium",
                            text_align="left",
                            width="100%",
                        ),
                        rx.input(
                            placeholder="unihostel@gmail.com",
                            type="email",
                            size="3",
                            width="100%",
                        ),
                        justify="start",
                        spacing="2",
                        width="100%",
                    ),
                    rx.vstack(
                        rx.hstack(
                            rx.text(
                                "Password",
                                size="3",
                                weight="medium",
                            ),
                            rx.link(
                                "Forgot password?",
                                href="#",
                                size="3",
                            ),
                            justify="between",
                            width="100%",
                        ),
                        rx.input(
                            placeholder="Enter your password",
                            type="password",
                            size="3",
                            width="100%",
                        ),
                        spacing="2",
                        width="100%",
                    ),
                    rx.button("Sign in", size="3", width="100%"),
                    rx.center(
                        rx.text("New here?", size="3"),
                        rx.link("Create Hostel", href="/create", size="3"),
                        opacity="0.8",
                        spacing="2",
                        direction="row",
                    ),
                    spacing="6",
                    width="100%",
                ),
                size="4",
                max_width="28em",
                width="100%",
            ),
            title="Login",
            spacing="4",
            justify="center",
        ),

    )