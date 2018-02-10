#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'Alexey Evdokimov'
import random
# TODO: import NumPy and implement all table choises with "weight choises"


class Dice(object):
    @staticmethod
    def roll(sides):
        return random.randint(1, sides)
    
    @staticmethod
    def planets_roll(sides, modifier):
        result = 0
        roll = Dice.roll(sides)
        if roll == sides:
            result += sides
        result += roll
        result += modifier
        
        return result
    
    @staticmethod
    def complex_roll(sides, modifier, num_of_dices=1, positive=False):
        '''
        Makes roll of XdY+Z type
        :param positive: If true, result is not less than 0
        :param sides: Y in XdY+Z
        :param modifier: Z in XdY+Z
        :param num_of_dices: X in XdY+Z
        :return: result
        '''
        
        result = 0
        
        for _ in range(num_of_dices):
            result += random.randint(1, sides)
            
        result += modifier
        
        if positive:
            if result < 0:
                result = 0
        
        return result


class Cluster(object):
    def __init__(self):
        self.cluster_size_hexes = (20, 20)  # Size of cluster in hexes
        self.hex_size = 5  # Size of hex in LY
        self.star_systems = []
        self.nebulas = []


class StarSystem(object):
    def __init__(self, system_name="Unknown system"):
        self.star_core = None  # One or more.
        self.planets = []  # Including asteroid and comet belts
        self.system_name = system_name
        
        self.make_stars()  # Make star(s)
        
        if not self.planets:  # If there are planets at all
            self.make_planets()
        
    def make_stars(self):
        # How many stars?
        roll_for_stars = Dice.roll(20)

        # According to Table G58 in GMG
        # TODO: make it with NumPy and choise by weight
        if roll_for_stars < 11:
            number_of_stars = 1
        elif roll_for_stars < 17:
            number_of_stars = 2
        elif roll_for_stars < 19:
            number_of_stars = 3
        elif roll_for_stars < 20:
            number_of_stars = 4
        else:
            number_of_stars = 5
            
        self.star_core = StarCore(number_of_stars)
        
    def make_planets(self):
        pass
            
    def print_chart(self):
        """
        Just a service placeholder function
        :return:
        """
        print(f"\n---===  {self.system_name}  ===---\n")
        print("Stars:")
        for place in self.star_core.stars:
            if type(place) == list:
                print("\n   Binary star:")
                for star in place:
                    print(f"     {star}")
            else:
                print(f"\n   {place}")
        print(f"\nOrbit track: {self.star_core.orbit_track}")


