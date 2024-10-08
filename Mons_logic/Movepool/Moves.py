import pygame as pg
import sys
from enum import Enum

class Attack(Enum):
    def Physical(self):
        Earthquake = {
            "name": "Earthquake",
            "type": "Ground",
            "description": [
                ""
                ],
            "power": 100,
            "accuracy": 1,
            "usage": 15,
            "effect": []#hits all targets on the field except Flying types
        }
        Chop = {
            "name": "Chop",
            "type": "Fighting",
            "description": [
                ""
                ],
            "power": 75,
            "accuracy": 85,
            "usage": 15,
            
        }
        Wing_Strike = {
            "name": "Wing Strike",
            "type": "Flying",
            "description": [
                ""
                ],
            "power": 70,
            "accuracy": 90,
            "usage": 15,
        
        }
        Leech = {
            "name": "Leech",
            "type": "Bug",
            "description": [
                ""
                ],
            "power": 55,
            "accuracy": 85,
            "usage": 20,
            "effect": []#restores 1/8 the damage inflicted 
        }
        Bite = {
            "name": "Bite",
            "type": "Dark",
            "description": [
                ""
                ],
            "power": 65,
            "accuracy": 90,
            "usage": 15,
            "effect": []#20% chance to make the target flinch
        
        }
        Water_Stride = {
            "name": "Water Stride",
            "type": "Water",
            "description": [
                "The user charges at the foe with enough force to walk over water."
                ],
            "power": 95,
            "accuracy": 90,
            "usage": 15,
        
        }
        Draco_Slash = {
            "name": "Draco Slash",
            "type": "Dragon",
            "description": [
                ""
                ],
            "power": 95,
            "accuracy": 90,
            "usage": 15,
        
        }
        Flame_Rush = {
            "name": "Flame Rush",
            "type": "Fire",
            "description": [
                ""
                ],
            "power": 100,
            "accuracy": 85,
            "usage": 10,
            "effect": []#30% chance to inlfict a Burn
        }
        Frost_Rush = {
            "name": "Frost Rush",
            "type": "Ice",
            "description": [
                ""
                ],
            "power": 100,
            "accuracy": 85,
            "usage": 10,
            "effect": []#30% chance to Freeze the target
        }
        Avalanche = {
            "name": "Avalanche",
            "type": ["Rock" or "Ice"],
            "description": [
                "Large boulders are thrown at the foe. If used on icy terrain, snow is used instead. May cause flinch."
                ],
            "power": 95,
            "accuracy": 90,
            "usage": 15,
            "effect": []#changes type depanding on the terrain. 30% chance to make the target flinch
        }
        Veno_Fang = {
            "name": "Veno Fang",
            "type": "Poison",
            "description": [
                ""
                ],
            "power": 70,
            "accuracy": 90,
            "usage": 15,
            "effect": []#15% chance to Poison the target
    }
        Stone_Blade = {
            "name": "Stone Blade",
            "type": "Rock",
            "description": [
                ""
                ],
            "power": 85,
            "accuracy": 80,
            "usage": 15,
            
        }
        Frost_Blade = {
            "name": "Frost Blade",
            "type": "Ice",
            "description": [
                ""
                ],
            "power": 85,
            "accuracy": 80,
            "usage": 15,
            "effect": []#15% chance to freeze the target
        }
        Vine_Lash = {
            "name": "Vine Lash",
            "type": "Grass",
            "description": [
                ""
                ],
            "power": 75,
            "accuracy": 90,
            "usage": 20,
            "effect": []#hits the target within a certain range
    }
        Headbutt = {
            "name": "Headbutt",
            "type": "Normal",
            "description": [
            ""
            ],
            "power": 85,
            "accuracy": 80,
            "usage": 20,
            "effect": []#25% chance to make the target flinch
    }
        Leaf_Scythe = {
            "name": "Leaf Scythe",
            "type": "Grass",
            "description": [
                ""
                ],
            "power": 90,
            "accuracy": 85,
            "usage": 15
        }
        Ice_Fist = {
            "name": "Ice Fist",
            "type": "Ice",
            "description": [
                ""
                ],
            "power": 80,
            "accuracy": 80,
            "usage": 15,
            "effect": []#20% chance to Freeze the target
        }
        Scratch = {
            "name": "Scratch",
            "type": "Normal",
            "description": [
                ""
                ],
            "power": 40,
            "accuracy": 80,
            "usage": 20
        }
        Tackle = {
            "name": "Tackle",
            "type": "Normal",
            "description": [
                ""
                ],
            "power": 40,
            "accuracy": 80,
            "usage": 20
        }
        Multi_Swipe = {
            "name": "Multi Scratch",
            "type": "Normal",
            "description": [
                ""
                ],
            "power": 20,
            "accuracy": 80,
            "usage": 25,
            "effect": []#may hit the target up to 6 times
        }
        Shatter = {
            "name": "Shatter",
            "type": "Fighting",
            "description": ,
            "power": 80,
            "accuracy": 80,
            "usage": 15,
            "effect": #destroys special barriers and cancels their effects
        }
        Dragon_Fist = {
            "name": "Dragon Fist",
            "type": "Dragon",
            "description": ,
            "power": 75,
            "accuracy": 80,
            "usage": 20,
        }
        Meteor_Strike = {
            "name": "Metor Strike",
            "type": "Rock",
            "description": ,
            "power": 95,
            "accuracy": 95,
            "usage": 15,
            "effect": #the closer the target to the impact, the greater the damage, user takes damage too
        }
        Metal_Blade = {
            "name": "Metal Blade",
            "type": "Steel",
            "description": ,
            "power": 85,
            "accuracy": 80,
            "usage": 15,
        }
        Mystic_Blade = {
            "name": "Mystic Balde",
            "type": "Fairy",
            "description": ,
            "power": 85,
            "accuracy": 80,
            "usage": 15,
        }
        Volt_Strike = {
            "name": "Volt Strike",
            "type": "Electric",
            "description": ,
            "power": 80,
            "accuracy": 85,
            "usage": 15,
            "effect": # the user takes damage, 10% chance to Paralyze
        }
        Electro_Blade = {
            "name": "Electro Blade",
            "type": "Electric",
            "description": ,
            "power": 85,
            "accuracy": 80,
            "usage": 15,
            "effect": # 10% chance to Paralyze
        }
        Electro_Wing = {
            "name": "Electro Wing",
            "type": "Electric",
            "description": ,
            "power": 75,
            "accuracy": 85,
            "usage": 15,
            "effect": # 15% chance to flinch or Paralyze
        }
        Necro_Blade = {
            "name": "Necro Blade",
            "type": "Dark",
            "description": ,
            "power": 85,
            "accuracy": 80,
            "usage": 15,
        }
        Errie_Blade = {
            "name": "Errie Blade",
            "type": "Ghost",
            "description": ,
            "power": 85,
            "accuracy": 80,
            "usage": 15,
        }
        Whirl_Blade = {
            "name": "Whirl Blade",
            "type": "Flying",
            "description": ,
            "power": 85,
            "accuracy": 95,
            "usage": 15,
            "effect": # the user spreads it's arms wide open and starts spinning around. hits in a range of 1 block around the user
        }
        Magnetic_Fist = {
            "name": "Magnetic Fist",
            "type": "Steel",
            "description": ,
            "power": 85,
            "accuracy": 85,
            "usage": 15,
            "effect": # when close enough to Steel types it won't miss
        }
        Moon_Strike = {
            "name": "Moon Strike",
            "type": ["Ice" or "Dark"],
            "description": [
                "Hits the foe with enough force to make a crater on the moon. The user takes damage."
                ],
            "power": 120,
            "accuracy": 95,
            "usage": 7,
        }

    def Special(self):
        Fright= {
            "name": "Fright",
            "type": "Ghost",
            "description": ,
            "power": 50,
            "accuracy": 1,
            "usage": 15,
            "effect": #25% chance to make the target flinch
        }
        Scorch = {
            "name": "Scorch",
            "type": "Fire",
            "description": ,
            "power": 50,
            "accuracy": 80,
            "usage": 20,
            "effect": #15% to inflict a Burn, hits in a certain range
            
        }
        Veno_Drop = {
            "name": "Veno Drop",
            "type": "Poison",
            "description": "",
            "power": 90,
            "accuracy": 85,
            "usage": 15,
            "effect": #20% chance to Poison the target
        }
        Flame_Gulf = {
            "name": "Falme Gulf",
            "type": "Fire",
            "description": ,
            "power": 95,
            "accuracy": 90,
            "usage": 15,
            "effect": #Hits in a certian range of the field, 18% chance to Burn the target. 
        }
        Cyclone = {
            "name": "Cyclone",
            "type": "Flying",
            "description": ,
            "power": 100,
            "accuracy": 1,
            "usage": 10,
            "effect": #hits everything on the field except the user, 40% chance to cuase Confusion
        }
        Twister = {
            "name": "Twister",
            "type": "Dragon",
            "description": ,
            "power": 70,
            "accuracy": 90,
            "usage": 15,
            "effect": # draws the nearest target in the attack, 20% chance of Confusion
        }
        Aurora_Blast = {
            "name": "Aurora Blast",
            "type": "Ice",
            "description": ,
            "power": 75,
            "accuracy": 90,
            "usage": 15,
            "effect": #15% chance to lower the targets Special Attack. hits in a certain range.
        }
        Ice_Ray = {
            "name": "Ice Ray",
            "type": "Ice",
            "description": ,
            "power": 90,
            "accuracy": 90,
            "usage": 10,
            "effect": #freezes the target, hits in a certain range
        }
        Draco_Breath = {
            "name": "Draco Breath",
            "type": "Dragon",
            "description": ,
            "power": 90,
            "accuracy": 90,
            "usage": 15,
        }
        Stellarium = {
            "name": "Stellarium",
            "type": "Normal",
            "description": ,
            "power": 75,
            "accuracy": 1,
            "usage": 15,
            
        }
        Mystic_Shine = {
            "name": "Mystic Shine",
            "type": "Fairy",
            "description": ,
            "power": 90,
            "accuracy": 1,
            "usage": 10,
            "effect": #10% chance to lowrer the targets accuracy
        }
        Glacial_Wind = {
            "name": "Galcial Wind",
            "type": "Ice",
            "description": ,
            "power": 50,
            "accuracy": 90,
            "usage": 20,
            "effect": #reduces the targets speed 10%, 5% chance of Freeze. hits in certain area except if used on icy fields
        }
        Heat_Wave = {
            "name": " Heat Wave",
            "type": "Fire",
            "description": ,
            "power": 70,
            "accuracy": 90,
            "usage": 20,
            "effect": # hits the targwt on a certain range. 10% chance to cause a Burn
        }
        Thunder_Storm = {
            "name": "Thunder Storm",
            "type": "Electric",
            "description": ,
            "power": 100,
            "accuracy": 90,
            "usage": 10,
            "effect": # if raining accuracy = 1, 15% chance to Paralyze
        }
        Kinnesis = {
            "name": "Kinnesis",
            "type": "Psychic",
            "description": ,
            "power": 90,
            "accuracy": 95,
            "usage": 10,
            "effect": # grabs the target at a certain range 
        }
        Jolt = {
            "name": "Jolt",
            "type": "Electric",
            "description": ,
            "power": 45,
            "accuracy": 90,
            "usage": 25,
            "effect": # hits in a certain range. 15% chance to Paralyze
        }
        Electro_Ball = {
            "name": "Electro Ball",
            "type": "Electric",
            "description": ,
            "power": 75,
            "accuracy": 90,
            "usage": 20,
            "effect": # hits in a certain range
        }
        Gifted_Mind = {
            "name": "Gifted Mind",
            "type": "Psychic",
            "description": ,
            "power": 110,
            "accuracy": 95,
            "usage": 7,
            "efect": # when used against Steel types it is super effective
        }
        EM_Storm = {
            "name": " EM Storm",
            "type": [],# adjusts to the users type, Electric/Steel
            "description": ,
            "power": 120,
            "accuracy": 1,
            "usage": 5,
            "effect": []# effect varies to the users type
        }
        EMP_Cannon = {
            "name": " EMP Cannon",
            "type": "Steel",
            "description": ,
            "power": 110,
            "accuracy": 1,
            "usage": 7,
            "effect": []# locks the targets tile to ensure the hit
        }
        Sonic_Palm = {
            "name": "Sonic Palm",
            "type": "Fighting",
            "description": ,
            "power": 60,
            "accuracy": 1,
            "usage": 20,
            "effect": []# 10% chance to cuase Confusion
        }
        Lunar_Beam = {
            "name": "Lunar Beam",
            "type": "Ice",
            "description": [
                "The user attacks the foe with the Moon's energy to strike the foe with an incredible burst of light."
                ],
            "power": 110,
            "accuracy": 1,
            "usage": 8,
            "effect": [] #Takes time to luanch the attack. 30s
        }

