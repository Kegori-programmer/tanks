from classes.GraphicClass import Graphic
from classes.InfoClass import Info
from classes.TankBotClass import TankBot
from classes.TankPlayerClass import TankPlayer
from helpers.MathHelper import Math
from helpers.PygameHelper import Pygame


speed = 10
width = 1024
height = 768
tank_size = 15
player_velocity = speed
bot_velocity = player_velocity / 3
graphic = Graphic(Pygame(width, height, (233, 216, 166)))
info = Info(graphic)
plr_1 = TankPlayer(graphic, 'player_1', round(width / 2), round(height / 2), tank_size, player_velocity, (0, 95, 115))
plr_2 = TankPlayer(graphic, 'player_2', round(width / 5), round(height / 5), tank_size, player_velocity, (10, 147, 150))
bot_1 = TankBot(graphic, 'bot_1', round(width / 10), round(height / 2), tank_size, bot_velocity / 1.1, (155, 34, 38))
bot_2 = TankBot(graphic, 'bot_2', round(width / 2), round(height / 10), tank_size, bot_velocity / 1.2, (174, 32, 18))
bot_3 = TankBot(graphic, 'bot_3', round(width / 10), round(height / 10), tank_size, bot_velocity / 1.3, (187, 62, 3))
bot_4 = TankBot(graphic, 'bot_4', round(width / 2), round(height / 5), tank_size, bot_velocity / 1.4, (202, 103, 2))
bot_5 = TankBot(graphic, 'bot_5', round(width / 5), round(height / 2), tank_size, bot_velocity / 1.5, (238, 155, 0))
bots = [bot_1, bot_2, bot_3, bot_4, bot_5]


# bots = [bot_1, bot_2, bot_3]
# bots = [bot_1]


def render():
    info.player(plr_1)
    plr_1.draw()
    for i, bot in enumerate(bots):
        info.bot(i, bot, width)
        bot.draw()


def logic():
    # Player
    pos_x, pos_y = plr_1.get_position()
    # pos_x, pos_y = plr_1.get_position(True)
    if plr_1.bound(graphic.width, graphic.height, pos_x, pos_y):
        plr_1.set_position(pos_x, pos_y)

    # Bot
    for bot in bots:
        pos_bot_x, pos_bot_y = bot.get_position(plr_1)
        if Math.distance_scalar(bot.pos, plr_1.pos) > bot.size + plr_1.size:
            bot.set_position(pos_bot_x, pos_bot_y)
        else:
            exit()


def run():
    running = True
    while running:
        running = graphic.running
        graphic.clock.tick(60)
        graphic.clear()
        logic()
        render()
        graphic.render()


run()
