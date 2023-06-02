# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <ymarcais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/05 13:50:23 by ymarcais          #+#    #+#              #
#    Updated: 2023/01/21 14:25:09 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
Reverses the order of a string and the case of its words.
"""

import sys

res = []
for arg in sys.argv[:0:-1]:
	res.append(arg[::-1])
if len(res) != 0:
	print(" ".join(res).swapcase())