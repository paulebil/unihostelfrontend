import reflex as rx

from unihostelfrontend.states.room_state import RoomState, Room



def show_room_card(room: Room) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.image(
                src=room.image_url,
                width="100%",
                height="200px",
                object_fit="cover",
            ),
            rx.vstack(
                rx.heading(
                    f"Room {room.room_number}",
                    size="5",
                    color=rx.color("teal", 9),
                   # color="rgb(107,99,246)",
                ),
                rx.text(
                    f"💰 {room.price_per_semester} per semester",
                    color="gray",
                ),
                rx.text(
                    f"🛏️ {room.room_type} Room",
                    color="gray",
                ),
                rx.text(
                    f"👥 Capacity: {room.capacity}",
                    color="gray",
                ),
                rx.hstack(
                    rx.cond(
                        room.bathroom,
                        rx.text("🚽 Private Bathroom", color="gray"),
                        rx.text("🚽 Shared Bathroom", color="gray"),
                    ),
                    rx.cond(
                        room.balcony,
                        rx.text("🏖️ Has Balcony", color="gray"),
                        rx.text("🏖️ No Balcony", color="gray"),
                    ),
                    spacing="3",
                ),
                rx.button(
                    "Book Now",
                    color_scheme="teal",
                    width="100%",
                ),
                width="100%",
                padding="1em",
                spacing="4",
            ),
            width="100%",
            spacing="4",
        ),
        size="3",
        hover_shadow="lg",
        background_color="white",
        border_radius="xl",
        padding="0",
        width="350px",
    )

def room_list() -> rx.Component:
    return rx.container(
        rx.flex(
            rx.foreach(
                RoomState.rooms,
                show_room_card
            ),
            spacing="4",
            align_items="stretch",
            justify_content="space-between",
            flex_wrap="wrap",
            gap="2em",
            padding="1em",
            width="100%",
        ),
        max_width="1200px",
        padding="2em",
    )

def add_room_button() -> rx.Component:
    return rx.button(
        rx.hstack(
            rx.icon("plus", size=26),
            rx.text("Add Room", size="4"),
        ),
        color_scheme="teal",
        on_click=RoomState.go_to_create_room,
    )


from unihostelfrontend.states.room_state import RoomFilterState


def room_filter() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.input(
                placeholder="Search rooms...",
                on_change=RoomFilterState.set_search_value,
                width="100%",
            ),
            rx.select(
                ["Price (Low to High)", "Price (High to Low)", "Capacity", "Room Type"],
                placeholder="Sort By",
                on_change=RoomFilterState.set_sort_value,
                width="200px",
            ),
            width="100%",
            spacing="4",
        ),
        rx.hstack(
            rx.checkbox("Private Bathroom"),
            rx.checkbox("Balcony"),
            rx.checkbox("Single Room"),
            rx.checkbox("Double Room"),
            spacing="6",
        ),
        width="100%",
        spacing="4",
        padding="1em",
    )