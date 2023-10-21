# Guardado con el nombre de: 04_DrawEvilHangMan.py
import math
import tkinter

class Rectangle(object):
    def __init__(self, x, y, w, h, a):
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h
        self.__angle = a

    @property
    def angle(self) -> float:
        return self.__angle

    @angle.setter
    def angle(self, value: float):
        if value > 360 or value < 0:
            self.__angle = value % 360
        else:
            self.__angle = value

    @property
    def botleft(self) -> tuple:
        return self.__x, self.__y

    @property
    def botright(self) -> tuple:
        return Rectangle.rotate(
            self.__x,
            self.__y,
            self.__w + self.__x,
            self.__y,
            self.__angle
        )

    @property
    def topleft(self) -> tuple:
        return Rectangle.rotate(
            self.__x,
            self.__y,
            self.__x,
            self.__h + self.__y,
            self.__angle
        )

    @property
    def topright(self) -> tuple:
        return Rectangle.rotate(
            self.__x,
            self.__y,
            self.__w + self.__x,
            self.__h + self.__y,
            self.__angle
        )

    @staticmethod
    def rotate(bx, by, x, y, a) -> tuple:
        nx = x - bx
        ny = y - by
        s = math.sin(math.radians(a))
        c = math.cos(math.radians(a))
        return (
            (nx * c - ny * s) + bx,
            (nx * s + ny * c) + by
        )





def main():
    master = tkinter.Tk("Prueba")
    canvas_width = 640
    canvas_height = 480
    w = tkinter.Canvas(master, width=canvas_width, height=canvas_height)
    w.pack()
    r = Rectangle(200, 200, 100, 50, 0)
    w.create_polygon([*r.botleft, *r.botright, *r.topright, *r.topleft], outline="#C3C3C3", fill="yellow", width=3)
    r.angle = 45
    w.create_polygon([*r.botleft, *r.botright, *r.topright, *r.topleft], outline="#C3C3C3", fill="#A2A2A2", width=3)
    r.angle = -75
    w.create_polygon([*r.botleft, *r.botright, *r.topright, *r.topleft], outline="#C3C3C3", fill="#C212B2", width=3)
    tkinter.mainloop()
    print("Fin del Programa")

if __name__ == '__main__':
    main()
print("Fin del Programa ---")