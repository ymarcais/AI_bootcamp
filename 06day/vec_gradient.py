# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vec_gradient.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/13 11:06:23 by ymarcais          #+#    #+#              #
#    Updated: 2022/12/13 14:05:34 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import pandas as pd

def simple_gradient( x, y, theta):
	df = pd.DataFrame(x)
	shape = df.shape
	m = shape[0]
	v1 = [1] * m 
	v1 = np.reshape(v1, (m, 1))
	xp = np.concatenate((v1, x), axis = 1)
	xp2 = np.dot(xp, theta)
	xpt = xp.transpose()
	sub = xp2 - y
	grad = (1 / m) *np.dot(xpt, sub)

	return grad 

x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733]).reshape((-1, 1))
y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554]).reshape((-1, 1))
theta = np.array([2, 0.7]).reshape((-1, 1))
print(simple_gradient(x, y, theta))



 
