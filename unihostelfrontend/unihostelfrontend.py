"""
UniHostel Frontend Application

This is the main entry point for the Reflex-based UniHostel web application.
"""

import reflex as rx

# Importing individual page components from the pages module
from .pages.index import index
from .pages.admin import admin_users, admin_hostels, admin_reports  # Import admin-specific pages
from .pages.booking import book_room
from .pages.profile import profile
from .pages.search import search
from .pages.login import login
from .pages.signup import signup
from .pages.createhostel import create_hostel, my_hostel
from .pages.rooms import create_room

# Import the global state (AppState) from the states module
from .states.state import AppState  # Global state for the app

# Initialize the Reflex application
app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="large",
        accent_color="teal",
    )
)

# Register pages with the app
app.add_page(index, route="/", title="Home Page")  # Home page
app.add_page(login, route="/login", title="Login")  # Login page
app.add_page(signup, route="/signup", title="Sign Up")  # Signup page
app.add_page(search, route="/search", title="Search Hostels")  # Search page
app.add_page(book_room, route="/book/room/[room_id]", title="My Bookings")  # Booking page
app.add_page(profile, route="/profile", title="Profile")  # Profile page

# Admin pages
app.add_page(admin_users, route="/admin/users", title="User Management")
app.add_page(admin_hostels, route="/admin/hostels", title="Hostel Approval")
app.add_page(admin_reports, route="/admin/reports", title="Reports")

# Custodian pages
app.add_page(create_hostel, route="/create", title="Create Hostel")
app.add_page(my_hostel, route="/create/hostel/my-hostels", title="My Hostels")
app.add_page(create_room, route="/create/room[room_hostel_id]", title="Create Room")

# student pages

