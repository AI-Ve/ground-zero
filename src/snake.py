from typing import List, Any
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN


class Snake:
    def __init__(self, height: int, width: int) -> None:
        self._body = [
            [height // 2, width // 2 + 1],
            [height // 2, width // 2],
            [height // 2, width // 2 - 1],
        ]
        self._direction = [0, 1]
        self._speed = 0
        self._score = 0

    @property
    def direction(self) -> Any:
        return self._direction
    
    @direction.setter
    def direction(self, key) -> None:
        if key == KEY_RIGHT:
            self._direction = [0, 1]
        elif key == KEY_LEFT:
            self._direction = [0, -1]
        elif key == KEY_UP:
            self._direction = [-1, 0]
        elif key == KEY_DOWN:
            self._direction = [1, 0]

    @property
    def body(self) -> List:
        return self._body

    @property
    def speed(self) -> int:
        return self._speed

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, x) -> None:
        self._score = x    


    def game_over(self, box: List) -> bool:
        if (
            self._body[0] in self._body[1:]
            or self._body[0][0] in [box[0][0], box[1][0]]
            or self._body[0][1] in [box[0][1], box[1][1]]
        ):
            return True
        else:
            return False
    
    
    def update(self) -> None:
        new_head = [self._body[0][0] + self._direction[0], self._body[0][1] + self._direction[1]]
        self._body.insert(0, new_head)

    
    def eat_food(self, food: List) -> bool:
        if self._body[0] == food:
            return True
        else:
            return False
