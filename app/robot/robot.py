from app.command.enum import Direction


class Robot:
    def __init__(
            self,
            table_width: int,
            table_height: int,
            x_current=0,
            y_current=0,
            direction: Direction = Direction.NORTH,
    ):
        self.table_width = table_width
        self.table_height = table_height
        self.x_current = x_current
        self.y_current = y_current
        self.direction = direction

    @property
    def report(self):
        return f"{self.x_current},{self.y_current},{self.direction.name}"

    @property
    def is_inbounds(self):
        return ((0 <= self.x_current < self.table_width)
                and
                (0 <= self.y_current < self.table_height))

    @property
    def is_out_of_bounds(self):
        return not self.is_inbounds

    def __copy__(self):
        return Robot(
            self.table_width,
            self.table_height,
            self.x_current,
            self.y_current,
            self.direction,
        )
