import reflex as rx
from ..templates.template import base_template

@rx.page(route="/signup", title="Sign Up")
def signup() -> rx.Component:
    """Signup page for new users."""
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
                            "Sign up to an account",
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
                    rx.vstack(
                        rx.hstack(
                            rx.text(
                                "Password",
                                size="3",
                                weight="medium",
                            ),
                            justify="between",
                            width="100%",
                        ),
                        rx.input(
                            placeholder="Confirm your password",
                            type="password",
                            size="3",
                            width="100%",
                        ),
                        spacing="2",
                        width="100%",
                    ),
                    rx.button("Sign up", size="3", width="100%"),
                    rx.center(
                        rx.text("Thank you For Signing Up with Us", size="3"),
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
       # title="Sign Up",