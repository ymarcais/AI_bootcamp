# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    matrix.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <ymarcais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/05 13:08:09 by ymarcais          #+#    #+#              #
#    Updated: 2023/03/05 13:36:00 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Matrix:
    def __init__(self, data=None, shape=None)
        if data = None:
            self.data = data
            self.shape = (len(data), len(data[0]))
        elif shape is not None:
            self.data = [0] * shape[1] for _ in range(shape[0])
            self.shape = shape
        else:
            raise ValueError('Either data or shape must be prodvided')
class Vector:
    def __init__(self, data)
    self.data = data

myClass = Matrix()
data = data([1, 2], [3, 4])