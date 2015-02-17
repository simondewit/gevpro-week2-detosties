#!/opt/local/bin/python3.4
# Simon de Wit, januari 2015


class Country():
    def __init__(self, name, colour):
        """
        Creates a Country object with 'name' as name.
        """
        self.name = name
        self.colour = colour

    def getName(self):
        """
        Returns the name of the Country object.
        """
        return self.name

    def getColour(self):
        """
        Returns the color name of the Country object.
        """
        return self.colour

    def __str__(self):
        return "{}{}".format("Hello from ", self.name)

    def __repr__(self):
        return "{}{}".format("Hello from ", self.name)
