import reflex as rx
from unihostelfrontend.states.image_state import ImageUploadState


class Room(rx.Base):
    """The room model."""
    id: int
    room_number: str
    price_per_semester: float
    room_type: str
    bathroom: bool
    balcony: bool
    capacity: int
    hostel_id: int
    image_url: str


class RoomCreate(rx.Base):
    """The room creation model."""
    room_number: str = ""
    price_per_semester: float = 0.0
    room_type: str = "DOUBLE"
    bathroom: bool = False
    balcony: bool = False
    capacity: int = 2
    hostel_id: int = 0
    image_url: str = ""


class RoomState(rx.State):
    """Room state for managing room operations."""

    # State vars for error handling and loading
    error: str = ""
    is_loading: bool = False

    # Sample rooms data (similar to your hostel state pattern)
    rooms: list[Room] = [
        Room(
            id=1,
            room_number="A101",
            price_per_semester=1500.0,
            room_type="DOUBLE",
            bathroom=True,
            balcony=False,
            capacity=2,
            hostel_id=1,
            image_url="/room.jpeg"
        ),
        Room(
            id=2,
            room_number="B202",
            price_per_semester=2000.0,
            room_type="SINGLE",
            bathroom=True,
            balcony=True,
            capacity=1,
            hostel_id=1,
            image_url="/room.jpeg"
        ),
        Room(
            id=3,
            room_number="C303",
            price_per_semester=1800.0,
            room_type="DOUBLE",
            bathroom=False,
            balcony=True,
            capacity=2,
            hostel_id=1,
            image_url="/room.jpeg"
        ),
        Room(
            id=4,
            room_number="D404",
            price_per_semester=2500.0,
            room_type="SINGLE",
            bathroom=True,
            balcony=True,
            capacity=1,
            hostel_id=2,
            image_url="/room.jpeg"
        ),
        Room(
            id=5,
            room_number="E505",
            price_per_semester=1600.0,
            room_type="DOUBLE",
            bathroom=False,
            balcony=False,
            capacity=2,
            hostel_id=2,
            image_url="/room.jpeg"
        ),
        Room(
            id=6,
            room_number="F606",
            price_per_semester=2200.0,
            room_type="SINGLE",
            bathroom=True,
            balcony=False,
            capacity=1,
            hostel_id=3,
            image_url="/room.jpeg"
        ),
        Room(
            id=7,
            room_number="G707",
            price_per_semester=1900.0,
            room_type="DOUBLE",
            bathroom=True,
            balcony=True,
            capacity=2,
            hostel_id=3,
            image_url="/room.jpeg"
        ),
        Room(
            id=8,
            room_number="H808",
            price_per_semester=1700.0,
            room_type="DOUBLE",
            bathroom=False,
            balcony=True,
            capacity=2,
            hostel_id=4,
            image_url="/room.jpeg"
        ),
        Room(
            id=9,
            room_number="I909",
            price_per_semester=2300.0,
            room_type="SINGLE",
            bathroom=True,
            balcony=True,
            capacity=1,
            hostel_id=4,
            image_url="/room.jpeg"
        ),
        Room(
            id=10,
            room_number="J1010",
            price_per_semester=1850.0,
            room_type="DOUBLE",
            bathroom=True,
            balcony=False,
            capacity=2,
            hostel_id=5,
            image_url="/room.jpeg"
        )
    ]

    @rx.var
    def current_hostel_id(self) -> str:  # Match the route parameter name
        return self.router.page.params.get("view_hostel_id", "")

    @rx.event
    async def create_room(self, form_data: dict):
        """Create a new room."""
        self.is_loading = True
        self.error = ""

        # try:
        #     # Get the image URL from the upload component
        #     image_url = ImageUploadState.image
        #
        #     # Add image URL and hostel_id to form data
        #     form_data["image_url"] = image_url
        #     form_data["hostel_id"] = self.get_hostel_id
        #
        #     # Here you would make your API call
        #     # api_url = "your_api_endpoint"
        #     # response = await api.post(api_url, json=form_data)
        #
        #     # For now, just redirect
        #     return rx.redirect(f"/rooms/{self.get_hostel_id}")
        #
        # except Exception as e:
        #     self.error = str(e)
        # finally:
        #     self.is_loading = False
        #

        return rx.redirect(f"/custodian/view/rooms/1")

    @rx.event
    async def view_room_details(self, room_id: int):
        """Handle view room details button click."""
        return rx.redirect(f"/room/{room_id}")

    @rx.event
    async def go_to_create_room(self):
        hostel_id = self.current_hostel_id
        print(hostel_id)
        return rx.redirect(f"/create/room/{hostel_id}")


class RoomFilterState(rx.State):
    search_value: str = ""
    show_bathroom: bool = False
    show_balcony: bool = False
    show_single: bool = False
    show_double: bool = False
    sort_by: str = ""

    @rx.event
    def set_search_value(self, value: str):
        self.search_value = value.lower()

    @rx.event
    def set_sort_value(self, value: str):
        self.sort_by = value
    @rx.event
    def toggle_bathroom(self, value: bool):
        self.show_bathroom = value

    @rx.event
    def toggle_balcony(self, value: bool):
        self.show_balcony = value

    @rx.event
    def toggle_single(self, value: bool):
        self.show_single = value

    @rx.event
    def toggle_double(self, value: bool):
        self.show_double = value

    @rx.event
    def sort_rooms(self, value: str):
        self.sort_by = value

