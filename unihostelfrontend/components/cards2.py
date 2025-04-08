import reflex as rx
import httpx
from typing import Optional


class Hostel(rx.Base):
    """The hostel model."""
    name: str
    location: str
    image_url: str


class State(rx.State):
    """The app state."""
    hostels: list[Hostel] = []
    is_loading: bool = False
    error: Optional[str] = None
    use_dummy_data: bool = True  # Toggle between dummy data and API

    # Dummy data
    dummy_hostels = [
        Hostel(name="IDeal Hostel", location="Kataza, Nakawa", image_url="/hostel.jpeg"),
        Hostel(name="Student Lodge", location="Makerere, Kampala", image_url="/hostel.jpeg"),
        Hostel(name="Campus View", location="Kyambogo, Banda", image_url="/hostel.jpeg"),
        Hostel(name="Comfort Zone", location="Ntinda, Kampala", image_url="/hostel.jpeg"),
        Hostel(name="Unity Hostel", location="Wandegeya, Central", image_url="/hostel.jpeg"),
        Hostel(name="Scholar's Home", location="Bukoto, Nakawa", image_url="/hostel.jpeg"),
        Hostel(name="Peace House", location="Kisaasi, Nakawa", image_url="/hostel.jpeg"),
        Hostel(name="Green View", location="Kamwokya, Central", image_url="/hostel.jpeg"),
    ]

    async def get_hostels(self):
        """Fetch hostels from API or use dummy data."""
        self.is_loading = True
        self.error = None

        if self.use_dummy_data:
            # Use dummy data with artificial delay
            # Simulate API delay
            self.hostels = self.dummy_hostels
            self.is_loading = False
            return

        # Real API call
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get("https://your-api-endpoint/hostels")
                response.raise_for_status()

                hostel_data = response.json()
                self.hostels = [
                    Hostel(
                        name=h.get("name", ""),
                        location=h.get("location", ""),
                        image_url=h.get("image_url", "/default-hostel.jpg")
                    )
                    for h in hostel_data
                ]

        except httpx.RequestError as e:
            self.error = f"Network error: {str(e)}"
        except httpx.HTTPStatusError as e:
            self.error = f"API error: {str(e)}"
        except Exception as e:
            self.error = f"Unexpected error: {str(e)}"

        finally:
            self.is_loading = False


def show_hostel(hostel: Hostel) -> rx.Component:
    return rx.link(
        rx.card(
            rx.vstack(
                rx.image(
                    src=hostel.image_url,
                    width="250px",
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


def image_card() -> rx.Component:
    return rx.cond(
        State.is_loading,
        rx.center(
            rx.spinner(size="3"),
            padding="5em",
        ),
        rx.cond(
            State.error,
            rx.center(
                rx.text(
                    State.error,
                    color="red",
                ),
                padding="5em",
            ),
            rx.flex(
                rx.foreach(
                    State.hostels,
                    show_hostel
                ),
                spacing="4",
                align_items="stretch",
                justify_content="space-between",
                flex_wrap="wrap",
                width="100%",
                gap="2em",
                padding="1em",
                max_width="1400px",
            ),
        ),
    )


