# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <ymarcais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/06 10:31:12 by ymarcais          #+#    #+#              #
#    Updated: 2023/02/04 14:07:20 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import datetime
from recipe import Recipe

class Book:
	@staticmethod
	def getcurrent_time() -> str
		return datetime.now().strftime("%Y-%m-%d %H:%M")

	def __init__(self, name = "Cookbook"):
		self.name = name
		self.creation_date = self.getcurrent_time()
		self.recipe.list = {"starter": [], "lunch" : [], "dessert" : []}

	def get_recipe_by_name(self, name : str) -> Recipe
		for meals in self.recipes_list.values():
			for meal in meals:
				if (meal.name == name):
					return (meal)
		return (None)

	def add_recipe(self, recipe: Recipe) -> None:
		"Add the recipe to the book"
		if not is(recipe, Recipe)
			print("Not a recipe")
			return
		self.recipe_list[recipe.recipe_type].append(recipe)
		self.lat_uptdate = self.get_current_time()
	
	if __name__ == "__main__":
		abc = Book()

		salad = Recipe("salad", 1 , 123, ["Salad of course", "Tomatoes" , "Avocado"], "A meal we can eat", "lunch")
		abc.add_recipe(salad)

		soupe = Recipe("soupe", 1 , 123, ["Salad of course", "Tomatoes" , "Avocado"], "A meal we can eat", "lunch")
		abc.add_recipe(soupe)

		cake = Recipe("cake", 1 , 123, ["Salad of course", "Tomatoes" , "Avocado"], "A meal we can eat", "dessert")
		abc.add_recipe(cake)

		print("Get salad : " + str(abc.get_recipe_by_name("salad")))
		print("Starter : " + str(abc.get_recipes_by_types('starter')))
		print("Lunch : " + str(abc.get_recipes_by_types('lunch')))
		print("Dessert : " + str(abc.get_recipes_by_types('dessert')))