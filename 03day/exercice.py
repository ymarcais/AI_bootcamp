# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exercice.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <ymarcais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/18 10:55:34 by ymarcais          #+#    #+#              #
#    Updated: 2023/02/18 11:18:12 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

class   NumPyCreator:

    def from_list(self, lst):
        arr = np.array(lst)
        return (arr)

    def from_tuple(self, tpl):
        arr = np.array(tpl)
        return (arr)
    
    def from_iterable(self, itr):
        arr = np.array(itr)
        return (arr)
    
    def from_shape(self, shape, value):
        arr = np.empty(shape)
        arr = np.array(value)
        arr.shape = shape
        return (arr.shape)

