from classes.GraphicClass import Graphic


class Tank:
    def __init__(self, graphic: Graphic, x: int, y: int, size: int, velocity: float, color: str):
        self.graphic = graphic
        self.dir_x = 0
        self.dir_y = 0
        self.dst_x = x
        self.dst_y = y
        self.pos_x = x
        self.pos_y = y
        self.size = size
        self.velocity = velocity
        self.color = color

    @property
    def status(self) -> str:
        if self.dir_x == 0 and self.dir_y == -1:
            return 'up'
        if self.dir_x == 0 and self.dir_y == 1:
            return 'down'
        if self.dir_x == -1 and self.dir_y == 0:
            return 'left'
        if self.dir_x == 1 and self.dir_y == 0:
            return 'right'
        return 'idle'

    def bound(self, width: int, height: int, x: float, y: float) -> bool:
        if x - self.size > 0 and x + self.size < width and y - self.size > 0 and y + self.size < height:
            return True
        return False

    def set_position(self, pos_x: float, pos_y: float):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def draw(self):
        self.graphic.draw_circle(self.size, (self.pos_x, self.pos_y), self.color, )
