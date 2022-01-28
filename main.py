from classes.GraphicClass import Graphic
from classes.InfoClass import Info
from classes.TankBotClass import TankBot
from classes.TankPlayerClass import TankPlayer
from helpers.MathHelper import Math
from helpers.PygameHelper import Pygame


speed = 1
size = 15
player_velocity = 3 * speed
bot_velocity = player_velocity / 3
running = True
graphic = Graphic(Pygame(800, 800, 'grey'))
info = Info(graphic)
plr_1 = TankPlayer(graphic, round(graphic.width / 2), round(graphic.height / 2), size, player_velocity, 'blue')
bot_1 = TankBot(graphic, round(graphic.width / 8), round(graphic.height / 2), size, bot_velocity, 'red')
bot_2 = TankBot(graphic, round(graphic.width / 2), round(graphic.height / 8), size, bot_velocity, 'red')


def render():
    info.player(plr_1)
    info.bot(bot_1)
    plr_1.draw()
    bot_1.draw()
    bot_2.draw()
    # graphic.draw_circle_alpha(20, (plr_1.dst_x, plr_1.dst_y), 'blue')
    graphic.draw_circle_alpha(size * 1.5, bot_1.dst, 'red')
    graphic.draw_circle_alpha(size * 1.5, bot_2.dst, 'red')


while running:
    graphic.clock.tick(60)
    graphic.clear()

    # Player
    # pos_x, pos_y = plr_1.get_position(True)
    pos_x, pos_y = plr_1.get_position(False)
    if plr_1.bound(graphic.width, graphic.height, pos_x, pos_y):
        plr_1.set_position(pos_x, pos_y)

    # Bot
    pos_bot_x, pos_bot_y = bot_1.get_position(plr_1)
    if Math.distance_scalar(bot_1.pos, plr_1.pos) > bot_1.size + plr_1.size:
        bot_1.set_position(pos_bot_x, pos_bot_y)
    pos_bot_x, pos_bot_y = bot_2.get_position(plr_1)
    if Math.distance_scalar(bot_2.pos, plr_1.pos) > bot_2.size + plr_1.size:
        bot_2.set_position(pos_bot_x, pos_bot_y)


    # Graphic
    render()
    graphic.render()
    running = graphic.running
