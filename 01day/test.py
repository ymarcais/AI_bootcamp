# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/06 18:31:47 by ymarcais          #+#    #+#              #
#    Updated: 2022/12/06 19:06:46 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#from book import Book
from recipe import Recipe

Myrecipe = Recipe("crepe", 2, 30, ["lait", "oeuf", "bierre", "farine"], "facile", "dessert")
print(str(Myrecipe))

