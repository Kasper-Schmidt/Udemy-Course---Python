countries_of_UK = ["England", "Scotland", "Northern Ireland", "Wales"]

num_of_countries = len(countries_of_UK)

# Listen indeholder 4 elementer, men indeks starter ved 0:
print(countries_of_UK[0])  # England
print(countries_of_UK[1])  # Scotland
print(countries_of_UK[2])  # Northern Ireland
print(countries_of_UK[3])  # Wales

# Det sidste gyldige indeks er længden minus 1:
print(countries_of_UK[num_of_countries - 1])  # Wales


# OUT OF RANGE-EKSEMPLER:

# Listen har ikke indeks 4:
# print(countries_of_UK[4])
# IndexError: list index out of range

# num_of_countries er 4, så dette forsøger også at bruge indeks 4:
# print(countries_of_UK[num_of_countries])
# IndexError: list index out of range

# Negative indeks tæller baglæns, men -5 er uden for denne liste:
# print(countries_of_UK[-5])
# IndexError: list index out of range