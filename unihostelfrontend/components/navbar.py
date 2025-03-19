import reflex as rx
from ..states.state import AppState  # Import the state to access user_role

def navbar():
    return rx.box(
        rx.flex(
            # Logo
            rx.link(
                rx.text("UniHostel", font_size="1.5rem", font_weight="bold"),
                href="/",
                color=rx.color("accent", 12),  # Use color mode-aware colors
            ),
            rx.spacer(),
            # Navigation Links (Role-Based)
            rx.cond(
                AppState.user_role == "student",
                rx.hstack(
                    rx.link("Search Hostels", href="/search", color=rx.color("accent", 12)),
                    rx.link("My Bookings", href="/booking", color=rx.color("accent", 12)),
                    rx.link("Profile", href="/profile", color=rx.color("accent", 12)),
                ),
                rx.cond(
                    AppState.user_role == "custodian",
                    rx.hstack(
                        rx.link("Manage Hostels", href="/admin/hostels", color=rx.color("accent", 12)),
                        rx.link("Bookings", href="/booking", color=rx.color("accent", 12)),
                        rx.link("Students", href="/admin/students", color=rx.color("accent", 12)),
                    ),
                    rx.cond(
                        AppState.user_role == "admin",
                        rx.hstack(
                            rx.link("User Management", href="/admin/users", color=rx.color("accent", 12)),
                            rx.link("Hostel Approval", href="/admin/hostels", color=rx.color("accent", 12)),
                            rx.link("Reports", href="/admin/reports", color=rx.color("accent", 12)),
                        ),
                        rx.hstack(
                            rx.link("Login", href="/login", color=rx.color("accent", 12)),
                            rx.link("Sign Up", href="/signup", color=rx.color("accent", 12)),
                        ),
                    ),
                ),
            ),
            # Color Mode Button
            # rx.color_mode_button(
            #     rx.color_mode_icon(),  # Displays a sun/moon icon for toggling
            #     bg="transparent",
            #     border="1px solid",
            #     border_color=rx.color("accent", 6),
            #     color=rx.color("accent", 12),
            #     padding="0.5rem",
            #     _hover={"bg": rx.color("accent", 3)},
            # ),

            rx.color_mode.button(position="bottom-left"),
            # Logout Button
            rx.button(
                "Logout",
                on_click=rx.redirect("/logout"),
                bg=rx.color("red", 5),  # Use color mode-aware colors
                color=rx.color("accent", 12),
                _hover={"bg": rx.color("red", 6)},
            ),
            align="center",
            justify="between",  # Use 'between' instead of 'space-between'
            padding="1rem",
        ),
        bg=rx.color("accent", 9),  # Use color mode-aware background color
        position="fixed",
        top="4rem",  # Adjusted to sit below the title bar
        width="100%",
        z_index="1000",
    )