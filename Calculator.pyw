#Intro to Programming
#Calculator.pyw
from graphics import *

win = GraphWin('Calc', 320, 500)
win.setCoords(0, 0, 4, 6)

buttons = dict()
buttons['0'] = Rectangle(Point(0, 0), Point(2, 1))
buttons['.'] = Rectangle(Point(2, 0), Point(3, 1))
buttons['='] = Rectangle(Point(3, 0), Point(4, 1))
buttons['1'] = Rectangle(Point(0, 1), Point(1, 2))
buttons['2'] = Rectangle(Point(1, 1), Point(2, 2))
buttons['3'] = Rectangle(Point(2, 1), Point(3, 2))
buttons['+'] = Rectangle(Point(3, 1), Point(4, 2))
buttons['4'] = Rectangle(Point(0, 2), Point(1, 3))
buttons['5'] = Rectangle(Point(1, 2), Point(2, 3))
buttons['6'] = Rectangle(Point(2, 2), Point(3, 3))
buttons['-'] = Rectangle(Point(3, 2), Point(4, 3))
buttons['7'] = Rectangle(Point(0, 3), Point(1, 4))
buttons['8'] = Rectangle(Point(1, 3), Point(2, 4))
buttons['9'] = Rectangle(Point(2, 3), Point(3, 4))
buttons['*'] = Rectangle(Point(3, 3), Point(4, 4))
buttons['AC'] = Rectangle(Point(0, 4), Point(1, 5))
buttons['+/-'] = Rectangle(Point(1, 4), Point(2, 5))
buttons['%'] = Rectangle(Point(2, 4), Point(3, 5))
buttons['/'] = Rectangle(Point(3, 4), Point(4, 5))

for symbol, btn in buttons.items():
    btn.setOutline('black')
    text = Text(btn.getCenter(), symbol)
    text.setSize(24)
    win.addItem(btn)
    win.addItem(text)

display = Text(Point(2, 5.5), '')

win.redraw()

# Return the symbol clicked
def clicked(click):
    cx, cy = click.getX(), click.getY()
    for symbol, btn in buttons.items():
        if btn.getP1().getX() < cx < btn.getP2().getX() and \
           btn.getP1().getY() < cy < btn.getP2().getY():
            return symbol
    return ''

while win.isOpen():
    click = win.getMouse()
    symbol = clicked(click)
    if symbol == 'AC':
        display.setText('')
        dirty = False
    elif symbol == '%' or symbol == '+/-':
        pass
    elif symbol == '=':
        display.setText(str(eval(display.getText())))
        dirty = True
    else:
        if dirty: continue
        display.setText(display.getText() + symbol)
