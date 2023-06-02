# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/01/14 14:53:24 by ymarcais          #+#    #+#              #
#    Updated: 2023/01/14 15:02:54 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

class charType():
	UPPER = 0
	LOWER = 1
	PUNC = 2
	SPACE = 3
	LEN = 4
	
def	text_analyser(*args) -> None:

	entry = ""
	argc = len(args)
	ulps = [0] * charType.LEN # [0, 0, 0, 0]
	if argc == 0:
		print("Waiting for input...")
		for line in sys.stdin:
			entry += line.rstrip('\n')
	elif argc == 1:
		entry = args[0]
		print("yep")
	else:
		print("ERROR")
		return
	for char in entry:
		if char.isupper():
			ulps[charType.UPPER] += 1
		elif char.islower():
			ulps[charType.LOWER] += 1
		elif char in string.punctuation:
			ulps[charType.PUNC] += 1
		elif char.isspace():
			ulps[charType.SPACE] += 1
	print("The text contains %d characters:" % len(entry))
	print("- %d upper letters" % ulps[charType.UPPER])
	print("- %d lower letters" % ulps[charType.LOWER])
	print("- %d punctuation marks" % ulps[charType.PUNC])
	print("- %d spaces" % ulps[charType.SPACE]) 


if __name__ == "__main__":
    if (len(sys.argv) == 1):
       text_analyser()
    else:
        text_analyser(*sys.argv[1:])

"""
text_analyzer("Python 2.0, released 2000, introduced features \
like List comprehensions and a garbage collection system capable of \
collecting reference cycles.")
"""
