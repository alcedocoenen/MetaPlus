import turtle

s = turtle.getscreen()
t = turtle.Turtle()
turtle.title("Plus-Minus Square")
speed = 0
t.speed(speed)
t.home()

# draw square
def draw_square(side, t, offset=(0,0)):
    # side = 200
    t.goto(offset)
    t.penup()
    # t.home()
    t.goto(offset)
    t.pendown()
    t.fd(side)
    t.lt(90)
    t.fd(side)
    t.lt(90)
    t.fd(side)
    t.lt(90)
    t.fd(side)
    t.lt(90)

# wait

# circle in the middle
def draw_circle(radius, side, t, offset=(0,0)):
    # diameter = 30
    t.speed(speed)
    t.penup()
    t.goto(offset)
    t.goto(offset[0]+side/2, offset[1]+side/2-radius)
    t.pendown()
    t.circle(radius)
    t.penup()
    t.goto(offset)

def draw_centralsound1(radius, side, t, offset=(0,0)):
    # draw_circle(radius,side)
    t.penup()
    t.goto(offset)
    t.goto(offset[0] + (side/2)-(side/4), offset[1] + side/2)
    t.pendown()
    t.fd(side/2)
    t.penup()
    t.goto(offset)

def draw_dashedline(len, t):
    # dash = len/6
    n = int(len/8)
    l1 = 5
    l2 = 3
    for i in range(n):
        t.forward(l1)
        t.penup()
        t.forward(l2)
        t.pendown()
    t.forward(l2)

def draw_centralsound2(radius, side, t, offset=(0,0)):
    # draw_circle(radius,side)
    t.penup()
    t.goto(offset)
    t.goto(offset[0] + (side/2)-(side/4), offset[1] + side/2)
    t.pendown()
    draw_dashedline(side/2, t)
    t.penup()
    t.goto(offset)

def draw_centralsound4(radius, side, t, offset=(0,0)):
    len_diagonal = (2 * (radius ** 2)) ** 0.5
    t.penup()
    t.goto(offset)
    t.goto(offset[0] + side/2-radius, offset[1] + side/2-radius)
    t.pendown()
    t.lt(45)
    draw_dashedline(2*len_diagonal, t)
    t.penup()
    t.goto(offset[0] + side / 2 - radius, offset[1] + side / 2 + radius)
    t.rt(90)
    t.pendown()
    draw_dashedline(2 * len_diagonal, t)
    t.penup()
    t.goto(offset)

def draw_centralsound3(radius, side, t, offset=(0,0)):
    len_diagonal = (2 * (radius ** 2)) ** 0.5
    t.penup()
    t.goto(offset)
    t.goto(offset[0] + side/2-radius, offset[1] + side/2-radius)
    t.pendown()
    t.lt(45)
    t.fd(2*len_diagonal)
    t.penup()
    t.goto(offset[0] + side / 2 - radius, offset[1] + side / 2 + radius)
    t.rt(90)
    t.pendown()
    t.fd(2 * len_diagonal)
    t.penup()
    t.goto(offset)

def draw_centralsound5(radius, side, t, offset = (0,0)):
    # draw_circle(radius,side, offset)
    draw_centralsound1(radius,side, t, offset)
    draw_centralsound3(radius,side, t, offset)

def draw_centralsound6(radius, side, t, offset=(0,0)):
    # draw_circle(radius, side, offset)
    draw_centralsound2(radius,side, t, offset)
    draw_centralsound4(radius,side, t, offset)


def draw_centralsound(radius, side, type, t, offset=(0,0)):
    #draw_circle(radius, side, offset)
    t.speed(speed)
    if type == 1:
        draw_centralsound1(radius, side, t, offset)
    elif type == 2:
        draw_centralsound2(radius, side, t, offset)
    elif type == 3:
        draw_centralsound3(radius, side, t, offset)
    elif type == 4:
        draw_centralsound4(radius, side, t, offset)
    elif type == 5:
        draw_centralsound5(radius, side, t, offset)
    elif type == 6:
        draw_centralsound6(radius, side, t, offset)


    # type 1 = ononderbroeken horizontale lijn door de cirkel
    # type 2 = onderbroken horizontale lijn door de cirkel
    # type 3 = x door de cirkel
    # type 4 = onderbroken lijn x door de cirkel
    # type 5 = lijn + x
    # type 6 = lijn + x onderbroken
    # type 7 = alleen de cirkel



def draw_number(side, sq_number, t, offset=(0,0)):
    t.penup()
    # bij side = 200
    # x = 20, y = 165, r = 15
    r = side * 0.075
    x = offset[0] + (side * 0.1)
    y = offset[1] + side - ((side * 0.025) + (2 * r))
    t.goto(x, y)
    t.pendown()
    t.circle(r)
    # FIXME font size adapt to side size. 50 bij side = 400
    fontsize = int(side * 0.125)
    # FIXME goto middle of the circle first
    t.write(sq_number, False, align="center", font=("Arial", fontsize, "bold"))
    t.penup()
    t.goto(offset)

def makeCompleteSquare(side, t, type, sq_number, offset=(0,0)):
    radius = side/8
    t.home()
    t.penup()
    draw_square(side, t, offset)
    draw_circle(radius, side, t, offset)
    draw_centralsound(radius,side, type, t, offset)
    draw_number(side, sq_number, t, offset)
    t.home()

makeCompleteSquare(200, t, 1, 12, (-400,300))
makeCompleteSquare(200, t, 2, 13, (-200,300))
makeCompleteSquare(200, t, 3, 14, (0, 300))
makeCompleteSquare(200, t, 4, 15, (200,300))
makeCompleteSquare(200, t, 5, 16, (400,300))
makeCompleteSquare(200, t, 6, 17, (-400,100))
makeCompleteSquare(200, t, 7, 18, (-200,100))
makeCompleteSquare(200, t, 1, 19, (0,100))
makeCompleteSquare(200, t, 2, 20, (200,100))
makeCompleteSquare(200, t, 3, 21, (400,100))





