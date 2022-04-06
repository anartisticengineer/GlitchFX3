def pixels_generator(w: int, h: int):
    for i in range(w * h):
        yield divmod(i, w)


def x_generator(w: int):
    for x in range(w):
        yield x


def y_generator(h: int):
    for y in range(h):
        yield y
