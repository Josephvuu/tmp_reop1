# Name: Joseph Vu
# Student ID: 887091577
# Section: 07
# Assignment: Module 9 Assignment 1

population_dict = {}

while True:
    city = input("What is next city? (enter q to quit) ")
    if city.lower() == 'q':
        break
    population = input(f"What is the population of {city}? ")
    population_dict[city] = population

max_small = int(input("What is the largest population for a small town? "))

big_cities = []
small_towns = []

for city, pop in population_dict.items():
    if int(pop) > max_small:
        big_cities.append(f"{city},{pop}")
    else:
        small_towns.append(f"{city},{pop}")

with open("populationdata.txt", "w") as f:
    bc_str = "Big Cities: " + " ".join(big_cities) if big_cities else "Big Cities: "
    st_str = "Small Towns: " + " ".join(small_towns) if small_towns else "Small Towns: "
    print(bc_str, file=f)
    print(st_str, file=f)