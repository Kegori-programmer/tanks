from classes.GraphicClass import Graphic
from classes.InfoClass import Info
from classes.TankBotClass import TankBot
from classes.TankPlayerClass import TankPlayer
from helpers.PygameHelper import Pygame
from tanks import tank

width, height = 1024, 768
# width, height = 1280, 1024
size, velocity = 15, 5
x, y = width / 2, height / 2
player_velocity = velocity / 1.5
bot_velocity = player_velocity / 2.5
graphic = Graphic(Pygame(width, height, (233, 216, 166)))
info = Info(graphic)
plr_1 = TankPlayer(graphic, tank((x - width / 4, y), player_velocity, size, 'plr_1', (0, 0, 0)), False)
# plr_2 = TankPlayer(graphic, tank((x+width / 4, y), velocity, size, 'plr_2', (0, 18, 25)))
bot_1 = TankBot(graphic, tank((x - width / 3.5, y - height / 2.5), bot_velocity, size, 'bot_1', (155, 34, 38)))
bot_2 = TankBot(graphic, tank((x + width / 2.5, y - height / 2.5), bot_velocity / 1.5, size, 'bot_2', (187, 62, 3)))
bot_3 = TankBot(graphic, tank((x - width / 2.5, y + height / 2.5), bot_velocity / 2, size, 'bot_3', (238, 155, 0)))
bot_4 = TankBot(graphic, tank((x + width / 3.5, y + height / 2.5), bot_velocity / 2.5, size, 'bot_4', (148, 210, 189)))
bot_5 = TankBot(graphic, tank((x, y - height / 2.5), bot_velocity / 3, size, 'bot_5', (0, 95, 115)))
# bots = [bot_1]
# bots = [bot_1, bot_2]
bots = [bot_1, bot_2, bot_3]
# bots = [bot_1, bot_2, bot_3, bot_4]
# bots = [bot_1, bot_2, bot_3, bot_4, bot_5]


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
		bot.set_position(pos_bot_x, pos_bot_y)


# if Math.distance_scalar(bot.pos, plr_1.pos) > bot.size + plr_1.size:
# bot.set_position(pos_bot_x, pos_bot_y)
# else:
#     exit()


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
