# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <ymarcais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/04 14:08:29 by ymarcais          #+#    #+#              #
#    Updated: 2023/02/04 15:01:45 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def generator (text, sep = " ", option = None)
    if not isinstance(text, str) or not isinstance(sep, str) \
        or option not in [None, "shuffle", "unique", "ordered"]:
        yield ("Error")
        return

    lst = text.split(sep)

    if (option == 'shuffle'):
        lst.sort(key=lambda x: random())
    elif (option == 'unique'):
        lst = [word for i, wor in enumerate(lst) if lst[:i].count(word) == 0]
    elif (option == 'ordered'):
        lst.sort()

    for words in lst:
        yield (words)