class StarCore(object):  # TODO: make help on star classes and types
    
    # "Common" stars spectral classes
    NO_CLASS = "no_class_star"
    O_B_CLASS = "O/B class"  # Blue-white
    A_CLASS = "A class"  # Blue
    F_CLASS = "F class"  # Green
    G_CLASS = "G class"  # Yellow
    K_CLASS = "K class"  # Orange
    M_CLASS = "M class"  # Red
    # Non-sequence stars
    BLACK_HOLE = "Black hole"
    NEUTRON = "Neutron star"
    WHITE_DWARF = "White dwarf"
    BLACK_DWARF = "Black dwarf"
    BROWN_DWARF = "Brown dwarf"
    RED_SUPERGIANT = "Red supergiant"
    
    def __init__(self, number_of_stars):
        self.stars = []
        self.orbit_track = 0
        self.number_of_planets = None
        
        for _ in range(number_of_stars // 2):
            self.binary_star()
            
        for _ in range(number_of_stars % 2):
            self.single_star()
            
        if self.number_of_planets is None or self.number_of_planets < 0:
            self.number_of_planets = 0
    
    def single_star(self):
        
        # According to Table G59 in GMG
        roll = Dice.roll(20)
        if roll == 1:
            self.stars.append(StarCore.O_B_CLASS)
            if not self.orbit_track:
                self.orbit_track = 1
            if self.number_of_planets is None:
                self.number_of_planets = Dice.planets_roll(12, -8)
        elif roll == 2:
            self.stars.append(StarCore.A_CLASS)
            if not self.orbit_track:
                self.orbit_track = 1
            if self.number_of_planets is None:
                self.number_of_planets = Dice.planets_roll(12, -6)
        elif roll in range(3, 7):
            self.stars.append(StarCore.F_CLASS)
            if not self.orbit_track:
                self.orbit_track = 2
            if self.number_of_planets is None:
                self.number_of_planets = Dice.planets_roll(12, -3)
        elif roll in range(7, 11):
            self.stars.append(StarCore.G_CLASS)
            if not self.orbit_track:
                self.orbit_track = 2
            if self.number_of_planets is None:
                self.number_of_planets = Dice.planets_roll(12, -2)
        elif roll in range(11, 15):
            self.stars.append(StarCore.K_CLASS)
            if not self.orbit_track:
                self.orbit_track = 2
            if self.number_of_planets is None:
                self.number_of_planets = Dice.planets_roll(12, -4)
        elif roll in range(15, 20):
            self.stars.append(StarCore.M_CLASS)
            if not self.orbit_track:
                self.orbit_track = 3
            if self.number_of_planets is None:
                self.number_of_planets = Dice.planets_roll(8, -2)
        else:
            self.non_sequence_star()
            
    def binary_star(self):
        
        # According to Table G60 in GMG
        roll = Dice.roll(20)
        if roll == 1:
            self.stars.append([StarCore.O_B_CLASS, StarCore.WHITE_DWARF])
            if not self.orbit_track:
                self.orbit_track = 1
            if self.number_of_planets is None:
                self.number_of_planets = Dice.planets_roll(12, -9)
        elif roll == 2:
            self.stars.append([StarCore.A_CLASS, StarCore.M_CLASS])
            if not self.orbit_track:
                self.orbit_track = 1
            if self.number_of_planets is None:
                self.number_of_planets = Dice.planets_roll(12, -9)
        elif roll == 3:
            self.stars.append([StarCore.F_CLASS, StarCore.G_CLASS])
            if not self.orbit_track:
                self.orbit_track = 4
            if self.number_of_planets is None:
                self.number_of_planets = Dice.planets_roll(12, -8)
        elif roll == 4 or roll == 5:
            self.stars.append([StarCore.F_CLASS, StarCore.K_CLASS])
            if not self.orbit_track:
                self.orbit_track = 2
            if self.number_of_planets is None:
                self.number_of_planets = Dice.planets_roll(12, -7)
        elif roll == 6 or roll == 7:
            self.stars.append([StarCore.F_CLASS, StarCore.BROWN_DWARF])
            if not self.orbit_track:
                self.orbit_track = 2
            if self.number_of_planets is None:
                self.number_of_planets = Dice.planets_roll(12, -7)
        elif roll in range(8, 12):
            self.stars.append([StarCore.G_CLASS, StarCore.G_CLASS])
            if not self.orbit_track:
                self.orbit_track = 4
            if self.number_of_planets is None:
                self.number_of_planets = Dice.planets_roll(12, -7)
        elif roll in range(12, 16):
            self.stars.append([StarCore.G_CLASS, StarCore.M_CLASS])
            if not self.orbit_track:
                self.orbit_track = 2
            if self.number_of_planets is None:
                self.number_of_planets = Dice.planets_roll(12, -6)
        elif roll == 16 or roll == 17:
            self.stars.append([StarCore.G_CLASS, StarCore.BROWN_DWARF])
            if not self.orbit_track:
                self.orbit_track = 2
            if self.number_of_planets is None:
                self.number_of_planets = Dice.planets_roll(12, -7)
        elif roll == 18 or roll == 19:
            self.stars.append([StarCore.K_CLASS, StarCore.M_CLASS])
            if not self.orbit_track:
                self.orbit_track = 3
            if self.number_of_planets is None:
                self.number_of_planets = Dice.planets_roll(12, -8)
        else:
            self.stars.append([StarCore.K_CLASS, StarCore.BROWN_DWARF])
            if not self.orbit_track:
                self.orbit_track = 3
            if self.number_of_planets is None:
                self.number_of_planets = Dice.planets_roll(12, -7)
                
    def non_sequence_star(self):
        
        # According to second part of Table G59 in GMG
        roll = Dice.roll(20)
        if roll == 1:
            self.stars.append(StarCore.BLACK_HOLE)
            if not self.orbit_track:
                self.orbit_track = 5
            if self.number_of_planets is None:
                self.number_of_planets = Dice.planets_roll(12, -9)
        elif roll == 2 or roll == 3:
            self.stars.append(StarCore.NEUTRON)
            if not self.orbit_track:
                self.orbit_track = 5
            if self.number_of_planets is None:
                self.number_of_planets = Dice.planets_roll(12, -7)
        elif roll in range(4, 8):
            self.stars.append(StarCore.WHITE_DWARF)
            if not self.orbit_track:
                self.orbit_track = 5
            if self.number_of_planets is None:
                self.number_of_planets = Dice.planets_roll(12, -8)
        elif roll in range(8, 11):
            self.stars.append(StarCore.BLACK_DWARF)
            if not self.orbit_track:
                self.orbit_track = 5
            if self.number_of_planets is None:
                self.number_of_planets = Dice.planets_roll(8, -2)
        elif roll in range(11, 19):
            self.stars.append(StarCore.BROWN_DWARF)
            if not self.orbit_track:
                self.orbit_track = 3
            if self.number_of_planets is None:
                self.number_of_planets = Dice.planets_roll(8, -3)
        else:
            self.stars.append(StarCore.RED_SUPERGIANT)
            if not self.orbit_track:
                self.orbit_track = 4
            if self.number_of_planets is None:
                self.number_of_planets = Dice.planets_roll(8, -1)
                
    
class Planet(object):
    # Planet type
    ASTEROID_BELT = "Asteroid belt"
    COMET_BELT = "Comet belt"
    SUB_TERRAN = "Sub-terran"
    TERRAN = "Terran"
    SUPER_TERRAN = "Super terran"
    GAS_GIANT_LARGE = "Gas giant, large"
    GAS_GIANT_SMALL = "Gas giant, small"
    
    # Planet temperature
    TEMPERATE = "Temperate"
    HOT = "Hot"
    COLD = "Cold"
    
    # Orbit track possible distances as in Table G61 in GMG
    OT_1 = [0.7, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0]
    OT_2 = [0.3, 0.4, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0]
    OT_3 = [0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0]
    OT_4 = [1.5, 2.0, 3.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 0, 0]
    OT_5 = [0, 0, 0, 0, 0, 0, 1.5, 2.0, 3.0, 5.0, 10.0, 15.0, 20.0, 30.0, 40.0, 50.0]
    ORBIT_TRACKS = [OT_1, OT_2, OT_3, OT_4, OT_5]
    
    PLANET_TYPES_ON_TRACK = [(6, -3), (4, -1), (4, 0), (4, 3),
                             (4, 4), (6, 4), (6, 6, 2), (6, 6, 2),
                             (4, 10, 2), (4, 10, 2), (8, 10), (8, 10),
                             (6, 12), (6, 12), (8, 12), (8, 12)]
    
    def __init__(self, orbit_ring, parent_system=None):
        self.parent_system = parent_system
        self.planet_type = Planet.TERRAN
        self.temperature = Planet.TEMPERATE
        self.graph_type = [0, 0, 0, 0, 0]  # GRAPH type of planet according GMG
        self.moons = []
        self.orbit_ring = orbit_ring


class Moon(object):
    def __init__(self):
        self.parent_planet = None


if __name__ == '__main__':
    ss = StarSystem()
    ss.system_name = "Centauri"
    ss.print_chart()
