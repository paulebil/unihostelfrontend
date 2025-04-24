import reflex as rx
from ..states.state import AppState
from unihostelfrontend.components.side_bar import sidebar

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "UniHostel", size="7", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.match(
                    AppState.user_role,
                    ("student",
                     rx.hstack(
                         navbar_link("Home", "/"),
                         # navbar_link("Search", "/search"),
                         # navbar_link("Profile", "/profile"),
                         navbar_link("Login", "/login"),
                         # navbar_link("Admin", "/admin"),
                         justify="end",
                         spacing="5",
                     ),
                     ),
                    ("custodian",
                     rx.hstack(
                         navbar_link("Home", "/"),
                         navbar_link("Search", "/search"),
                         navbar_link("Profile", "/profile"),
                         navbar_link("Login", "/login"),
                         navbar_link("Admin", "/admin"),
                         justify="end",
                         spacing="5",
                     ),
                     ),
                    ("admin",
                     rx.hstack(
                         navbar_link("Home", "/"),
                         navbar_link("ManageUsers", "/admin/users"),
                         navbar_link("ManageHostels", "/admin/hostels"),
                         navbar_link("Report", "/admin/reports"),
                         navbar_link("Login", "/login"),
                         justify="end",
                         spacing="5",
                     ),
                     ),
                    rx.hstack(
                        navbar_link("Home", "/#"),
                        navbar_link("About", "/#"),
                        navbar_link("Pricing", "/#"),
                        navbar_link("Contact", "/#"),
                        justify="end",
                        spacing="5",
                    ),

                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("About"),
                        rx.menu.item("Pricing"),
                        rx.menu.item("Contact"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )

def admin_navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "UniHostel", size="7", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.match(
                    AppState.user_role,
                    ("student",
                     rx.hstack(
                         #navbar_link("Home", "/"),
                         # navbar_link("Search", "/search"),
                         # navbar_link("Profile", "/profile"),
                         #navbar_link("Login", "/login"),
                         # navbar_link("Admin", "/admin"),
                         sidebar(),
                         justify="end",
                         spacing="5",
                     ),
                     ),
                    ("custodian",
                     rx.hstack(
                         navbar_link("Home", "/"),
                         navbar_link("Search", "/search"),
                         navbar_link("Profile", "/profile"),
                         navbar_link("Login", "/login"),
                         navbar_link("Admin", "/admin"),
                         justify="end",
                         spacing="5",
                     ),
                     ),
                    ("admin",
                     rx.hstack(
                         navbar_link("Home", "/"),
                         navbar_link("ManageUsers", "/admin/users"),
                         navbar_link("ManageHostels", "/admin/hostels"),
                         navbar_link("Report", "/admin/reports"),
                         navbar_link("Login", "/login"),
                         justify="end",
                         spacing="5",
                     ),
                     ),
                    rx.hstack(
                        navbar_link("Home", "/#"),
                        navbar_link("About", "/#"),
                        navbar_link("Pricing", "/#"),
                        navbar_link("Contact", "/#"),
                        justify="end",
                        spacing="5",
                    ),

                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("About"),
                        rx.menu.item("Pricing"),
                        rx.menu.item("Contact"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )