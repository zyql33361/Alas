from module.logger import logger
from module.map.map_base import CampaignMap
from module.map.map_grids import RoadGrids, SelectedGrids

from ..campaign_war_archives.campaign_base import CampaignBase
from .b1 import Config as ConfigBase

MAP = CampaignMap('B2')
MAP.shape = 'F8'
MAP.camera_data = ['C2', 'C6']
MAP.camera_data_spawn_point = ['C6']
MAP.map_data = """
    MB -- -- -- -- MB
    Me -- ++ ++ -- Me
    -- __ Me ++ -- --
    Me -- -- ME -- ME
    -- ME -- -- -- MM
    ++ ++ -- -- ME ++
    -- ++ -- ME -- --
    SP -- -- -- -- SP
"""
MAP.weight_data = """
    50 50 50 50 50 50
    50 50 50 50 50 50
    50 50 50 50 50 50
    50 50 50 50 50 50
    50 50 50 50 50 50
    50 50 50 50 50 50
    50 50 50 50 50 50
    50 50 50 50 50 50
"""
MAP.spawn_data = [
    {'battle': 0, 'enemy': 3},
    {'battle': 1, 'enemy': 2, 'mystery': 1},
    {'battle': 2, 'enemy': 2},
    {'battle': 3, 'enemy': 1},
    {'battle': 4, 'enemy': 2, 'boss': 1},
]
A1, B1, C1, D1, E1, F1, \
A2, B2, C2, D2, E2, F2, \
A3, B3, C3, D3, E3, F3, \
A4, B4, C4, D4, E4, F4, \
A5, B5, C5, D5, E5, F5, \
A6, B6, C6, D6, E6, F6, \
A7, B7, C7, D7, E7, F7, \
A8, B8, C8, D8, E8, F8, \
    = MAP.flatten()


class Config(ConfigBase):
    # ===== Start of generated config =====
    MAP_HAS_MAP_STORY = False
    MAP_HAS_FLEET_STEP = False
    MAP_HAS_AMBUSH = False
    MAP_HAS_MYSTERY = True
    # ===== End of generated config =====
    HOMO_EDGE_COLOR_RANGE = (0, 12)
    HOMO_EDGE_HOUGHLINES_THRESHOLD = 210
    MAP_SWIPE_MULTIPLY = (1.101, 1.122)
    MAP_SWIPE_MULTIPLY_MINITOUCH = (1.065, 1.085)
    MAP_SWIPE_MULTIPLY_MAATOUCH = (1.034, 1.053)
    HOMO_STORAGE = ((6, 5), [(211, 175), (782, 175), (158, 569), (800, 569)])
    MAP_ENSURE_EDGE_INSIGHT_CORNER = 'top'


class Campaign(CampaignBase):
    MAP = MAP
    ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'

    def battle_0(self):
        if self.clear_filter_enemy(self.ENEMY_FILTER, preserve=0):
            return True

        return self.battle_default()

    def battle_4(self):
        return self.clear_boss()
