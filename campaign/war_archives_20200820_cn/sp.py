from module.logger import logger
from module.map.map_base import CampaignMap
from module.map.map_grids import RoadGrids, SelectedGrids

from ..campaign_war_archives.campaign_base import CampaignBase

MAP = CampaignMap('SP')
MAP.shape = 'I7'
MAP.camera_data = ['D2', 'D5', 'F2', 'F5']
MAP.camera_data_spawn_point = ['D2']
MAP.map_data = """
    -- MS ++ SP -- SP -- -- ME
    -- -- Me -- -- -- ME -- --
    ++ ++ -- MS Me -- ++ ++ --
    ++ ++ Me -- __ -- ME ++ MS
    -- -- ME -- -- ME -- ME --
    -- Me -- ++ -- ++ ME -- --
    -- -- Me ++ MB ++ -- ME --
"""
MAP.weight_data = """
    10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10
"""
MAP.spawn_data = [
    {'battle': 0, 'enemy': 2, 'siren': 2},
    {'battle': 1, 'enemy': 1},
    {'battle': 2, 'enemy': 2, 'siren': 1},
    {'battle': 3, 'enemy': 1},
    {'battle': 4, 'enemy': 2},
    {'battle': 5, 'enemy': 1},
    {'battle': 6},
    {'battle': 7, 'boss': 1},
]
A1, B1, C1, D1, E1, F1, G1, H1, I1, \
A2, B2, C2, D2, E2, F2, G2, H2, I2, \
A3, B3, C3, D3, E3, F3, G3, H3, I3, \
A4, B4, C4, D4, E4, F4, G4, H4, I4, \
A5, B5, C5, D5, E5, F5, G5, H5, I5, \
A6, B6, C6, D6, E6, F6, G6, H6, I6, \
A7, B7, C7, D7, E7, F7, G7, H7, I7, \
    = MAP.flatten()


class Config:
    MAP_SIREN_TEMPLATE = ['CL', 'CA', 'BB', 'CV']
    MOVABLE_ENEMY_TURN = (3,)
    MAP_HAS_SIREN = True
    MAP_HAS_MAP_STORY = False
    MAP_HAS_FLEET_STEP = True

    MAP_HAS_AMBUSH = False
    MAP_HAS_MOVABLE_ENEMY = True
    MAP_SWIPE_MULTIPLY = (1.175, 1.197)
    MAP_SWIPE_MULTIPLY_MINITOUCH = (1.137, 1.158)
    MAP_SWIPE_MULTIPLY_MAATOUCH = (1.103, 1.123)
    STAR_REQUIRE_3 = 0  # SP map don't need to clear all enemies.


class Campaign(CampaignBase):
    MAP = MAP

    def battle_0(self):
        if self.fleet_2_protect():
            return True

        if self.clear_siren():
            return True
        if self.clear_enemy(scale=(3,)):
            return True

        return self.battle_default()

    def battle_5(self):
        if self.clear_enemy(scale=(1,)):
            return True
        if self.clear_enemy(scale=(2,)):
            return True

        return self.battle_default()

    def battle_7(self):
        return self.fleet_boss.clear_boss()
