# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    TinyStatistician.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <ymarcais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/12 13:17:22 by ymarcais          #+#    #+#              #
#    Updated: 2023/02/12 19:24:22 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class TinyStatistician:

	def mean(self, x):
		j = 0
		b = 0
		for i in x:
			b += i
			j += 1
		return b/j 

	def quartil(self, x, p):
		size = len(x)
		if size == 0:
				return None
		i = int((p / 100) * size)
		x = sorted(x)
		res = [i]
		if size % 2 == 0:
			res += x[i - 1]
			res /= 2
		return (res)
		
	def median(self, x):
		return TinyStatistician.quartil(self, x, 50)
	
	def var(self, x):
		size = len(x)
		if size == 0:
			return None
		res = 0
		xmean = TinyStatistician.mean(self, x)
		for i in range(size):
			res +=(x[i] - xmean) ** 2
		return res / size

	def std(self, x):
		return TinyStatistician.var(self, x)	** 0.5
 
a = [1, 42, 300,10, 59]
print(TinyStatistician().quartil(a, 30))
print(TinyStatistician().mean(a))
print(TinyStatistician().median(a))
print(TinyStatistician().var(a))
print(TinyStatistician().std(a))

