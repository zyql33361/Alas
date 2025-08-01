from .campaign_base import CampaignBase
from module.map.map_base import CampaignMap
from module.map.map_grids import SelectedGrids, RoadGrids
from module.logger import logger

MAP = CampaignMap('ESP')
MAP.shape = 'E10'
MAP.camera_data = ['B5', 'B6']
MAP.camera_data_spawn_point = ['B8']
MAP.map_data = """
    -- -- -- -- --
    ++ ++ -- ++ ++
    ++ ++ MB ++ ++
    -- ME -- ME --
    ME -- -- -- ME
    ++ ++ __ ++ ++
    ++ MS -- MS ++
    ++ -- MS -- ++
    -- -- -- -- --
    -- SP -- SP --
"""
MAP.weight_data = """
    50 50 50 50 50
    50 50 50 50 50
    50 50 50 50 50
    50 50 50 50 50
    50 50 50 50 50
    50 50 50 50 50
    50 50 50 50 50
    50 50 50 50 50
    50 50 50 50 50
    50 50 50 50 50
"""
MAP.spawn_data = [
    {'battle': 0, 'enemy': 4, 'siren': 3},
    {'battle': 1},
    {'battle': 2},
    {'battle': 3},
    {'battle': 4},
    {'battle': 5},
    {'battle': 6},
    {'battle': 7, 'boss': 1},
]
A1, B1, C1, D1, E1, \
A2, B2, C2, D2, E2, \
A3, B3, C3, D3, E3, \
A4, B4, C4, D4, E4, \
A5, B5, C5, D5, E5, \
A6, B6, C6, D6, E6, \
A7, B7, C7, D7, E7, \
A8, B8, C8, D8, E8, \
A9, B9, C9, D9, E9, \
A10, B10, C10, D10, E10, \
    = MAP.flatten()


class Config:
    # ===== Start of generated config =====
    MAP_SIREN_TEMPLATE = ['UlrichVonHutten', 'PeterStrasser']
    MOVABLE_ENEMY_TURN = (2,)
    MAP_HAS_SIREN = True
    MAP_HAS_MOVABLE_ENEMY = True
    MAP_HAS_MAP_STORY = False
    MAP_HAS_FLEET_STEP = True
    MAP_HAS_AMBUSH = True
    MAP_HAS_MYSTERY = False
    STAR_REQUIRE_1 = 0
    STAR_REQUIRE_2 = 0
    STAR_REQUIRE_3 = 0
    # ===== End of generated config =====

    INTERNAL_LINES_HOUGHLINES_THRESHOLD = 35
    EDGE_LINES_HOUGHLINES_THRESHOLD = 35
    MAP_ENSURE_EDGE_INSIGHT_CORNER = 'bottom'
    MAP_SWIPE_MULTIPLY = (0.960, 0.978)
    MAP_SWIPE_MULTIPLY_MINITOUCH = (0.928, 0.946)
    MAP_SWIPE_MULTIPLY_MAATOUCH = (0.901, 0.918)


class Campaign(CampaignBase):
    MAP = MAP
    ENEMY_FILTER = '1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C'

    def battle_0(self):
        if self.clear_siren():
            return True
        if self.clear_filter_enemy(self.ENEMY_FILTER, preserve=2):
            return True

        return self.battle_default()

    def battle_5(self):
        if self.clear_siren():
            return True
        if self.clear_filter_enemy(self.ENEMY_FILTER, preserve=0):
            return True

        return self.battle_default()

    def battle_7(self):
        return self.fleet_boss.clear_boss()
