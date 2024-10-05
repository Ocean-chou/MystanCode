"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.


File: breakout.py
Name: Ocean
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    vx = graphics.get_velocity_x()                  # The initial velocity of the ball in the x direction
    vy = graphics.get_velocity_y()                  # The initial velocity of the ball in the y direction
    life = NUM_LIVES                                # The number of times the ball falls below the window
    d_ball = graphics.ball.width                    # The diameter of ball
    brick_count = graphics.get_brick()              # The number of brick
    ball_in_paddle = False                          # Detect if the ball is inside the paddle
    # Add the animation loop here!
    while True:
        # UPDATE
        if graphics.start_game:
            graphics.ball.move(vx, vy)
            # CHECK
            if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width-d_ball:
                vx = -vx
            if graphics.ball.y <= 0:
                vy = -vy
            if graphics.ball.y >= graphics.window.height-d_ball:
                life -= 1
                graphics.set_ball()
                vx = graphics.get_velocity_x()      # Regenerate a random x-direction velocity
                vy = graphics.get_velocity_y()      # Regenerate a random y-direction velocity
                graphics.set_restart()              # Return 'False' to breakoutgraphics.py
            # Remove Brick and Bouncing
            # Assuming the ball is a square, detect if any of the four vertices collide with object
            ball_top_lift = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
            ball_top_right = graphics.window.get_object_at(graphics.ball.x+d_ball, graphics.ball.y)
            ball_bottom_lift = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+d_ball)
            ball_bottom_right = graphics.window.get_object_at(graphics.ball.x+d_ball, graphics.ball.y+d_ball)
            # If the bottom of the ball is higher than the top of the paddle,
            # the ball is definitely not inside the paddle
            if graphics.ball.y+d_ball < graphics.paddle.y:
                ball_in_paddle = False
            # If the ball collide the scoreboard,it will not bounce and the scoreboard will not be removed
            if ball_top_lift is not graphics.scoreboard:
                if ball_top_lift is not None:
                    if graphics.ball.y+d_ball <= graphics.paddle.y:
                        graphics.remove_brick()
                        if ball_top_right is not None:
                            vy = -vy
                        elif ball_bottom_lift is not None:
                            vx = -vx
                        else:
                            vx = -vx
                            vy = -vy
                    else:
                        if ball_in_paddle is False:
                            vx = -vx
                            if ball_top_lift is graphics.paddle:
                                ball_in_paddle = True
                elif ball_top_right is not None:
                    if graphics.ball.y+d_ball <= graphics.paddle.y:
                        graphics.remove_brick()
                        if ball_bottom_right is not None:
                            vx = -vx
                        elif ball_top_lift is not None:
                            vy = -vy
                        else:
                            vx = -vx
                            vy = -vy
                    else:
                        if ball_in_paddle is False:
                            vx = -vx
                            if ball_top_right is graphics.paddle:
                                ball_in_paddle = True
                elif ball_bottom_right is not None:
                    if ball_in_paddle is False:
                        graphics.remove_brick()
                        if ball_bottom_lift is not None:
                            vy = -vy
                        elif ball_top_right is not None:
                            vx = -vx
                        else:
                            vx = -vx
                            vy = -vy
                        if ball_bottom_right is graphics.paddle:
                            ball_in_paddle = True
                elif ball_bottom_lift is not None:
                    if ball_in_paddle is False:
                        graphics.remove_brick()
                        if ball_top_lift is not None:
                            vx = -vx
                        elif ball_bottom_right is not None:
                            vy = -vy
                        else:
                            vx = -vx
                            vy = -vy
                        if ball_bottom_lift is graphics.paddle:
                            ball_in_paddle = True
            remove_brick_count = graphics.score
            # The game over if the number of times the ball falls below the window reaches the setting
            if life == 0:
                break
            # The game end if the all bricks are breakout
            if remove_brick_count == brick_count:
                break
        # PAUSE
        pause(FRAME_RATE)
    if life == 0:
        graphics.game_over()
    else:
        graphics.game_clear()


if __name__ == '__main__':
    main()
