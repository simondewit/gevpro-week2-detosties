#!/opt/local/bin/python3.4
# Simon de Wit, januari 2015


class Country():
    def __init__(self, name):
        """
        Creates a Country object with 'name' as name.
        """
        self.name = name

    def getName(self):
        """
        Returns the name of the Country object.
        """
        return self.name

    def __str__(self):
        return "{}{}".format("Hello from ", self.name)

    def __repr__(self):
        return "{}{}".format("Hello from ", self.name)
