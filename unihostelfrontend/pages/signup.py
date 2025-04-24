import reflex as rx
from ..templates.template import base_template
from unihostelfrontend.states.auth_state import AuthState

@rx.page(route="/signup", title="Sign Up")
def signup() -> rx.Component:
    """Signup page for new users."""
    return base_template(
        content=rx.flex(
            rx.card(
                rx.form(  # Add form wrapper
                    rx.vstack(
                        rx.center(
                            rx.image(
                                src="/logo2.png",
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
                                "Full Name",
                                size="3",
                                weight="medium",
                                text_align="left",
                                width="100%",
                            ),
                            rx.input(
                                placeholder="John Doe",
                                name="full_name",
                                required=True,
                                size="3",
                                width="100%",
                            ),
                            justify="start",
                            spacing="2",
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
                                name="email",
                                required=True,
                                size="3",
                                width="100%",
                            ),
                            justify="start",
                            spacing="2",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.text(
                                "Password",
                                size="3",
                                weight="medium",
                            ),
                            rx.input(
                                placeholder="Enter your password",
                                type="password",
                                name="password",
                                min_length=8,
                                required=True,
                                size="3",
                                width="100%",
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.text(
                                "Confirm Password",
                                size="3",
                                weight="medium",
                            ),
                            rx.input(
                                placeholder="Confirm your password",
                                type="password",
                                name="confirm_password",
                                min_length=8,
                                required=True,
                                size="3",
                                width="100%",
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        # Show error message if any
                        rx.cond(
                            AuthState.signup_error,
                            rx.text(
                                AuthState.signup_error,
                                color="red",
                            ),
                        ),
                        rx.button(
                            "Sign up",
                            type="submit",
                            size="3",
                            width="100%",
                        ),
                        rx.center(
                            rx.text("Already have an account?", size="3"),
                            rx.link("Login", href="/login", size="3"),
                            opacity="0.8",
                            spacing="2",
                            direction="row",
                        ),
                        spacing="6",
                        width="100%",
                    ),
                    on_submit=AuthState.handle_signup,
                    reset_on_submit=True,
                ),
                size="4",
                max_width="28em",
                width="100%",
            ),
            title="Sign Up",
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