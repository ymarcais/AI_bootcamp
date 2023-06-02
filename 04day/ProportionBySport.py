# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ProportionBySport.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/11 11:35:34 by ymarcais          #+#    #+#              #
#    Updated: 2022/12/11 12:23:45 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd

class olymp:

	def proportion_by_sport(self, data, oy, gender, sport):
		poy = data[data["Year"] == int(oy)]
		goy = poy[poy["Sex"] == str(gender)]
		nb_total_player = len(goy)
		soy = goy[goy["Sport"] == str(sport)]
		nb_sport_player = len(soy)
		proportion = (nb_sport_player/nb_total_player)*100
		print(round(proportion, 2),"%")
		return ("")

from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('/mnt/nfs/homes/ymarcais/AI/athlete_events.csv')
myClass = olymp()
print(myClass.proportion_by_sport(data, 1992, "F", "Judo"))

