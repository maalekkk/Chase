from parse_args import cls_logger, func_logger


@cls_logger(func_logger)
class Animal:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"({self.x}, {self.y}, {self.move_dist})")

    @property
    def coords(self):
        return [self.x, self.y]

    def move(self):
        pass