class Field(Enum):
    def terrain(self):
        Over_Grow = {
            "name": "Over Grow",
            "type": "Grass",
            "description": ,
            "usage": 5,
            "effect": # creates an ancient forest terrain, boosts Grass, Bug, Beast and Fairy types moves 13%
            }
        Blizzard = {
            "name": "Blizzard",
            "type": "Ice",
            "description": ,
            "usage": 5,
            "effect": # summons a hailstorm that creates en icy field. boosts Ice type moves 13%
            }
        Hurracaine = {
            "name": "Hurracaine",
            "type": "Water",
            "description": ,
            "usage": 5,
            "effect": # summons a hurricane. bossts Water, Electric and Flying moves 13%
            }
        Oasis = {
            "name": "Oasis",
            "type": "Psychic",
            "description": ,
            "usage": 5,
            "effect": # creates a peaceful place for meditaion. boosts Psychic and Fighting moves 13%
            }
        Errie_Mist = {
            "name": "Errie Mist",
            "type": "Ghost",
            "description": ,
            "usage": 5,
            "effect": # summons a mysterious fog that covers all. boosts Ghost and Dark type moves 13%
            }
        Mine = {
            "name": "Mine",
            "type": "Rock",
            "description": ,
            "usage": 5,
            "effect": # creates a mining site. boosts Steel and Rock type moves 13%
            }
        Harsh_Land = {
            "name": "Harsh Land",
            "type": "Fire",
            "description": ,
            "usage": 5,
            "effect": # creates a desolate land. boosts Fire, Ground and Dragon type moves 13%.
            }
        Swamps = {
            "name": "Swamps",
            "type": "Poison",
            "description": ,
            "usage": 5,
            "effect": # creates a swampy land. boosts Poison type moves 13%
            }
        Obstaculum = {
            "name": "Obstaculum",
            "type": "Normal",
            "description": ,
            "usage": 5,
            "effect": # let's the user adapt to the terrain. boosts users Normal type moves 13% and speed 10%
            }

