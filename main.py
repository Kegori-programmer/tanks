from classes.GraphicClass import Graphic
from classes.InfoClass import Info
from classes.TankBotClass import TankBot
from classes.TankPlayerClass import TankPlayer
from helpers.PygameHelper import Pygame


size = 15
velocity = 5
running = True
graphic = Graphic(Pygame(800, 800, 'grey'))
info = Info(graphic)
plr_1 = TankPlayer(graphic, round(graphic.width / 2), round(graphic.height / 2), size, velocity, 'blue')
bot_1 = TankBot(graphic, round(graphic.width / 8), round(graphic.height / 2), size, velocity / 3, 'red')


def render():
    graphic.clear()
    info.player(plr_1)
    info.bot(bot_1)
    plr_1.draw()
    bot_1.draw()
    graphic.draw_circle_alpha(20, (bot_1.dst_x, bot_1.dst_y), 'red')
    graphic.render()


while running:
    graphic.clock.tick(60)
    running = graphic.running
    # Player
    # pos_x, pos_y = plr_1.get_position(True)
    pos_x, pos_y = plr_1.get_position(False)
    if plr_1.bound(graphic.width, graphic.height, pos_x, pos_y):
        plr_1.set_position(pos_x, pos_y)
    # Bot
    pos_bot_x, pos_bot_y = bot_1.get_position(plr_1)
    bot_1.set_position(pos_bot_x, pos_bot_y)
    # Graphic
    render()
