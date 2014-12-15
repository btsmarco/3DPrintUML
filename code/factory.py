#! /usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import division
import os, sys, re

# Assumes SolidPython is in site-packages or elsewhwere in sys.path
from solid import *
from solid.utils import *

def assembly(bX,bY,CardList,LineList):

    # Slab
    boardX = bX
    boardY = bY
    base = cube([boardX, boardY, 1],True)

    Cubes = []

    for card in CardList:
        c = translate(card.GetPosition())(color(Red)(cube([card.GetWidth(),card.GetHeight(),0.5],True)))
        Cubes.append(c)

    Lines = []
    for line in LineList:
        l = translate(line.GetPosition())(color(Red)(cube([line.GetWidth(),1,0.5],True)))
        Lines.append(l)

    FinalBoard = union()(
            base,
            Cubes,
            Lines,
        )

    return FinalBoard
