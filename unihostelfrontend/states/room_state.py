import reflex as rx


class Room(rx.Base):
    room_number: str = ""
    price_per_semester: float = 0.0
    room_type: str = "DOUBLE"
    bathroom: bool = False
    balcony: bool = False
    capacity: int
    hostel_id: int = 0


class RoomState(rx.State):
    """Room state for managing room creation."""
    # Add state vars for error handling and loading
    error: str = ""
    is_loading: bool = False

    @rx.var
    def get_hostel_id(self) -> str:
        return self.router.page.params.get("hostel_id", "")

    @rx.event
    async def create_room(self, form_data: dict):
        """Create a new room."""
        self.is_loading = True
        self.error = ""

        try:
            hostel_id = self.get_hostel_id
            # Process form data and make API call

            # On success
            return rx.redirect(f"/hostel/{hostel_id}")

        except Exception as e:
            self.error = str(e)
        finally:
            self.is_loading = False