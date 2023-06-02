# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    prediction2.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <ymarcais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/04 15:46:54 by ymarcais          #+#    #+#              #
#    Updated: 2023/03/04 16:25:42 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def prediction(x, theta):
    x_row = x.shape[0]
    x = np.reshape(x, (x_row, 1))
    vector_1 = [1] * x_row
    vector_1 = np.reshape(vector_1, (x_row, 1))
    xp = np.concatenate((vector_1, x), axis = 1)
    y_hat = np.dot(xp, theta)
    return y_hat

    
x = np.arange(1,6)
theta = np.array([[5], [0]])
#print(prediction(x, theta))

theta2 = np.array([[0], [1]])
prediction(x, theta2)
#print(prediction(x, theta2))

theta3 = np.array([[5], [3]])
print(prediction(x, theta3))