import reflex as rx

class Hostel(rx.Base):
    """The hostel model."""
    name: str
    location: str
    image_url: str

class State(rx.State):
    # Initialize with default values
    hostels: list[Hostel] = [
        Hostel(
            name="IDeal Hostel",
            location="Kataza, Nakawa",
            image_url="/hostel.jpeg"
        ),
        Hostel(
            name="Student Lodge",
            location="Makerere, Kampala",
            image_url="/hostel.jpeg"
        ),
        Hostel(
            name="Campus View",
            location="Kyambogo, Banda",
            image_url="/hostel.jpeg"
        ),
        Hostel(
            name="Comfort Zone",
            location="Ntinda, Kampala",
            image_url="/hostel.jpeg"
        ),
        Hostel(
            name="Unity Hostel",
            location="Wandegeya, Central",
            image_url="/hostel.jpeg"
        ),
        Hostel(
            name="Scholar's Home",
            location="Bukoto, Nakawa",
            image_url="/hostel.jpeg"
        ),
    ]
# In your cards.py file:
def image_card() -> rx.Component:
    return rx.flex(
        rx.foreach(
            State.hostels,
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
                rx.image(
                    src=hostel.image_url,
                    width="250px",  # Slightly smaller to fit more cards
                    height="200px",
                    border_radius="15px",
                    object_fit="cover",
                ),
                rx.box(
                    rx.heading(hostel.name, size="5"),
                    rx.text(f"Location: {hostel.location}", color="gray"),
                    padding="2",
                ),
                spacing="2",
                align_items="start",
                width="100%",
            ),
            size="3",
            hover_shadow="5",
            background_color="var(--gray-1)",
        )
    )