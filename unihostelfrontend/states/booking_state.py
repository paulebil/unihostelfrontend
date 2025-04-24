import reflex as rx

from unihostelfrontend.states.room_state import Room, RoomState

# First create a booking state with hostel information
class BookingState(rx.State):
    """Booking state for managing room bookings."""
    error: str = ""
    is_loading: bool = False

    selected_room: Room = None


    # Sample hostel data (you should replace this with your actual hostel data)
    hostels: dict[int, str] = {
        1: "Hostel A",
        2: "Hostel B",
        3: "Hostel C",
        4: "Hostel D",
        5: "Hostel E"
    }

    @rx.var
    def current_room_id(self) -> str:
        return self.router.page.params.get("room_id", "")

    @rx.var
    def hostel_name(self) -> str:
        # Get hostel name based on room's hostel_id
        # In real app, you'd fetch this from your backend
        room_hostel_id = 1  # Replace with actual room's hostel_id
        return self.hostels.get(room_hostel_id, "Unknown Hostel")

    @rx.event
    async def create_booking(self, form_data: dict):
        """Create a new booking."""
        self.is_loading = True
        self.error = ""

        try:
            # Here you would make your API call to create booking
            #return rx.redirect(f"/student/view/rooms/{self.current_room_id}")
            return rx.redirect(f"/payment/make")
        except Exception as e:
            self.error = str(e)
        finally:
            self.is_loading = False


    @rx.event
    async def on_load(self):
        """Load room data when the page loads."""
        try:
            room_state = await self.get_state(RoomState)
            room_id = int(self.current_room_id)

            # Find the room in the rooms list
            self.selected_room = next(
                (room for room in room_state.rooms if room.id == room_id),
                None
            )
            if not self.selected_room:
                self.error = "Room not found"
        except Exception as e:
            self.error = str(e)
