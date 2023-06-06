AI_Paddle = Class{}

function AI_Paddle:init(x, y, width, height)
    self.x = x
    self.y = y
    self.width = width
    self.height = height

    self.dy = 0
    self.speed = 500

    
end

function AI_Paddle:update(dt, Ball)
    if ball.y < self.y then
        self.dy = -PADDLE_SPEED
      elseif ball.y > self.y + self.height then
        self.dy = PADDLE_SPEED
      else
        self.dy = 0
      end
      self.y = self.y + self.dy * dt
    
    end
    
function AI_Paddle:render()
        love.graphics.setColor(10, 0, 255)  --Set the pink color
        love.graphics.rectangle('fill', self.x, self.y, self.width, self.height)

      end