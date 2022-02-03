from helpers.TypesHelper import TColor, TTank


def tank(position: (float, float), velocity: float, size: int, name: str, color: TColor) -> TTank:
	x, y = position
	return {
		'x': x,
		'y': y,
		'velocity': velocity,
		'size': size,
		'name': name,
		'color': color
	}
