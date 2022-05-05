from classes.GraphicClass import Graphic
from classes.InfoClass import Info
from helpers.GeneratorHelper import GenBot, GenPlr
from helpers.PygameHelper import Pygame

# width, height = 1024, 768
width, height = 1280, 1024
size, velocity = 15, 2
graphic = Graphic(Pygame(width, height, (233, 216, 166)))
info = Info(graphic)
gen_plr, gen_bot = GenPlr(graphic, width, height, velocity, size), GenBot(graphic, width, height, velocity / 1.5, size)
plr1 = gen_plr.plr1
bots = gen_bot.bots


def render():
	info.player(plr1)
	plr1.draw()
	for i, bot in enumerate(bots):
		info.bot(i, bot, width)
		bot.draw()


def logic():
	# Player
	pos_plr = plr1.get_position()
	if plr1.bound(graphic.width, graphic.height, pos_plr):
		plr1.set_position(pos_plr)
	# Bots
	for bot in bots:
		pos_bot = bot.get_position(plr1)
		bot.set_position(pos_bot)


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
