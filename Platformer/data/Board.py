from data.Environment import Environment
from data.Turret import Turret


class Board:
    def __init__(self, envgroup, decgroup, allgroup, dangroup, cell_size=16):
        self.cell_size = cell_size
        self.dangroup = dangroup
        self.envgroup = envgroup
        self.decgroup = decgroup
        self.allgroup = allgroup
        file = open('files/levels/yara_test_field.txt', 'rt')
        self.board = file.read().split('p')
        for i in range(0, len(self.board)):
            self.board[i] = self.board[i].split()
        file.close()
        self.width = len(self.board[0])
        self.height = len(self.board)
        self.left = 10
        self.top = 10

    def render(self, screen):
        objects = {}
        for x in range(self.width):
            for y in range(self.height):
                if self.board[y][x] == '0':
                    pass
                elif self.board[y][x] == '1':
                    sprite = Environment('images/blocks/environment/1_stone_surface.png',
                                         self.envgroup, self.allgroup, x, y,
                                         self.cell_size)
                elif self.board[y][x] == '2':
                    sprite = Environment('images/blocks/environment/2_stone.png',
                                         self.envgroup, self.allgroup, x, y,
                                         self.cell_size)
                elif self.board[y][x] == '3':
                    sprite = Environment('images/blocks/environment/3_stone_corner.png',
                                         self.envgroup, self.allgroup, x, y,
                                         self.cell_size)
                elif self.board[y][x] == '4':
                    sprite = Environment('images/blocks/decor/4_moss.png',
                                         self.decgroup, self.allgroup, x, y,
                                         self.cell_size)
                elif self.board[y][x] == '5':
                    sprite = Environment('images/blocks/environment/5_stone_surface_moss.png',
                                         self.envgroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '6':
                    sprite = Environment('images/blocks/decor/6_grass.png',
                                         self.decgroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '7':
                    sprite = Environment('images/blocks/environment/7_stone_surface_grass.png',
                                         self.envgroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '8':
                    sprite = Environment('images/blocks/environment/8_dead_bush.png',
                                         self.decgroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '9':
                    sprite = Environment('images/blocks/environment/9_dirt.png',
                                         self.envgroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '10':
                    sprite = Environment('images/blocks/danger/10_spikes.png',
                                         self.dangroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '11':
                    sprite = Environment('images/blocks/decor/11_lian_1.png',
                                         self.decgroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '12':
                    sprite = Environment('images/blocks/decor/12_lian_2.png',
                                         self.decgroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '13':
                    sprite = Environment('images/blocks/decor/13_lian_3.png',
                                         self.decgroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '14':
                    sprite = Environment('images/blocks/danger/14_small_spike.png',
                                         self.dangroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '15':
                    sprite = Environment('images/blocks/special/15_jump_pad.png',
                                         self.jumpadgr, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '-1':
                    sprite = Environment('images/turret/turret_base.png',
                                         self.dangroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '-2':
                    sprite = Turret('images/turret/turret_cannon.png', self.dangroup, self.allgroup, x, y, self.cell_size)
                    if 'turrets' in objects:
                        objects['turrets'].append(sprite)
                    else:
                        objects['turrets'] = [sprite]
        return objects
