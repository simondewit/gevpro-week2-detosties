#!/usr/bin/env python
# Simon de Wit, januari 2015


class Country():
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return "{}{}".format("Hello from ", self.name)
