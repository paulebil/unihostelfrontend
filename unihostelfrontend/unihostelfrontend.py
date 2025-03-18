"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


# Importing individual page components from the pages module
from .pages.index import index
from .pages.admin import admin
from .pages.booking import booking
from .pages.profile import profile
from .pages.search import search

class State(rx.State):
    """The app state."""

    ...

# Initialize the Reflex application
app = rx.App()

# Register pages with the app
app.add_page( index)
app.add_page( admin)
app.add_page(booking)
app.add_page(profile)
app.add_page(search)
