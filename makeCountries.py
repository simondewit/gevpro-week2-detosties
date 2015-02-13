from country import Country


def makeCountries(fname, l):
    countries = []
    countries_obj = []
    with open('countries_list.txt', 'r') as in_f:
        for line in in_f:
            countries.append(line.strip())
            countries_obj.append(Country(line.strip()))
    return countries, countries_obj
