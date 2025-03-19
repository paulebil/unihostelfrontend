import reflex as rx
from ..templates.template import base_template

@rx.page(route="/login", title="Login")
def login() -> rx.Component:
    """Login page for users."""
    return base_template(
        content=rx.container(
            rx.heading("Login", size="7"),
            rx.input(placeholder="Email", width="100%"),
            rx.input(placeholder="Password", type_="password", width="100%"),
            rx.button("Login", bg="blue.500", color="white", margin_top="1rem"),
            rx.link("Don't have an account? Sign Up", href="/signup", color="blue.500"),
            spacing="4",
            justify="center",
            min_height="85vh",
        ),
        title="Login",
    )