# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/07 12:52:26 by ymarcais          #+#    #+#              #
#    Updated: 2022/12/07 13:56:56 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

iterable = [1, 2, 3, 4, 5, 6]
y = lambda dum: not (dum % 2)

def	ft_filter(y, iterable):
	for x in iterable:
		if y(x) is True:
			yield x

print(list(ft_filter(y, iterable)))
