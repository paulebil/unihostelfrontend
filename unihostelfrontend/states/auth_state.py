import reflex as rx

class AuthState(rx.State):
    """The authentication state."""
    # Login state vars
    email: str = ""
    password: str = ""
    error: str = ""

    # Signup state vars
    confirm_password: str = ""
    full_name: str = ""
    signup_error: str = ""

    def check_passwords_match(self) -> bool:
        """Check if passwords match."""
        return self.password == self.confirm_password

    @rx.var
    def passwords_match(self) -> bool:
        """Check if passwords match for real-time validation."""
        return self.check_passwords_match()

    @rx.event
    async def handle_login(self, form_data: dict):
        """Handle login form submission."""
        self.email = form_data["email"]
        self.password = form_data["password"]

        # Add your API authentication logic here
        # try:
        #     response = await api.post("/login", json={
        #         "email": self.email,
        #         "password": self.password
        #     })
        #     if response.status_code == 200:
        #         return rx.redirect("/dashboard")
        #     else:
        #         self.error = "Invalid credentials"
        # except Exception as e:
        #     self.error = "Login failed"

        # For demo, just redirect
        return rx.redirect("/create/hostel/my-hostels")

    @rx.event
    async def handle_signup(self, form_data: dict):
        """Handle signup form submission."""
        self.full_name = form_data["full_name"]
        self.email = form_data["email"]
        self.password = form_data["password"]
        self.confirm_password = form_data["confirm_password"]

        if not self.check_passwords_match():
            self.signup_error = "Passwords do not match"
            return

        # Add your API signup logic here
        # try:
        #     response = await api.post("/signup", json={
        #         "full_name": self.full_name,
        #         "email": self.email,
        #         "password": self.password
        #     })
        #     if response.status_code == 200:
        #         return rx.redirect("/login")
        #     else:
        #         self.signup_error = "Signup failed"
        # except Exception as e:
        #     self.signup_error = "Signup failed"

        # For demo, redirect to login
        return rx.redirect("/login")