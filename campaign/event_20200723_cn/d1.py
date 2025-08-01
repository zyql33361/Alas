from module.campaign.campaign_base import CampaignBase
from module.logger import logger
from module.map.map_base import CampaignMap
from module.map.map_grids import RoadGrids, SelectedGrids

MAP = CampaignMap('D1')
MAP.shape = 'I8'
MAP.camera_data = ['D2', 'D6', 'F2', 'F6']
MAP.camera_data_spawn_point = ['D2']
MAP.map_data = """
    ++ ++ ++ ME -- ME -- ++ --
    SP -- Me -- -- -- Me -- ME
    SP -- -- ++ MS -- -- -- --
    SP -- -- -- __ -- MS ++ ++
    ++ ++ Me -- -- -- Me ++ --
    ++ ++ -- -- MS -- -- ME --
    -- ME -- MB ++ MB -- -- ME
    -- ME -- ME ++ -- ME -- ++
"""
MAP.weight_data = """
    10 10 10 10 10 10 10 10 10
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
    {'battle': 2, 'enemy': 2},
    {'battle': 3, 'enemy': 1},
    {'battle': 4, 'enemy': 2},
    {'battle': 5, 'enemy': 1, 'boss': 1},
]
A1, B1, C1, D1, E1, F1, G1, H1, I1, \
A2, B2, C2, D2, E2, F2, G2, H2, I2, \
A3, B3, C3, D3, E3, F3, G3, H3, I3, \
A4, B4, C4, D4, E4, F4, G4, H4, I4, \
A5, B5, C5, D5, E5, F5, G5, H5, I5, \
A6, B6, C6, D6, E6, F6, G6, H6, I6, \
A7, B7, C7, D7, E7, F7, G7, H7, I7, \
A8, B8, C8, D8, E8, F8, G8, H8, I8, \
    = MAP.flatten()


class Config:
    SUBMARINE = 0

    # POOR_MAP_DATA = True
    MAP_HAS_AMBUSH = False
    MAP_HAS_FLEET_STEP = True
    MAP_HAS_MOVABLE_ENEMY = True
    MAP_HAS_SIREN = True
    MAP_HAS_DYNAMIC_RED_BORDER = False
    MAP_HAS_MAP_STORY = True
    MAP_SIREN_COUNT = 2
    DETECTION_BACKEND = 'homography'
    HOMO_STORAGE = ((6, 6), [(583.092, 82.574), (1247.528, 82.574), (564.74, 614.947), (1434.046, 614.947)])

    HOMO_EDGE_HOUGHLINES_THRESHOLD = 350
    MAP_SIREN_TEMPLATE = ['U101', 'U73', 'U552']
    MAP_SWIPE_MULTIPLY = (1.191, 1.213)
    MAP_SWIPE_MULTIPLY_MINITOUCH = (1.152, 1.173)
    MAP_SWIPE_MULTIPLY_MAATOUCH = (1.118, 1.138)


class Campaign(CampaignBase):
    MAP = MAP

    def battle_0(self):
        if self.clear_siren():
            return True
        if self.clear_enemy(scale=(1,)):
            return True
        if self.clear_enemy(scale=(2,), genre=['light', 'main', 'enemy', 'carrier']):
            return True
        if self.clear_enemy(genre=['light', 'main', 'enemy']):
            return True

        return self.battle_default()

    def battle_5(self):
        return self.fleet_boss.clear_boss()
