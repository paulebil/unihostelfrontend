import reflex as rx

from unihostelfrontend.states.image_state import ImageUploadState


class Hostel(rx.Base):
    """The hostel model."""
    id: int
    name: str
    location: str
    image_url: str

class HostelCreate(rx.Base):
    """The hostel state."""
    name: str = ""
    image_url: str = ""
    description: str = ""
    location: str = ""
    average_price: int = 0
    available_rooms: int = 0
    rules_and_regulations: str = ""
    amenities: str = ""


class HostelState(rx.State):


    hostels: list[Hostel] = [
        Hostel(
            id=1,
            name="IDeal Hostel",
            location="Kataza, Nakawa",
            image_url="/hostel.jpeg"
        ),
        Hostel(
            id=2,
            name="Student Lodge",
            location="Makerere, Kampala",
            image_url="/hostel.jpeg"
        ),
        Hostel(
            id=3,
            name="Campus View",
            location="Kyambogo, Banda",
            image_url="/hostel.jpeg"
        ),
        Hostel(
            id=4,
            name="Comfort Zone",
            location="Ntinda, Kampala",
            image_url="/hostel.jpeg"
        ),
        Hostel(
            id=5,
            name="Unity Hostel",
            location="Wandegeya, Central",
            image_url="/hostel.jpeg"
        ),
        Hostel(
            id=6,
            name="Scholar's Home",
            location="Bukoto, Nakawa",
            image_url="/hostel.jpeg"
        ),
    ]



    @rx.event
    async def create_hostel(self, form_data: dict):
        """Create a new hostel."""
        # Get the image URL from the upload component
        image_url = ImageUploadState.image  # Access the image URL from upload state

        # Add image URL to form data
        form_data["image_url"] = image_url

        api = ""

        # Make API call to your backend
        # try:
        #     response = await api.post("/hostels/", json=form_data)
        #     if response.status_code == 200:
        #         return rx.redirect("/create/room", is_external=True)
        #     else:
        #         return rx.window_alert("Failed to create hostel")
        # except Exception as e:
        #     return rx.window_alert(f"Error: {str(e)}")

        return rx.redirect("/create/room", is_external=False)

    @rx.event
    async def handle_create_rooms(self, hostel_id: int):
        """Handle create rooms button click."""
        return rx.redirect(f"/create/room/{hostel_id}", is_external=True)

    @rx.event
    async def handle_view_rooms(self, hostel_id: int):
        """Handle view rooms button click."""
        return rx.redirect(f"/view/rooms/{hostel_id}", is_external=True)
