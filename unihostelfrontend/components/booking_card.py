import reflex as rx

from unihostelfrontend.states.room_state import Room
from unihostelfrontend.states.booking_state import BookingState


def render_student_information_form() -> rx.Component:
    return rx.card(

        rx.vstack(
            # Student Information Section
            rx.heading("Student Information", size="4"),
            rx.text(
                "Full Name",
                size="3",
                weight="medium",
                text_align="left",
                width="100%",
            ),
            rx.input(
                placeholder="Full Name",
                required=True,
                name="student_name",
                width="100%",
            ),

            rx.text(
                "Email",
                size="3",
                weight="medium",
                text_align="left",
                width="100%",
            ),
            rx.input(
                placeholder="Email",
                type_="email",
                required=True,
                name="student_email",
                width="100%",
            ),

            rx.text(
                "Phone Number",
                size="3",
                weight="medium",
                text_align="left",
                width="100%",
            ),
            rx.input(
                placeholder="Phone Number",
                required=True,
                name="student_phone",
                width="100%",
            ),

            rx.text(
                "University Name",
                size="3",
                weight="medium",
                text_align="left",
                width="100%",
            ),
            rx.input(
                placeholder="University",
                required=True,
                name="student_university",
                width="100%",
            ),

            rx.text(
                "Course",
                size="3",
                weight="medium",
                text_align="left",
                width="100%",
            ),
            rx.input(
                placeholder="Course",
                required=True,
                name="student_course",
                width="100%",
            ),

            rx.text(
                "Year of Study",
                size="3",
                weight="medium",
                text_align="left",
                width="100%",
            ),
            rx.select(
                ["1st Year", "2nd Year", "3rd Year", "4th Year"],
                placeholder="Year of Study",
                required=True,
                name="student_study_year",
                width="100%",
            ),
            spacing="4",
            width="100%",
            padding="4"

        ),

        width="100%",
        margin_top="2em",

    )

def render_home_residence_form() -> rx.Component:
    return rx.card(

        rx.vstack(
            # Home Residence Section
            rx.heading("Home Residence Information", size="4"),

            rx.text(
                "Home Address",
                size="3",
                weight="medium",
                text_align="left",
                width="100%",
            ),
            rx.input(
                placeholder="Home Address",
                required=True,
                name="home_address",
                width="100%",
            ),

            rx.text(
                "Home District",
                size="3",
                weight="medium",
                text_align="left",
                width="100%",
            ),
            rx.input(
                placeholder="District",
                required=True,
                name="home_district",
                width="100%",
            ),

            rx.text(
                "Home Country",
                size="3",
                weight="medium",
                text_align="left",
                width="100%",
            ),
            rx.input(
                placeholder="Country",
                required=True,
                name="home_country",
                width="100%",
            ),
            spacing="4",
            width="100%",
            padding="4"

        ),
        width="100%",
        margin_top="2em",
    )

def render_nex_of_kin_form() -> rx.Component:
    return rx.card(
        rx.vstack(
            # Next of Kin Section
            rx.heading("Next of Kin Information", size="4"),

            rx.text(
                "Next of kin Name",
                size="3",
                weight="medium",
                text_align="left",
                width="100%",
            ),
            rx.input(
                placeholder="Next of Kin Name",
                required=True,
                name="next_of_kin_name",
                width="100%",
            ),

            rx.text(
                "Next of kin Phone Number",
                size="3",
                weight="medium",
                text_align="left",
                width="100%",
            ),
            rx.input(
                placeholder="Next of Kin Phone",
                required=True,
                name="next_of_kin_phone",
                width="100%",
            ),

            rx.text(
                "Next of kin Relationship",
                size="3",
                weight="medium",
                text_align="left",
                width="100%",
            ),
            rx.select(
                ["Parent", "Guardian", "Sibling", "Spouse", "Other"],
                placeholder="Relationship with Next of Kin",
                required=True,
                name="kin_relationship",
                width="100%",
            ),

            spacing="4",
            width="100%",
            padding="4"
        ),
        width="100%",
        margin_top="2em",
        margin_bottom="2em",

    )

def render_rooms_detail_card(room: Room) -> rx.Component:
    # Room detals card
    return rx.card(
            rx.vstack(
                rx.image(
                    src=room.image_url,
                    width="100%",
                    height="200px",
                    object_fit="cover",
                ),
                rx.vstack(
                    rx.heading("Room Details", size="4"),
                    rx.divider(),
                    rx.text(f"💰 Price per semester: {room.price_per_semester}"),
                    rx.text(f"🛏️ Room Type: {room.room_type}"),
                    rx.text(f"👥 Capacity: {room.capacity}"),
                    rx.hstack(
                        rx.cond(
                            room.bathroom,
                            rx.text("🚽 Private Bathroom"),
                            rx.text("🚽 Shared Bathroom"),
                        ),
                        rx.cond(
                            room.balcony,
                            rx.text("🏖️ Has Balcony"),
                            rx.text("🏖️ No Balcony"),
                        ),
                        spacing="3",
                    ),
                    padding="1em",
                    spacing="4",
                    width="100%",
                ),
            ),
            width="800px",
            margin_bottom="2em",
    )


def booking_form(room: Room) -> rx.Component:
    return rx.vstack(
        rx.heading(
            f"Book Room {room.room_number}",
            size="5",
            color=rx.color("teal", 9),
        ),

        # Booking Form
        rx.form(
            render_rooms_detail_card(room),
            render_student_information_form(),
            render_home_residence_form(),
            render_nex_of_kin_form(),

            # Submit Button
            rx.button(
                "Submit Booking Request",
                type_="submit",
                width="100%",
                color_scheme="teal",
                is_loading=BookingState.is_loading,
            ),
            spacing="6",
            on_submit=BookingState.create_booking,

        ),
        rx.cond(
            BookingState.error != "",
            rx.text(
                BookingState.error,
                color="red",
            ),
        ),
        spacing="8",
        width="100%",
        padding="2em",
        padding_left="10em",
    )
