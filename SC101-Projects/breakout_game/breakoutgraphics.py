"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks10
BRICK_COLS = 10        # Number of columns of bricks10
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball

# start_game = False


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self.paddle_offset = paddle_offset
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=self.window.height-self.paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = 'silver'
        self.set_ball()
        # Default initial velocity for the ball
        self.vx = 0
        self.vy = 0
        # Initialize our mouse listeners
        self.start_game = False
        onmouseclicked(self.control)
        onmousemoved(self.tracker)
        # Draw bricks
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_offset = brick_offset
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_spacing = brick_spacing
        self.set_brick()
        # Scoreboard
        self.score = 0
        self.scoreboard = GLabel('score: ' + str(self.score))
        self.window.add(self.scoreboard, x=0, y=self.scoreboard.height)

    def set_ball(self):
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)
        # self.window.add(self.ball, x=2, y=(self.window.height-self.paddle_offset))

    def tracker(self, mouse):
        # If the mouse moves left beyond the window, the paddle will not move outside the window
        if mouse.x-self.paddle.width/2 <= 0:
            self.paddle.x = 0
        # If the mouse moves right beyond the window, the paddle will not move outside the window
        elif mouse.x+self.paddle.width/2 >= self.window.width:
            self.paddle.x = self.window.width-self.paddle.width
        else:
            self.paddle.x = mouse.x-self.paddle.width/2

    def control(self, click):
        if not self.start_game:
            self.start_game = True

    def set_restart(self):
        self.start_game = False

    @staticmethod
    def get_velocity_x():
        vx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            vx = -vx
        return vx

    @staticmethod
    def get_velocity_y():
        return INITIAL_Y_SPEED

    def set_brick(self):
        brick_y = self.brick_offset
        for i in range(self.brick_rows):
            brick_x = 0
            for j in range(self.brick_cols):
                brick = GRect(self.brick_width, self.brick_height)
                brick.filled = True
                brick.fill_color = 'red'
                if i >= 2:
                    brick.fill_color = 'orange'
                if i >= 4:
                    brick.fill_color = 'yellow'
                if i >= 6:
                    brick.fill_color = 'green'
                if i >= 8:
                    brick.fill_color = 'indigo'
                self.window.add(brick, x=brick_x, y=brick_y)
                brick_x += self.brick_width+self.brick_spacing
            brick_y += self.brick_height+self.brick_spacing

    def get_brick(self):
        brick_count = self.brick_cols * self.brick_rows
        return brick_count

    def remove_brick(self):
        obj = self.window.get_object_at(0, 0)
        if self.window.get_object_at(self.ball.x, self.ball.y) is not None:
            obj = self.window.get_object_at(self.ball.x, self.ball.y)
        elif self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height) is not None:
            obj = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height)
        elif self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y) is not None:
            obj = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y)
        elif self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.height) is not None:
            obj = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.height)
        # Only remove brick
        if obj is not self.paddle and obj is not self.scoreboard:
            self.window.remove(obj)
            self.score += 1
            self.scoreboard.text = 'score: ' + str(self.score)

    def game_over(self):
        self.window.remove(self.ball)
        over = GLabel('GAME OVER')
        over.font = '-40'
        over.color = 'red'
        self.window.add(over, x=(self.window.width-over.width)/2, y=(self.window.height+over.height)/2)

    def game_clear(self):
        self.window.remove(self.ball)
        over = GLabel('YOU WIN!')
        over.font = '-40'
        over.color = 'red'
        self.window.add(over, x=(self.window.width-over.width)/2, y=(self.window.height+over.height)/2)
