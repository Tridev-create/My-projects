push = require 'push'

Class = require 'class'

require 'Paddle-class'

require 'AI_Paddle'

require 'Ball-class'

WIDTH_LEVEL = 1280
HEIGHT_LEVEL = 720

VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

PADDLE_SPEED = 250

function love.load()


    love.graphics.setDefaultFilter('nearest', 'nearest')

    math.randomseed(os.time())

    scoreFont = love.graphics.newFont('font.ttf', 32)

    Victoryfont = love.graphics.newFont('font.ttf', 50)

    Scorefont = love.graphics.newFont('font.ttf', 15)


    Coolfont = love.graphics.newFont('font.ttf', 8)



    love.graphics.setFont(Coolfont)

    love.window.setTitle('Pong-Amazing Game')

    sounds = {
        ['paddle_hit'] = love.audio.newSource('sounds/paddle_hit.wav', 'static') ,
        ['score'] = love.audio.newSource('sounds/score.wav', 'static') ,
        ['wall_hit'] = love.audio.newSource('sounds/wall_hit.wav', 'static') ,
        ['celebrate'] = love.audio.newSource('sounds/Celebrate.wav', 'static') ,
        ['music'] = love.audio.newSource('sounds/marios_way.mp3', 'static') ,
    }

    sounds['music']:setLooping(true)
    sounds['music']:play()

    push:setupScreen(VIRTUAL_WIDTH ,VIRTUAL_HEIGHT, WIDTH_LEVEL , HEIGHT_LEVEL, {
        fullscreen = true, 
        resizable = true, 
        vsync = true

    })

    player1Score = 0
    player2Score = 0

    onetime = 1

    servingPlayer = 1

    player1 = Paddle(10, 30, 5, 30)
    player2 = AI_Paddle(VIRTUAL_WIDTH - 10, VIRTUAL_HEIGHT - 30, 5, 30)

    ball = Ball(VIRTUAL_WIDTH / 2 - 10, VIRTUAL_HEIGHT / 2 - 2, 15, 15)

    gameState = 'start'

    winningPlayer = 0
   

end

function love.resize(w, h)
    push:resize(w, h)

end

local isPaused = false

local AI_Paddle = AI_Paddle(VIRTUAL_WIDTH - 15, VIRTUAL_HEIGHT / 2 - 20, 5, 40)


--function love.keypressed(key)
  --  if key == 'tab' then
    --    isPaused = not isPaused
    --end
--end
function love.update(dt)

    if not isPaused then

    if gameState == 'serve' then
        ball.dy = math.random(-50,50)
        if servingPlayer == 1 then
            ball.dx = math.random(140, 200)
            else
                ball.dx = -math.random(140, 200)
        end
    

    elseif gameState == 'play' then
        
        if ball:collides(player1) then
            ball.dx = -ball.dx * 1.5 --add speed when the ball is detecting with paddles everytime
            ball.x = player1.x + 5  
             
        if ball.dy < 0 then
            ball.dy = -math.random(10, 150)
        else
            ball.dy = math.random(10, 150)
        end
        sounds['paddle_hit']:play()
    end



        if ball:collides(player2) then
            ball.dx = -ball.dx * 1.05
            ball.x = player2.x - 15

            if ball.dy < 0 then
                ball.dy = -math.random(10, 150)
            else
                ball.dy = math.random(10, 150)
            end

            sounds['paddle_hit']:play()
    end

    if ball.y <= 0 then -- wall
        ball.y = 0
        ball.dy = -ball.dy
        sounds['wall_hit']:play()
    end

    if ball.y >= VIRTUAL_HEIGHT - 4 then
        ball.y = VIRTUAL_HEIGHT - 4
        ball.dy = -ball.dy
        sounds['wall_hit']:play()
    end
end
    if ball.x < 0 then -- when the ball get out on the right of the screen
        servingPlayer = 1
        player2Score = player2Score + 1
        ball:reset()
        gameState = 'serve'
        sounds['score']:play()

        if player2Score == 10 then
            winningPlayer = 2
            gameState = 'win'
        else
            gameState = 'serve'
    
            ball:reset()
        end
    
    end

    if ball.x > VIRTUAL_WIDTH then -- left
        servingPlayer = 2
        player1Score = player1Score + 1
        ball:reset()
        gameState = 'serve'

        sounds['score']:play()

        if player1Score == 10 then
            winningPlayer = 1
            gameState = 'win'
        else
            gameState = 'serve'
    
            ball:reset()
        end
    
    end

    
    if love.keyboard.isDown('w') then
        player1.dy = -PADDLE_SPEED
        elseif love.keyboard.isDown('s') then
            player1.dy = PADDLE_SPEED
            else
                player1.dy = 0
            end

    if love.keyboard.isDown('up') then
        player2.dy = -PADDLE_SPEED
        elseif love.keyboard.isDown('down') then
            player2.dy = PADDLE_SPEED
            else
                player2.dy = 0
            
    end


    if gameState == 'play' then
        ball:update(dt)
    end

        player1:update(dt)
        player2:update(dt)


        if ball.y < AI_Paddle.y + AI_Paddle.height / 20 then
            AI_Paddle.dy = -PADDLE_SPEED
        elseif ball.y > AI_Paddle.y + AI_Paddle.height / 20 then
            AI_Paddle.dy = PADDLE_SPEED
        else
            AI_Paddle.dy = 0
        end
    
        AI_Paddle:update(dt)

        if ball:collides(AI_Paddle) then
            ball.dx = -ball.dx * 1.03
            ball.x = AI_Paddle.x - ball.width
            sounds['paddle_hit']:play()

            if ball.dy < 0 then
                ball.dy = -math.random(10, 150)
            else
                ball.dy = math.random(10, 150)
            end
        end

