# -*- coding: utf-8 -*-

"""
Filename: typeHolo.py

Description:
Here have to be defined the classes.
Author: Simon BECKER
Date: 2024-07-09

License:
GNU General Public License v3.0

Copyright (C) [2024] Simon BECKER

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
import numpy as np

class info_Holo:
    nb_pix_X = 0
    nb_pix_Y = 0
    pixSize = 0.0
    magnification = 0.0
    lambdaMilieu = 0.0

class particule:
    def __init__(self, posX, posY, posZ, nb_vox):
        self.posX = posX
        self.posY = posY
        self.posZ = posZ
        self.nb_vox = nb_vox

    def __repr__(self):
        return """Objet X:% s, Y:% s, Z:% s, nb_vox:% s\n"""%(self.posX, self.posY, self.posZ, self.nb_vox)


class objet:
    def __init__(self, nb_pix = 0, label = 0, pSum = 0.0, pxSumX = 0.0, pxSumY = 0.0, pxSumZ = 0.0, xMin = 0, xMax = 0, 
    yMin = 0, yMax = 0, zMin = 0, zMax = 0, baryX = 0.0, baryY = 0.0, baryZ = 0.0):
        self.nb_pix = nb_pix
        self.label = label
        self.pSum = pSum
        self.pxSumX = pxSumX
        self.pxSumY = pxSumY
        self.pxSumZ = pxSumZ
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.zMin = zMin
        self.zMax = zMax
        self.baryX = baryX
        self.baryY = baryY
        self.baryZ = baryZ

    def __repr__(self):
        return """Objet nbPix:% s, label:% s
        pSum:% s, pxSumX:% s, pxSumY:% s, pxSumZ:% s
        xMin:% s, xMax:% s, yMin:% s, yMax:% s, zMin:% s, zMax:% s
        baryX:% s,baryY:% s,baryZ:% s\n"""%(self.nb_pix, self.label, self.pSum, self.pxSumX, self.pxSumY, self.pxSumZ, self.xMin, self.xMax, self.yMin, \
        self.yMax, self.zMin, self.zMax, self.baryX, self.baryY, self.baryZ)

""" monObj = objet(10, 5, 2)
monObj.baryY = 52
print(monObj)
maListObj = []
maListObj.append(monObj)
maListObj.append(monObj)

for obj in maListObj:
    print(obj) """
