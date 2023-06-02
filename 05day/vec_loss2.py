# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vec_loss2.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <ymarcais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/05 10:59:54 by ymarcais          #+#    #+#              #
#    Updated: 2023/03/05 11:10:05 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def loss_(y, y_hat):
    m = len(y)
    J = sum((np.subtract(y_hat, y))**2 / (2 * m))
    return J

X = np.array([[0], [15], [-9], [7], [12], [3], [-21]])
Y = np.array([[2], [14], [-13], [5], [12], [4], [-19]])
# Example 1:
print(loss_(X, Y))

    