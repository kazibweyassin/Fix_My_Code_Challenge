#!/usr/bin/python3
""" 
User class
"""

class User():
    """A class representing a user."""

    def __init__(self):
        """Initialize a User object."""
        self.__email = None

    def set_email(self, value):
        """Set the email address of the user.

        Args:
            value (str): The email address to set.

        Raises:
            TypeError: If the value is not a string.
        """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value

    @property
    def email(self):
        """Get the email address of the user.

        Returns:
            str: The email address of the user.
        """
        return self.__email

    @email.setter
    def email(self, value):
        """Set the email address of the user.

        Args:
            value (str): The email address to set.
        """
        self.set_email(value)
   
if __name__ == "__main__":
    u = User()
    u.email = "john@snow.com"
    print(u.email)
