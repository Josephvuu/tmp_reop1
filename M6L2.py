def get_fav_food():
    foods_dict = {}
    fav_food = ""

    while fav_food != 'q':
        fav_food = input("Enter your favorite food or 'q' to quit: ")
        if (fav_food == 'q'):
            break

        country = input("What country is that food from? ")
        foods_dict[fav_food] = country

    return foods_dict


empty_list = get_fav_food()
print(empty_dict)