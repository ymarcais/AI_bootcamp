# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ImageProcessor.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ymarcais <ymarcais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/18 13:55:54 by ymarcais          #+#    #+#              #
#    Updated: 2023/02/18 16:09:52 by ymarcais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

class ImageProcessor:

    def load(self, path):
            img = Image.open(path)
            width, height = img.size
            img = img.convert("RGB")
            pixels_list = list(img.getdata())
            pixels_array = np.array(pixels_list, dtype=np.float64)
            pixels_array = pixels_array.reshape(height, width, 3)
            pink_filter = pixels_array.copy()
            pink_filter[:,:,0] *= 1.8# increase red channel
            pink_filter[:,:,2] *= 4.2 # increase blue channel
            return {"width": width, "height": height, "pixels": pink_filter}
         
             
# * astype(np.uint8) is a method provided by the NumPy library 
# * that is used to convert the data type of a NumPy array to an 8-bit unsigned integer type
path = 'image200x190.png'
myClass = ImageProcessor()
result = myClass.load(path)
print("longueur est de %d et la hauteur est de %d" % (result["width"], result["height"]))
print(result["pixels"])
plt.imshow(result["pixels"].astype(np.uint8))
plt.show()




        
