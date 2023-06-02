# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    FileLoader.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/09 10:18:10 by ymarcais          #+#    #+#              #
#    Updated: 2022/12/11 10:47:32 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import pandas as pd

class FileLoader:

	def load(self, path):
		df = pd.read_csv(path)
		#print(df.shape)
		return pd.DataFrame(df)
	
	def display(self, df, n):
		if n > 0:
			return df.head(n)
		else:
			return df.tail(1)

path = '/mnt/nfs/homes/ymarcais/42githubperso/AI/04day/athlete_events.csv'
myClass = FileLoader()
print(myClass.load(path))
df = myClass.load(path)
#print(myClass.display(df, -4))p
