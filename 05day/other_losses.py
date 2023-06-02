# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    other_losses.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/14 13:40:43 by ymarcais          #+#    #+#              #
#    Updated: 2022/12/14 14:58:25 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from vec_loss import loss_
from math import sqrt

def mse_(y, y_hat):
	mse = 2 * loss_(y, y_hat)
	return mse

def rmse_(y, y_hat):
	rmse = sqrt(mse_(y, y_hat))
	return rmse

def mae_(y, y_hat):
	m = y.shape[0]
	one = [1] * m 
	mae = (1 / m) *np.dot(one, abs(y - y_hat))
	return mae

def r2score_(y, y_hat):
	m = y.shape[0]
	ym = sum(y) / m
	t = (y - y_hat).reshape(1, m)
	num = np.dot(t, (y - y_hat))

	t2 = (y - ym).reshape(1, m)
	den = np.dot(t2, (y - ym))
	r2 = 1 - (num / den)
	return r2 


x = np.array([0, 15, -9, 7, 12, 3, -21])
y = np.array([2, 14, -13, 5, 12, 4, -19])
print(r2score_(x, y))
