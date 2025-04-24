import reflex as rx
from ..templates.template import admin_base_template

@rx.page(route="/profile", title="Profile")
def profile() -> rx.Component:
    """Profile page for users to manage their account."""
    return admin_base_template(
        content=rx.container(
            rx.heading("Profile", size="7"),
            rx.form(
                rx.vstack(
                    rx.input(placeholder="Full Name", width="100%"),
                    rx.input(placeholder="Email", width="100%"),
                    rx.input(placeholder="Phone Number", width="100%"),
                    rx.button("Save Changes", bg="blue.500", color="white"),
                ),
                spacing="4",
            ),
            spacing="4",
            justify="center",
            min_height="85vh",
        ),
        title="Profile",
    )