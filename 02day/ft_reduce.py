# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_reduce.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <ymarcais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/07 13:58:44 by ymarcais          #+#    #+#              #
#    Updated: 2023/02/12 17:13:32 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

lst = ["H", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"]
y = lambda u, v: u + v

def ft_reduce(y, lst):
	it = iter(lst)
	total = next(it)
	for x in it:
		total = y(total, x)
	return total


print(ft_reduce(y, lst))
print(list(ft_reduce(y, lst)))


lst =["H", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"]
y = lamda u, y: u + v
		
