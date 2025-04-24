import reflex as rx
from ..templates.template import base_template

from unihostelfrontend.states.hostel_state import HostelState
from unihostelfrontend.states.auth_state  import AuthState

@rx.page(route="/login", title="Login")
def login() -> rx.Component:
    """Login page for users."""
    return base_template(
        content=rx.flex(
            rx.card(
                rx.form(  # Add form wrapper
                    rx.vstack(
                        # ... your existing layout code ...
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
                                name="email",  # Add name
                                required=True,  # Add required
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
                                name="password",  # Add name
                                min_length=8,
                                required=True,  # Add required
                                size="3",
                                width="100%",
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        rx.button(
                            "Sign in",
                            type="submit",  # Add type
                            size="3",
                            width="100%",
                        ),
                        # Show error message if any
                        rx.cond(
                            AuthState.error,
                            rx.text(
                                AuthState.error,
                                color="red",
                            ),
                        ),
                        # ... rest of your layout code ...

                        rx.center(
                            rx.text("New here?", size="3"),
                            rx.link("Sign up", href="/signup", size="3"),
                            opacity="0.8",
                            spacing="2",
                            direction="row",
                        ),
                        spacing="6",
                        width="100%",
                    ),
                    on_submit=AuthState.handle_login,
                    reset_on_submit=True,
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

