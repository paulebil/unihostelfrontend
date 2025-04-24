import reflex as rx

def show_payment() -> rx.Component:
    return rx.card(
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
                    ),
                ),
    )