# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    fit.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/13 14:18:30 by ymarcais          #+#    #+#              #
#    Updated: 2022/12/13 15:08:30 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from vec_gradient import simple_gradient

def fit_(x, y, theta, alpha, max_iter):
	i= 0
	while i < max_iter:
		theta = theta -alpha * (simple_gradient( x, y, theta))
		print(theta)
		i += 1
	return theta

x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])
theta= np.array([1, 1]).reshape((-1, 1))

alpha=5e-8
max_iter=1500000
theta = fit_(x, y, theta, alpha, max_iter)
print(theta)
