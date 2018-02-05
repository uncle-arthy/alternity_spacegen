#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'Alexey Evdokimov'
import random


class Dice(object):
    @staticmethod
    def d20():
        return random.randint(1, 20)
    
    @staticmethod
    def d12():
        return random.randint(1, 12)
    
    @staticmethod
    def d10():
        return random.randint(1, 10)
    
    @staticmethod
    def d2():
        return random.randint(1, 2)


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
        
        self.make_stars()
        
    def make_stars(self):
        # How many stars?
        roll_for_stars = Dice.d20()

        if roll_for_stars < 11:  # TODO: make it with NumPy and choise by weight
            number_of_stars = 1
        elif roll_for_stars < 17:
            number_of_stars = 2
        elif roll_for_stars < 19:
            number_of_stars = 3
        elif roll_for_stars < 20:
            number_of_stars = 4
        else:
            number_of_stars = 5

        for _ in range(number_of_stars):
            self.stars.append(Star())
        print(f"Number of stars: {number_of_stars}")

class Star(object):  # TODO: make help on star classes and types
    
    # "Common" stars spectral classes
    NO_CLASS = "no_class_star"
    O_CLASS = "o_class_star"
    B_CLASS = "b_class_star"
    A_CLASS = "a_class_star"
    F_CLASS = "f_class_star"
    G_CLASS = "g_class_star"
    K_CLASS = "k_class_star"
    M_CLASS = "m_class_star"
    # Non-sequence stars
    BLACK_HOLE = "black_hole"
    NEUTRON = "neutron_star"
    WHITE_DWARF = "white_dwarf_star"
    BLACK_DWARF = "black_dwarf_star"
    BROWN_DWARF = "brown_dwarf_star"
    RED_SUPERGIANT = "red_supergiant_star"
    
    
    def __init__(self):
        pass
    
    def single_star(self):
        pass
    
    def binary_star(self):
        pass

    
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


if __name__ == '__main__':
    ss = StarSystem()
