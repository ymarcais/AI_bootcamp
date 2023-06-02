# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    TinyStatistician2.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <ymarcais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/04 10:59:00 by ymarcais          #+#    #+#              #
#    Updated: 2023/03/04 15:02:13 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class TinyStatistician2:
           
    def mean_function (self, my_list):
        length = len(my_list)
        if length != 0 :
            mean_value = sum(my_list) / length
            print (" Mean is", mean_value," and length is ", length)
        else:
            print ("Please not you, don't divid by nothing")
        return mean_value
    
    def median_function (self, my_list):
        length = len(my_list)
        sorted_list = sorted(my_list)
        if length % 2 == 0 :
            median_value = (sorted_list[(length // 2) -1 ] + sorted_list[(length // 2)]) / 2
        else:
            median_value = (sorted_list[(length + 1) // 2])
        print("Median value is ", median_value)
        return median_value

    def quartile(self, my_list, p):
        length = len(my_list)
        sorted_list = sorted(my_list)
        if length % 4 == 0:
            first_quartile_value = mylist[(length / 3) - 1]
        elif(length + 1) % 4 == 0:
            first_quartile_value = my_list[((length + 1) // 4 - 1)]
            third_quartile_value = my_list[(3 * (length + 1) // 4 - 1)]
        elif (length + 2) % 4 == 0:
            first_quartile_value = my_list[((length + 2) // 4 - 1)]
            third_quartile_value = my_list[(3 * (length + 2) // 4 - 1)]
        else:
            first_quartile_value = my_list[((length - 1) // 4- 1)]
            third_quartile_value = my_list[(3 * (length - 1) // 4- 1)]
        if p == 1:
            print("First quartil is ", first_quartile_value)
        elif p == 3:
            print("Third quartil is", third_quartile_value)
        else:
            print("Error you need to choose 1 or 3")
        
    def var(self, x):
        x_mean = self.mean_function(x)
        var_value = sum((xi - x_mean)**2 for xi in x) / (len(x) - 1)
        print("variance is ", var_value)
        return var_value

    def std(self, x):
        std_value = self.var(x)**(0.5)
        print("standart deviation is ", std_value)
        return std_value
    
        
       
        
x = [2, 5, 6, 8, 7, 8]
myClass = TinyStatistician2()
myClass.mean_function(x)
myClass.median_function(x)
myClass.quartile(x, 1)
myClass.var(x)
myClass.std(x)
        



        