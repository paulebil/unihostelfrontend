import reflex as rx

class AppState(rx.State):
    user_role: str = "guest"  # Default role (e.g., "student", "custodian", "admin", "guest")

    def set_user_role(self, role: str):
        """Set the user role after login."""
        self.user_role = role