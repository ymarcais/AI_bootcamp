# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    my_linear_regression.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/13 15:18:06 by ymarcais          #+#    #+#              #
#    Updated: 2022/12/13 16:45:22 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



class MyLinearRegression():

	def __init__(self, thetas, alpha=0.001, max_iter=1000):
		self.alpha = alpha
		self.max_iter = max_iter
		self.thetas = thetas

	 def fit_(self, x, y, thetas, alpha, max_iter):
		i= 0
		while i < max_iter:
			thetas = thetas -alpha * (simple_gradient( x, y, thetas))
			i += 1
		return thetas

def predict_(x, theta):
		m = x.shape[0]
		x = np.reshape(x, (m, 1))
		v1 = [1] * m
		v1 = np.reshape(v1, (m, 1))
		xp = np.concatenate((v1, x), axis = 1)
		y_hat = np.dot(xp, theta)
		return y_hat

