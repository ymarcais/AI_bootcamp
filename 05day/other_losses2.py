# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    other_losses2.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <ymarcais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/05 11:13:00 by ymarcais          #+#    #+#              #
#    Updated: 2023/03/05 11:59:25 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

class other_losses:
    def mse_(self, y, y_hat):
        size = len(y)
        mse = np.sum((np.subtract(y, y_hat))**2 / size)
        return mse
    
    def rmse_(self, y, y_hat):
        rmse = self.mse_(y, y_hat)**0.5
        return rmse
        
    def mae_(self, y, y_hat):
        size = len(y)
        mae = np.sum(np.abs(np.subtract(y, y_hat)) / size)
        return mae

    def r2_(self, y, y_hat):
        size = len(y)
        y_mean = np.sum(y) / size
        r2 = 1 - (np.sum(np.subtract(y_hat, y)**2) / np.sum(np.subtract(y, y_mean)**2))
        return r2

myClass = other_losses()
# Example 1:
x = np.array([0, 15, -9, 7, 12, 3, -21])
y = np.array([2, 14, -13, 5, 12, 4, -19])
# Mean squared error
## your implementation
print(myClass.r2_(x, y))