# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/06 10:33:45 by ymarcais          #+#    #+#              #
#    Updated: 2022/12/06 19:20:57 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class Recipe:
	name: str
	cooking_lvl:int
	cooking_time:int
	ingredients:list
	description:str
	recipe_type:str

	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):

		if type(name) != str:
			print(type(name))
			sys.exit()
		self.name = name

		if type(cooking_lvl) is not int:
			print(type (cooking_lvl))
			sys.exit()
		self.cooking_lvl = cooking_lvl

		self.cooking_time = cooking_time

		if type(ingredients) != list:
			print(type (ingredients))
			sys.exit()
		self.ingredients = ingredients		

		self.description = description

		if 	recipe_type not in ["starter", "lunch", "dessert"]:
			print("dfghj")
			sys.exit()
		self.recipe_type = recipe_type

	def __str__(self):
		txt = "name: " + self.name + "\ncooking_lvl: " + str(self.cooking_lvl) + "\ncooking_time: " + str(self.cooking_time) + "\ningredients: " + str(self.ingredients) + "\ndescriptions: " + self.description + "\nrecipe_type: " + self.recipe_type + "\n"
		return txt

