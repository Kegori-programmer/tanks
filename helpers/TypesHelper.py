from typing import TypedDict, Tuple, Union

TColor = Union[Tuple[int, int, int], str]

TTank = TypedDict('TTank', {
	'x': float,
	'y': float,
	'velocity': float,
	'size': int,
	'name': str,
	'color': TColor,
})
