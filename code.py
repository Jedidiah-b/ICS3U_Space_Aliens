import ugame
# the layers of the stage should be from top to bottom
import stage

# moving ball
class Ball(stage.Sprite):
    # __init__ method class handles creating new sprites 
    def __init__(self, x, y):
        super().__init__(bank, 1, x, y)
        self.dx = 2
        self.dy = 1
    
    def update(self):
        super().update()
        self.set_frame(self.frame % 4 + 1)
        self.move(self.x + self.dx, self.y + self.dy)
        if not 0 < self.x < 144:
            self.dx = -self.dx
        if not 0 < self.y < 112:
            self.dy = -self.dy


# this contains the image of the ball 
bank = stage.Bank.from_bmp16("ball.bmp")
# this contains the background of the map
background = stage.Grid(bank, 10, 8) 
# this displays text 
text = stage.Text(12, 1)
text.move(32, 60)
text.text("Hello world!")
ball = stage.Sprite(bank, 1, 8, 8)
game = stage.Stage(ugame.display, 12)
game.layers = [background]
game.render_block()

dx = 2 
while True:
  # this controls the animation for the sprite 
  ball.update()
  ball.set_frame(ball.frame % 4 + 1) 
  # this controls the movement of the sprite 
  ball.move(ball.x + dx, ball.y)
  if not 0 < ball.x < 144:
        dx = -dx
  game.render_sprites([ball])
  game.tick() 