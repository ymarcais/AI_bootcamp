# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <ymarcais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/01/28 15:45:51 by ymarcais          #+#    #+#              #
#    Updated: 2023/01/28 18:48:02 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# use of nested dictionary

cookbook = {}

def print_recipe(recipe: str) -> None:
    print("Here is your recipe for %s, a %s meal:" %(recipe, cookbook[recipe]["meal"]))
    print("It takes %d minutes of cooking." %(cookbook[recipe]["prep_time"]))
    print("And that's what you'll need : ", end="")
    print(", ".join(cookbook[recipe]["ingredients"])

def recipe_delone(recipe: str) -> None:
    print("%s's recipe is deleted\n" %recipe)
    del cookbook[recipe]

def addrecipe(recipe: str, t_meal: str, time: int, ingredients: list[str], verbose: bool = True):
    cookbook[recipe] = {"meal" : t_meal, "prep_time": time, "ingredients" : ingredients}

def print_cookbook():
    if len(cookbook) == 0:
        print("Your cookbook is empty :(")
    else:
        print("You cookbook contains:")
        for recipe in cookbook:
            print("-" + recipe)
    print("")

# Function used in the loop:

def strip_arr(src: list[str] -> list[str]
    for elem in src:
        yield elem.strip())

def ft_addrecipe():
    try:
            recipe_name = str(intput("Pleqse, set your recipe name: "))
            type_meal = str(input("and its type of meal: "))
            time_min = int(intput(how long does it takes, in minutes: "))
            if (time_min < 0): raise ValueError
            ingredients = str(input("Don't forget the ingredients ! :").split(","))
    except  ValueError:
        print("\nWrong input...\n")
        return
    ingredients = [elem for elem in strip_arr(ingredients) if (len(elem) > 0)]
    addrecipe(recipe_name, type_meal, time_min, ingredients)



    

