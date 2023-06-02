# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tools.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/12 15:44:14 by ymarcais          #+#    #+#              #
#    Updated: 2022/12/12 18:16:01 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import pandas as pd

def add_intercept(x):
	df = pd.DataFrame(x)
	shape = df.shape
	nb_row = shape[0]
	nb_col= shape[1]
	y = np.ones(nb_row)
	x = np.insert(x, 0, y, axis=1)
	return x 

#x = np.arange(1,6)
x = np.arange(1,13).reshape(3,4)
print(add_intercept(x))
	
