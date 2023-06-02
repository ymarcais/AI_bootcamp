# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    SpatioTemporalData.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/11 13:02:17 by ymarcais          #+#    #+#              #
#    Updated: 2022/12/11 14:16:22 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd

class SpatioTemporalData:

	def where(self, data, oy):
		poy = data[data["Year"] == int(oy)]
		city = poy["City"][0]
		print(city)
		return ""

	def when(self, data, loc):
		loy = data[data["City"] == str(loc)]
		year = loy["Year"][0]
		print(loy)
		return ""

from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('/mnt/nfs/homes/ymarcais/AI/athlete_events.csv')
myClass = SpatioTemporalData()

print(myClass.where(data, 1992))