class Defense(Enum):
    def shield(self):
        Protect = {
            "name": "Protect",
            "type": "Normal",
            "description": [
                "Creates an energy field to protect the user from attaks and effects"],
            "usage": 10,
            "effect": []#negates damage, stat reduction or status inflection.
            
        }
        Aura_Veil = {
            "name": "Aura Veil",
            "type": "Fairy",
            "description": ,
            "usage": 20,
            "effect": []#protects the user from stat and status conditions
        }

class Stats(Enum):
    def increase(self):
        Howl = {
            "name": "Howl",
            "type": "Beast",
            "description": ,
            "usage": 20,
            "effect": []#raises the users attack 10%
            }
        Reflect = {
            "name": "Reflect",
            "type": "Psychic",
            "description": [
                ""
                ],
            "usage": 20,
            "effect": []#raises the users defense 10%
            }
        Light_Wall = {
            "name": "Light Wall",
            "type": ,
            "description": ,
            "usage": 20,
            "effect": []#raises the users Special Defense
        }
        Fairy_Light = {
            "name": "Fairy Light",
            "type": "Fairy",
            "description": ,
            "usage": 15,
            "effect": []# heightens the users Special attack and Special Defense 10%. lowers the enemy accuracy 5%
        }

    def lower(self):
        Growl = {
            "name": "Growl",
            "type": ,
            "description": ,
            "accuracy": 95,
            "usage": 20,
            "effect": #reduces the targets attack 10%
            }
        Sand_Hurl = {
            "name": "Sand Hurl",
            "type": "Ground",
            "description": ,
            "accuracy": 90,
            "usage": 20,
            "effect": #lowers the targets accuracy 10%, hits in a certain range
            
        }
        Glance = {
            "name": "Glance",
            "type": ,
            "description": ,
            "accuracy": 90,
            "usage": 20,
            "effect": #reduces the foes Defense 10%
        }

class Status(Enum):
    Burn = {
        "name": "Burn",
        "effect": []#deals damage every 30s, reduces attack and may cause flinch(if flinched, 15s deley to recover)
    }
    Freeze = {
        "name": "Freeze",
        "effect": []#freezes the target for 50s, after defrost target's speed falls 30s
    }
    Paralyze = {
        "name": "Paralyze",
        "effect": []#paralizes the target, low chance to attack. Speed falls 10%
    }
    Poison = {
        "name": "Poison",
        "effect": []#Target losess HP every 10s in battle. Outside battle losess HP every 6 steps.
    }
    Confusion = {
        "name": "Confused",
        "effect": []#swaps the movementent keys for 60s, 50% chance to hit itself
    }
    Sleep = {
        "name": "Sleep",
        "effect": []#makes the target fall into a deep sleep, 10% to awake while in battle. 90s to wake up after battle.
    }
    

        "name": "",
        "type": ,
        "description": ,
        "power": ,
        "accuracy": ,
        "usage": ,

        "name": "",
        "type": ,
        "description": ,
        "accuracy": ,
        "usage": ,
        "effect":