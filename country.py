#!/opt/local/bin/python3.4
# Simon de Wit, januari 2015


class Country():
    def __init__(self, name, color):
        """
        Creates a Country object with 'name' as name.
        """
        self.name = name
        self.color = color

    def getName(self):
        """
        Returns the name of the Country object.
        """
        return self.name

    def getColor(self):
        """
        Returns the color name of the Country object.
        """
        return self.color

    def __str__(self):
        return "{}{}".format("Hello from ", self.name)

    def __repr__(self):
        return "{}{}".format("Hello from ", self.name)
