# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/05 17:31:54 by ymarcais          #+#    #+#              #
#    Updated: 2022/12/05 19:51:05 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

mylist = sys.argv[1:]
len = len(mylist)
if len == 0:
    sys.exit()
if len > 1:
    print("error")
    sys.exit

num_string = mylist[0]
if num_string[0] == '-':
    if not mylist[0][1:].isdigit():
        print("error")
        sys.exit()
    else:
        x = int(mylist[0]) 
else:
    if not mylist[0][0:].isdigit():
        print("error")
    x = int(mylist[0])
if x == 0:
    print("it s NULL")
elif x % 2 == 0:
        print("it s even")
else:
    print("its odd")
