import reflex as rx

from unihostelfrontend.states.hostel_state import HostelState, Hostel

# In your cards.py file:
def image_card() -> rx.Component:
    return rx.flex(
        rx.foreach(
            HostelState.hostels,
            show_hostel
        ),
        spacing="4",
        align_items="stretch",
        justify_content="space-between",  # Spreads cards across the width
        flex_wrap="wrap",
        width="100%",
        gap="2em",
        padding="1em",
        max_width="1400px"  # Maximum width to maintain readability
    )


def show_hostel(hostel: Hostel) -> rx.Component:
    return rx.link(
        rx.card(
            rx.vstack(
                rx.inset(
                    rx.image(
                        src=hostel.image_url,
                        width="100%",
                        height="150px",
                        object_fit="cover",
                    ),
                    side="top",
                    pb="current",
                ),
                rx.vstack(
                    rx.heading(
                        hostel.name,
                        size="3",
                        color=rx.color("accent", 9),
                        margin_bottom="0.5em",
                    ),
                    rx.hstack(
                        rx.icon("map-pin"),
                        rx.text(
                            hostel.location,
                            color="gray",
                            font_size="0.9em",
                        ),
                        spacing="2",
                    ),
                    padding="0",
                    width="100%",
                    align_items="start",
                ),
                spacing="0",
                width="100%",
            ),
            size="3",
            hover_shadow="lg",
            background_color="white",
            border_radius="xl",
            width="300px",
            height="250px",
            transition="all 0.2s ease-in-out",
            _hover={
                "transform": "translateY(-5px)",
            },
        ),
        href=f"/hostel/{hostel.id}",  # Add dynamic link to hostel details page
        text_decoration="none",
    )



def render_hostel_detail(hostel: Hostel) -> rx.Component:
    return rx.container(
        rx.vstack(
            # Main card with images
            rx.card(
                rx.vstack(
                    rx.grid(
                        rx.inset(
                            rx.image(
                                src=hostel.image_url,
                                width="100%",
                                height="200px",
                                object_fit="cover",
                            ),
                            side="top",
                            pb="current",
                        ),
                        rx.inset(
                            rx.image(
                                src=hostel.image_url,
                                width="100%",
                                height="200px",
                                object_fit="cover",
                            ),
                            side="top",
                            pb="current",
                        ),
                        rx.inset(
                            rx.image(
                                src=hostel.image_url,
                                width="100%",
                                height="200px",
                                object_fit="cover",
                            ),
                            side="top",
                            pb="current",
                        ),
                        columns="3",
                        spacing="2",
                        width="100%",
                    ),
                    rx.vstack(
                        rx.heading(
                            hostel.name,
                            size="4",
                            color=rx.color("teal", 9),
                        ),
                        rx.hstack(
                            rx.icon("map-pin"),
                            rx.text(
                                hostel.location,
                                color="gray",
                                font_size="1.1em",
                            ),
                            spacing="2",
                            padding_y="2",
                        ),
                        rx.button(
                            "View Rooms",
                            on_click=lambda: HostelState.handle_view_rooms(hostel.id),
                            color_scheme="teal",
                            size="3",
                            width="100%",
                        ),
                        spacing="2",
                        align="start",
                        width="100%",
                        padding="4",
                    ),
                    width="100%",
                    spacing="0",
                ),
                size="2",
                width="800px",
                hover_shadow="lg",
                background_color="white",
                border_radius="xl",
                overflow="hidden",
                transition="all 0.2s ease-in-out",
                _hover={
                    "transform": "translateY(-5px)",
                },
            ),
            # Additional information in separate cards
            render_hostel_description(hostel),
            render_hostel_rules(hostel),
            render_hostel_contact(hostel),
            spacing="6",
            width="100%",
        ),
        max_width="1200px",
        padding="4",
        center_content=True,
    )
