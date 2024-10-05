"""
File: bouncing_ball.py
Name: Ocean
-------------------------
This file shows the animation
about the bouncing process of a ball.
When user clicks the mouse, the ball will drop.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
# ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
# vy = 0
# life = 0
start_game = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global start_game
    ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
    vy = 0
    life = 0
    ball.filled = True
    window.add(ball)
    onmouseclicked(control)
    while life < 3:
        # After the ball bounces outside the window three times, click is ineffective.
        if start_game:
            # In game loop
            while ball.x < window.width:
                vy += GRAVITY
                ball.move(VX, vy)
                if ball.y + SIZE >= window.height:
                    if vy > 0:
                        vy = -vy * REDUCE
                pause(DELAY)
            ball.filled = True
            window.add(ball, x=START_X, y=START_Y)
            life += 1
            start_game = False
            # End of loop
        pause(DELAY)


def control(mouse):
    global start_game
    if not start_game:
        start_game = True

    # global ball
    # global vy
    # global life
    # switch = window.get_object_at(START_X+SIZE/2, START_Y+SIZE/2)
    # if switch is not None:
    #     # When the ball is bouncing, click is ineffective.
    #     if life < 3:
    #         # After the ball bounces outside the window three times, click is ineffective.
    #         while ball.x < window.width:
    #             vy += GRAVITY
    #             ball.move(VX, vy)
    #             if ball.y+SIZE >= window.height:
    #                 if vy > 0:
    #                     vy = -vy*REDUCE
    #             pause(DELAY)
    #         ball.filled = True
    #         window.add(ball, x=START_X, y=START_Y)
    #         life += 1


if __name__ == "__main__":
    main()
