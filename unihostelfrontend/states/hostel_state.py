import reflex as rx

from unihostelfrontend.states.image_state import ImageUploadState


class Hostel(rx.Base):
    """The hostel model."""
    id: int
    name: str
    location: str
    image_url: str
    description: str
    average_price: int
    available_rooms: int
    rules_and_regulations: str  # Changed from rules to rules_and_regulations
    amenities: str
    phone:str
    email_address:str
    address_line: str

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
            image_url="/hostel.jpeg",
            description="A modern student accommodation facility offering comfortable living spaces with state-of-the-art amenities. Located in a prime location with easy access to campus and local amenities.",
            average_price=1500000,
            available_rooms=15,
            rules_and_regulations="""• Quiet hours from 10 PM to 6 AM
    • No overnight guests without prior approval 
    • Keep common areas clean
    • No smoking inside the building
    • Regular room inspections
    • Payment due by the 5th of each month""",
            amenities="""• High-speed WiFi
    • 24/7 Security
    • Study rooms
    • Laundry facilities
    • Common room with TV
    • Backup power supply
    • Water storage tanks""",
            phone="+254-760-852-959",
            email_address="user@example.com",
            address_line="here@hotmail"
        ),
        Hostel(
            id=2,
            name="Student Lodge",
            location="Makerere, Kampala",
            image_url="/hostel.jpeg",
            description="Premium student housing in the heart of Makerere. Modern facilities and a vibrant community atmosphere make this an ideal choice for students.",
            average_price=1200000,
            available_rooms=20,
            phone="+254-760-852-959",
            email_address="user@example.com",
            address_line="here@hotmail",

    rules_and_regulations="""• Quiet hours from 11 PM to 6 AM
    • Visitors must leave by 10 PM
    • No cooking in rooms
    • Weekly room cleaning required
    • No pets allowed
    • Semester payment plan available""",
            amenities="""• Free WiFi
    • CCTV Security
    • Reading room
    • Shared kitchen
    • Games room
    • Standby generator
    • Water supply""",
        ),
        Hostel(
            id=3,
            name="Campus View",
            location="Kyambogo, Banda",
            image_url="/hostel.jpeg",
            description="Affordable student accommodation with a fantastic view of the campus. Clean, comfortable rooms with all essential amenities provided.",
            average_price=900000,
            available_rooms=25,
            phone="+254-760-852-959",
            email_address="user@example.com",
            address_line="here@hotmail",
            rules_and_regulations="""• Study hours 7 PM to 10 PM
    • No loud music
    • Keep rooms tidy
    • Monthly inspections
    • No alterations to rooms
    • Security deposit required""",
            amenities="""• Internet access
    • Security guards
    • Study tables
    • Washing area
    • TV room
    • Solar backup
    • Water reservoir"""
        ),
        Hostel(
            id=4,
            name="Comfort Zone",
            location="Ntinda, Kampala",
            image_url="/hostel.jpeg",
            description="Your home away from home. Spacious rooms and modern facilities ensure a comfortable stay for all students.",
            average_price=1300000,
            available_rooms=18,
            phone="+254-760-852-959",
            email_address="user@example.com",
            address_line="here@hotmail",
            rules_and_regulations="""• Curfew at midnight
    • Guest registration required
    • Regular cleaning checks
    • No loud gatherings
    • Maintenance requests within 24h
    • Advance payment required""",
            amenities="""• Broadband internet
    • 24/7 security
    • Private study areas
    • Laundry service
    • Recreation room
    • Power backup
    • Clean water supply"""
        ),
        Hostel(
            id=5,
            name="Unity Hostel",
            location="Wandegeya, Central",
            image_url="/hostel.jpeg",
            description="A community-focused student residence offering both comfort and convenience. Close to major universities and shopping centers.",
            average_price=1100000,
            available_rooms=30,
            phone="+254-760-852-959",
            email_address="user@example.com",
            address_line="here@hotmail",
            rules_and_regulations="""• Quiet time after 10 PM
    • Visitor hours 8 AM - 8 PM
    • Weekly room cleaning
    • No cooking appliances
    • Security protocols
    • Monthly payment option""",
            amenities="""• WiFi included
    • Security system
    • Study hall
    • Washing machines
    • Social room
    • Generator backup
    • Water tanks"""
        ),
        Hostel(
            id=6,
            name="Scholar's Home",
            location="Bukoto, Nakawa",
            image_url="/hostel.jpeg",
            description="Premium student accommodation designed for academic excellence. Quiet environment with all necessary facilities.",
            average_price=1400000,
            available_rooms=22,
            phone="+254-760-852-959",
            email_address="user@example.com",
            address_line="here@hotmail",
            rules_and_regulations="""• Study priority hours
    • Controlled access
    • Cleanliness standards
    • Room personalization allowed
    • Regular maintenance
    • Flexible payment plans""",
            amenities="""• Fast internet
    • Guard service
    • Library room
    • Cleaning service
    • Entertainment area
    • Power solution
    • Water system"""
        ),
    ]
    current_hostel: Hostel = None
    hostels: list[Hostel]

    @rx.event
    def get_hostel(self, hostel_id: str):
        """Get hostel by ID."""
        try:
            id_num = int(hostel_id)
            for hostel in self.hostels:
                if hostel.id == id_num:
                    self.current_hostel = hostel
                    break
        except ValueError:
            # Handle invalid ID
            pass

    @rx.event
    async def on_load(self):
        """Load hostel details when page loads."""
        # Get the hostel_id from router params
        hostel_id = self.router.page.params.get("hostel_id", "")
        try:
            id_num = int(hostel_id)
            for hostel in self.hostels:
                if hostel.id == id_num:
                    self.current_hostel = hostel
                    break
        except ValueError:
            # Handle invalid ID
            pass



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

        return rx.redirect("/custodian/view/rooms/[room_hostel_id]", is_external=False)

    @rx.event
    async def handle_create_rooms(self, hostel_id: int):
        """Handle create rooms button click."""
        return rx.redirect(f"/create/room/{hostel_id}", is_external=False)

    @rx.event
    async def handle_view_rooms(self, hostel_id: int):
        """Handle view rooms button click."""
        return rx.redirect(f"/custodian/view/rooms/{hostel_id}", is_external=False)

    @rx.event
    async def handle_student_view_rooms(self, hostel_id: int):
        return rx.redirect(f"/student/view/rooms/{hostel_id}", is_external=False)

    @rx.event
    async def go_to_create_hostel(self):

        return rx.redirect(f"/create/hostel/")

