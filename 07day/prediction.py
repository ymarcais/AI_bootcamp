# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    prediction.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/16 16:38:42 by ymarcais          #+#    #+#              #
#    Updated: 2022/12/16 16:47:00 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def predict_(x, theta):
		m = x.shape[0]
		n = x.shape[1]
		x = np.reshape(x, (m, n))
		v1 = [1] * m
		v1 = np.reshape(v1, (m, 1))
		xp = np.concatenate((v1, x), axis = 1)
		y_hat = np.dot(xp, theta)
		return y_hat

x = np.arange(1,13).reshape((4,-1))
#theta = np.array([5, 0, 0, 0]).reshape((-1, 1))
theta = np.array([0, 1, 0, 0]).reshape((-1, 1))
predict_(x, theta)
print(predict_(x, theta))
