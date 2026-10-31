# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        """
        Initialise a person with a name and date of birth

        Raises TypeError for invalid types and ValueError for an empty name
        """
        
        if type(name) is not str:
            raise TypeError()
        if name == "":
            raise ValueError()

        if type(birth) is not date:
            raise TypeError()

        
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

        self.name = name
        self.birth = birth

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

    def initials(self):
        """
        Return the uppercase initials of the person's name
        """
        parts = self.name.split()
        initials = ""

        for word in parts:
            initials += word[0].upper()

        return initials

    def is_birthday(self):
        """
        Return True if today is the person's birthday
        """

        today = date.today()

        if self.birth.day == today.day and self.birth.month == today.month:
            return True
        else:
            return False