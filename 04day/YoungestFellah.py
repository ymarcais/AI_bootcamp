# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    YoungestFellah.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/09 11:12:02 by ymarcais          #+#    #+#              #
#    Updated: 2022/12/11 15:15:26 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd

class Olymp:

	def youngest_fellah(self, data, oy): 
		poy = data[data["Year"] == int(oy)]
		poy = poy.nsmallest(10, "Age")
		print("MEN")
		moy = poy[poy["Sex"] == str("M")] 
		print (moy)
		print("FEMAL")
		foy = poy[poy["Sex"] ==	str("F")]
		print(foy)
		return ""	
		

from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('/mnt/nfs/homes/ymarcais/42githubperso/AI/04day/athlete_events.csv')
myClass = Olymp()

print(myClass.youngest_fellah(data, 1992)) 