#
# def render_hostel_description(hostel: Hostel) -> rx.Component:
#     return rx.card(
#         rx.vstack(
#             rx.heading("Description", size="3"),
#             rx.text(
#                 hostel.description,
#                 color="gray",
#                 font_size="1.1em",
#             ),
#             spacing="4",
#             width="100%",
#             padding="4",
#         ),
#         width="800px",
#     )
#
# def render_hostel_rules(hostel: Hostel) -> rx.Component:
#     return rx.card(
#         rx.vstack(
#             rx.heading("Rules and Regulations", size="3"),
#             rx.text(
#                 hostel.rules_and_regulations,
#                 color="gray",
#                 font_size="1.1em",
#             ),
#             spacing="4",
#             width="100%",
#             padding="4",
#         ),
#         width="800px",
#     )
#
# def render_hostel_contact(hostel: Hostel) -> rx.Component:
#     return rx.card(
#         rx.vstack(
#             rx.heading("Contact Information", size="3"),
#             rx.text(
#                 f"📞 {hostel.phone}",
#                 color="gray",
#                 font_size="1.1em",
#             ),
#             rx.text(
#                 f"📧 {hostel.email_address}",
#                 color="gray",
#                 font_size="1.1em",
#             ),
#             rx.text(
#                 f"📍 {hostel.address_line}",
#                 color="gray",
#                 font_size="1.1em",
#             ),
#             spacing="4",
#             width="100%",
#             padding="4",
#         ),
#         width="800px",
#     )
#

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def render_hostel_header(hostel: Hostel) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading(
                hostel.name,
                size="4",
                color=rx.color("teal", 9)
            ),
            rx.hstack(
                rx.icon("map-pin"),
                rx.text(
                    hostel.location,
                    color="gray",
                    font_size="1.1em"
                ),
                spacing="2",
                padding_y="2"
            ),
            width="100%",
            padding="4",
            align_items="start"
        ),
        width="800px"
    )

def render_hostel_images(hostel: Hostel) -> rx.Component:
    return rx.card(
        rx.grid(
            rx.image(
                src=hostel.image_url,
                width="100%",
                height="200px",
                object_fit="cover"
            ),
            columns="3",
            spacing="2",
            width="100%"
        ),
        width="800px"
    )

def render_hostel_description(hostel: Hostel) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("Description", size="3"),
            rx.text(
                hostel.description,
                color="gray",
                font_size="1.1em"
            ),
            spacing="4",
            width="100%",
            padding="4"
        ),
        width="800px"
    )

def render_hostel_amenities(hostel: Hostel) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("Amenities", size="3"),
            rx.text(
                hostel.amenities,
                color="gray",
                font_size="1.1em",
                white_space="pre-line"
            ),
            spacing="4",
            width="100%",
            padding="4"
        ),
        width="800px"
    )

def render_hostel_rules(hostel: Hostel) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("Rules and Regulations", size="3"),
            rx.text(
                hostel.rules_and_regulations,
                color="gray",
                font_size="1.1em",
                white_space="pre-line"
            ),
            spacing="4",
            width="100%",
            padding="4"
        ),
        width="800px"
    )

def render_hostel_contact(hostel: Hostel) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("Contact Information", size="3"),
            rx.text(f"📞 {hostel.phone}", color="gray", font_size="1.1em"),
            rx.text(f"📧 {hostel.email_address}", color="gray", font_size="1.1em"),
            rx.text(f"📍 {hostel.address_line}", color="gray", font_size="1.1em"),
            spacing="4",
            width="100%",
            padding="4"
        ),
        width="800px"
    )

def render_hostel_stats(hostel: Hostel) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("Additional Information", size="3"),
            rx.text(
                f"💰 Average Price: UGX {hostel.average_price:,} per semester",
                color="gray",
                font_size="1.1em"
            ),
            rx.text(
                f"🏠 Available Rooms: {hostel.available_rooms}",
                color="gray",
                font_size="1.1em"
            ),
            spacing="4",
            width="100%",
            padding="4"
        ),
        width="800px"
    )

def render_action_card(hostel: Hostel) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.text(
                "Looking for comfortable student accommodation? View our available rooms and find your perfect space.",
                color="gray",
                font_size="1.1em",
                text_align="center"
            ),
            rx.button(
                "View Rooms",
                on_click=lambda: HostelState.handle_student_view_rooms(hostel.id),
                color_scheme="teal",
                size="3",
                width="100%"
            ),
            spacing="4",
            width="100%",
            padding="4",
            align_items="center"
        ),
        width="200px"
    )

def render_full_hostel(hostel: Hostel) -> rx.Component:
    return rx.flex(
        rx.vstack(
            render_hostel_header(hostel),
            render_hostel_images(hostel),
            render_hostel_description(hostel),
            render_hostel_amenities(hostel),
            render_hostel_rules(hostel),
            render_hostel_contact(hostel),
            render_hostel_stats(hostel),
            spacing="6",
            width="100%",
            align_items="center"
        ),
        rx.vstack(
            render_action_card(hostel),
            width="30%",
            align_items="start"
        ),

        #direction="column",
        spacing="7",
        align="stretch",
        width="100%",
        padding_left="10em",
        padding_right="10em",
        padding_bottom="10em",
        max_width="1400px"

    )