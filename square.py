#!/usr/bin/python3

class square():
    """
    A class representing a square.
    """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """
        Initializes a square object.

        Args:
            *args: Variable length arguments to set attributes of the square.
            **kwargs: Keyword arguments to set attributes of the square.
        """
        for arg in args:
            setattr(self, arg[0], arg[1])
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """
        Calculates the area of the square.

        Returns:
            The area of the square.
        """
        return self.width * self.width

    def Perimiter_of_my_square(self):
        """
        Calculates the perimeter of the square.

        Returns:
            The perimeter of the square.
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            A string representation of the square in the format "width/height".
        """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.Perimiter_of_my_square())