end
end

    function love.keypressed(key)
        if key == 'space' then
            isPaused = not isPaused
        
     elseif key == 'escape' then
            love.event.quit()
        elseif key == 'enter' or key == 'return' then
            if gameState == 'start' then
                ball = Ball(VIRTUAL_WIDTH / 2 - 10, VIRTUAL_HEIGHT / 2 - 2, 15, 15)
                gameState = 'serve'
            elseif gameState == 'serve' then
                ball = Ball(VIRTUAL_WIDTH / 2 - 10, VIRTUAL_HEIGHT / 2 - 2, 15, 15)
                sounds['paddle_hit']:play()
                gameState = 'play'
            elseif gameState == 'win' then
                
                gameState = 'serve'
                ball = Ball(VIRTUAL_WIDTH / 2 - 10, VIRTUAL_HEIGHT / 2 - 2, 15, 15)
                ball:reset()

                player1Score = 0
                player2Score = 0

                if winningPlayer == 1 then
                    servingPlayer = 2
                    else
                        servingPlayer = 1
                end
                
            
        end
    end     
    end   
    

function love.draw()
    push:apply('start')

       
            Score()
            
            if isPaused then
                love.graphics.setFont(Victoryfont)
                love.graphics.printf('Pause', 10, 80, VIRTUAL_WIDTH , 'center')
        
                love.graphics.setFont(Coolfont)
                love.graphics.printf('" Press Space to Resume the Game ! "', 0, 150, VIRTUAL_WIDTH , 'center')
        
            else     
                
                player1:render()
        
                ball:render()
            end
           
                if  gameState == 'start' then
                love.graphics.setFont(Coolfont)
                love.graphics.printf("Start Game Bro!", 0, 20, VIRTUAL_WIDTH,'center')
                elseif gameState == 'serve' then
                    love.graphics.setFont(Coolfont)
                    love.graphics.printf('Player ' .. tostring(servingPlayer) .. "'s serve!"
                    , 0, 10, VIRTUAL_WIDTH, 'center')
                    love.graphics.printf('Press Enter to serve!', 0, 20, VIRTUAL_WIDTH, 'center')
                    Paddle_reset()
                    
            end
            
            
        
                if ball:collides(player1) then
                player1.height = player1.height + 2
                ball.height = ball.height - 0.25
                ball.width = ball.width - 0.25
            
               elseif ball:collides(player2) then
                    player2.height = player2.height + 2
                    ball.height = ball.height - 0.25
                    ball.width = ball.width - 0.25
                    
            end
            if gameState == 'win' then
                love.graphics.clear(40/255, 45/255, 52/255, 255/255)
        
                    love.graphics.setFont(Victoryfont)
                    love.graphics.printf('VICTORY !!!', 10, 80, VIRTUAL_WIDTH , 'center')
            
                    love.graphics.setFont(Coolfont)
                    love.graphics.printf('" Press Enter To Restart A New Game ! "', 0, 150, VIRTUAL_WIDTH , 'center')
        
                    love.graphics.printf('Player ' .. tostring(winningPlayer) .. ' wins!', 0, 130, VIRTUAL_WIDTH , 'center')
        
                    sounds['celebrate']:play(onetime)

        end
    

    displayFPS()

    AI_Paddle:render()

    push:apply('end')

    
    
end

function displayFPS()
    love.graphics.setFont(Coolfont)
    love.graphics.setColor(0, 255/255, 0, 255/255)
    love.graphics.print('FPS : ' .. tostring(love.timer.getFPS()), 10, 10)
end

function  Victory() 
    if winningPlayer == 1 then
        love.graphics.clear(40/255, 45/255, 52/255, 255/255)

        love.graphics.setFont(Victoryfont)
        love.graphics.printf('VICTORY !!!', 0, 80, VIRTUAL_WIDTH , 'center')

        love.graphics.setFont(Coolfont)
        love.graphics.printf('" Press Enter To Restart A New Game ! "', 0, 150, VIRTUAL_WIDTH , 'center')

        love.graphics.printf('Player 1 is winner' , 0, 130, VIRTUAL_WIDTH , 'center')
        player1Score = 0


        elseif  winningPlayer == 2  then
            love.graphics.clear(40/255, 45/255, 52/255, 255/255)

            love.graphics.setFont(Victoryfont)
            love.graphics.printf('VICTORY !!!', 0, 80, VIRTUAL_WIDTH , 'center')
    
            love.graphics.setFont(Coolfont)
            love.graphics.printf('" Press Enter To Restart A New Game ! "', 0, 150, VIRTUAL_WIDTH , 'center')

            love.graphics.printf('Player 2 is winner' , 0, 130, VIRTUAL_WIDTH , 'center')

        

        end       
    end

function Score()
    love.graphics.setFont(scoreFont)
    love.graphics.print(tostring(player1Score), VIRTUAL_WIDTH / 2 - 55, 
    VIRTUAL_HEIGHT / 3)
    love.graphics.print(tostring(player2Score), VIRTUAL_WIDTH / 2 + 30,
    VIRTUAL_HEIGHT / 3)
  
end

function Paddle_reset()
    player1 = Paddle(10, 30, 5, 30)
    player2 = Paddle(VIRTUAL_WIDTH - 10, VIRTUAL_HEIGHT - 30, 5, 30)
end
