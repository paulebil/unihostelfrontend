import reflex as rx

def sidebar_item(text: str, icon: str, href: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("accent", 4),
                    "color": rx.color("accent", 11),
                },
                "border-radius": "0.5em",
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )

def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Home", "arrow-big-left", "/"),
        sidebar_item("Dashboard", "layout-dashboard", "/admin/reports"),
        sidebar_item("Hostels", "house", "/create/hostel/my-hostels"),
        sidebar_item("Bookings", "notebook-tabs", "/booking"),
        spacing="1",
        width="100%",
    )

def sidebar() -> rx.Component:
    return rx.drawer.root(
        rx.drawer.trigger(rx.icon("align-justify", size=30)),
        rx.drawer.overlay(z_index="5"),
        rx.drawer.portal(
            rx.drawer.content(
                rx.vstack(
                    rx.box(
                        rx.drawer.close(rx.icon("x", size=30)),
                        width="100%",
                    ),
                    rx.hstack(
                        rx.image(
                            src="/logo2.png",
                            width="2.25em",
                            height="auto",
                            border_radius="25%",
                        ),
                        rx.heading("UniHostel", size="7", weight="bold"),
                        align="center",
                        justify="start",
                        padding_x="0.5rem",
                        width="100%",
                    ),
                    sidebar_items(),
                    rx.spacer(),
                    rx.vstack(
                        rx.vstack(
                            sidebar_item("Profile", "user", "/profile"),
                            sidebar_item("Log out", "log-out", "/#"),
                            spacing="1",
                            width="100%",
                        ),
                        rx.divider(),
                        rx.hstack(
                            rx.icon_button(
                                rx.icon("user"),
                                size="3",
                                radius="full",
                            ),
                            rx.vstack(
                                rx.box(
                                    rx.text(
                                        "My account",
                                        size="3",
                                        weight="bold",
                                    ),
                                    rx.text(
                                        "user@unihostel.com",
                                        size="2",
                                        weight="medium",
                                    ),
                                    width="100%",
                                ),
                                spacing="0",
                                align="start",
                                justify="start",
                                width="100%",
                            ),
                            padding_x="0.5rem",
                            align="center",
                            justify="start",
                            width="100%",
                        ),
                        width="100%",
                        spacing="5",
                    ),
                    spacing="5",
                    padding_x="1em",
                    padding_y="1.5em",
                    bg=rx.color("accent", 3),
                    align="start",
                    height="650px",
                    width="16em",
                ),
                top="auto",
                right="auto",
                height="100%",
                width="20em",
                padding="1.5em",
                bg=rx.color("accent", 2),
            ),
        ),
        direction="left",
    )