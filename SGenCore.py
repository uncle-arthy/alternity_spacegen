#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'Alexey Evdokimov'


class Cluster(object):
    def __init__(self):
        self.cluster_size_hexes = (20, 20)  # Size of cluster in hexes
        self.hex_size = 5  # Size of hex in LY
        self.star_systems = []
        self.nebulas = []


class StarSystem(object):
    def __init__(self):
        self.stars = []  # One or more. Main star goes first
        self.planets = []  # Including asteroid and comet belts
    

class Star(object):
    
    NO_TYPE = "no_type"
    
    def __init__(self):
        self.star_type = Star.NO_TYPE

    
class Planet(object):
    
    ASTEROID_BELT = "asteroid_belt"
    COMET_BELT = "comet_belt"
    TERRAN_TYPE = "terran_type"
    GAS_GIANT = "gas_giant"
    
    def __init__(self):
        self.parent_system = None
        self.planet_type = Planet.TERRAN_TYPE
        self.graph_type = [0, 0, 0, 0, 0]  # GRAPH type of planet according to rulebook
        self.moons = []


class Moon(object):
    def __init__(self):
        self.parent_planet = None
