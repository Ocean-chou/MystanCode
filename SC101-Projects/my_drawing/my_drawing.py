"""
File: my_drawing.py
Name: Ocean
----------------------

"""

from campy.graphics.gobjects import GOval, GRect, GLine, GPolygon, GArc
from campy.graphics.gwindow import GWindow
window = GWindow(400, 600, title='my_drawing.py')


def main():
    """
    Title: My wife's love

    Snoopy is my wife's favorite cartoon character,
    She agrees with me learning Python,so I want to give her a Snoopy that I draw.
    """
    white = GRect(400, 600)
    white.filled = True
    white.fill_color = 'white'
    white.color = 'white'
    window.add(white)
    wooden_house()
    snoopy()


def wooden_house():
    roof = GPolygon()
    roof.add_vertex((50, 200))
    roof.add_vertex((350, 200))
    roof.add_vertex((380, 350))
    roof.add_vertex((20, 350))
    roof.filled = True
    roof.fill_color = 'red'
    roof1 = GPolygon()
    roof1.add_vertex((50, 200))
    roof1.add_vertex((350, 200))
    roof1.add_vertex((360, 250))
    roof1.add_vertex((40, 250))
    roof1.filled = True
    roof1.fill_color = 'white'
    roof2 = GPolygon()
    roof2.add_vertex((380, 350))
    roof2.add_vertex((20, 350))
    roof2.add_vertex((30, 360))
    roof2.add_vertex((370, 360))
    roof2.filled = True
    roof2.fill_color = 'red'
    board1 = GLine(30, 300, 370, 300)
    wall = GRect(300, 140, x=50, y=360)
    wall.filled = True
    wall.fill_color = 'red'
    board2 = GLine(50, 405, 350, 405)
    board3 = GLine(50, 450, 350, 450)
    window.add(roof)
    window.add(roof1)
    window.add(roof2)
    window.add(wall)
    window.add(board1)
    window.add(board2)
    window.add(board3)
    f1 = GRect(212, 20, x=62, y=200)
    f1.filled = True
    f1.fill_color = 'white'
    f1.color = 'white'
    window.add(f1)


def snoopy():
    head1 = GArc(190, 100, 120, 100)
    window.add(head1, x=60, y=150)
    head2 = GArc(128, 200, 290, 40)
    window.add(head2, x=50, y=112)
    head3 = GArc(50, 160, 350, 190)
    window.add(head3, x=82, y=100)
    head4 = GArc(70, 60, 190, 160)
    window.add(head4, x=65, y=196)
    eye = GLine(75, 180, 85, 190)
    window.add(eye)
    ear1 = GOval(20, 70, x=85, y=220)
    ear1.filled = True
    ear1.fill_color = 'white'
    window.add(ear1)
    ear2 = GOval(10, 60, x=90, y=220)
    ear2.filled = True
    ear2.fill_color = 'black'
    window.add(ear2)
    collar = GRect(5, 60, x=132, y=150)
    collar.filled = True
    window.add(collar)
    nose1 = GOval(15, 15, x=100, y=85)
    nose1.filled = True
    nose1.fill_color = 'white'
    window.add(nose1)
    nose2 = GOval(10, 10, x=103, y=90)
    nose2.filled = True
    nose2.fill_color = 'black'
    window.add(nose2)
    body1 = GArc(80, 150, 0, 190)
    window.add(body1, x=135, y=120)
    body2 = GArc(155, 20, 30, 90)
    window.add(body2, x=180, y=205)
    body3 = GArc(155, 20, 90, 60)
    window.add(body3, x=130, y=205)
    leg = GLine(215, 163, 240, 165)
    window.add(leg)
    foot1 = GArc(40, 120, 10, 180)
    window.add(foot1, x=240, y=125)
    foot2 = GArc(30, 150, 270, 100)
    window.add(foot2, x=264, y=120)
    foot3 = GArc(40, 120, 60, 130)
    window.add(foot3, x=230, y=125)
    toe1 = GLine(260, 156, 280, 152)
    window.add(toe1)
    toe2 = GLine(263, 170, 280, 168)
    window.add(toe2)
    arm1 = GLine(160, 180, 190, 180)
    window.add(arm1)
    arm2 = GArc(100, 30, 20, 70)
    window.add(arm2, x=160, y=180)
    arm3 = GArc(30, 40, 210, 210)
    window.add(arm3, x=182, y=180)
    arm4 = GLine(160, 205, 185, 208)
    window.add(arm4)
    hand1 = GLine(192, 205, 190, 215)
    window.add(hand1)
    hand2 = GLine(200, 203, 202, 215)
    window.add(hand2)


if __name__ == '__main__':
    main()
