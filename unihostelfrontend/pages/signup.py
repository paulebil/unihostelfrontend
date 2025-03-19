import reflex as rx
from ..templates.template import base_template

@rx.page(route="/signup", title="Sign Up")
def signup() -> rx.Component:
    """Signup page for new users."""
    return base_template(
        content=rx.container(
            rx.heading("Sign Up", size="7"),
            rx.input(placeholder="Full Name", width="100%"),
            rx.input(placeholder="Email", width="100%"),
            rx.input(placeholder="Password", type_="password", width="100%"),
            rx.input(placeholder="Confirm Password", type_="password", width="100%"),
            rx.button("Sign Up", bg="blue.500", color="white", margin_top="1rem"),
            rx.link("Already have an account? Login", href="/login", color="blue.500"),
            spacing="4",
            justify="center",
            min_height="85vh",
        ),
        title="Sign Up",
    )