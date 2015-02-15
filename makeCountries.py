from country import Country


def makeCountries():
    """
    Makes 2 lists, 1 with names that *.txt contains, and 1 with Country-objects with the names of list 1.
    """
    countries = []
    countries_obj = []
    with open("countries_list.txt") as in_f:
        for line in in_f:
            countries.append(line.strip())
            countries_obj.append(Country(line.strip()))
    return countries, countries_obj
