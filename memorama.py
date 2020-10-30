from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
state2 = {'click': 0}
writer = Turtle(visible=False)
GuessedTiles = 0

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap, and detect if player has won."
    global GuessedTiles
    if GuessedTiles == 64:
        up()
        goto(-100, 200)
        color("blue")
        write("GANASTE", font = ("Arial", 10, "normal"))
        return
    spot = index(x, y)
    mark = state['mark']
   
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot        
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        GuessedTiles += 2
        print(GuessedTiles)

    state2['click'] += 1
    writer.undo()
    writer.write(state2['click'], font= ("Arial", 15, "normal"))#este imprime todos los demás

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 26, y + 10)
        color('black')
        write(tiles[mark], align = "center", font=('Arial', 20, 'normal'))

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(450, 480, 370, 0)
addshape(car)
hideturtle()
tracer(False)
writer.undo()
writer.goto(0, 200)
writer.color('blue')
writer.write(state2['click'], font= ("Arial", 15, "normal")) #este imprime el número de clicks inicial
onscreenclick(tap)
draw()
done()