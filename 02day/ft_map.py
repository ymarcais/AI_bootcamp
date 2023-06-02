# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_map.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/07 10:58:10 by ymarcais          #+#    #+#              #
#    Updated: 2022/12/07 12:04:33 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

iterable = [7, 2, 3, 4, 5]
y = lambda dum: dum + 1 

def ft_map(y, iterable):
	gen_exp = (y(x) for x in iterable)
	return gen_exp

print(list(ft_map(y,iterable)))
