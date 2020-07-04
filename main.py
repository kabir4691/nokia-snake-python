import pygame
import time
import random

yellowColor = (255, 255, 102)
blackColor = (0, 0, 0)
redColor = (213, 50, 80)
greenColor = (0, 255, 0)
blueColor = (50, 153, 213)

screenWidth = 400
screenHeight = 400

snakeSize = 10
snakeSpeed = 10

clock = pygame.time.Clock()

def init():
  
  pygame.init()

  global font
  font = pygame.font.SysFont("comicsansms", 30)
  
  global surface
  surface = pygame.display.set_mode((screenWidth, screenHeight))
  
  pygame.display.set_caption('Snake Game')

def updateScore(score):
  message = font.render("Your Score: " + str(score), True, yellowColor)
  surface.blit(message, [0, 0])
 
def updateSnake(snakePath):
  for item in snakePath:
    pygame.draw.rect(surface, blackColor, [item[0], item[1], snakeSize, snakeSize])

def displayGameOverMessage():
  surface.fill(blueColor)
  message = font.render('Game over', True, redColor)
  surface.blit(message, [screenWidth / 4, screenHeight / 4])
  message = font.render('Press space key to play again', True, redColor)
  surface.blit(message, [screenWidth / 4, (screenHeight / 4) + 100])
  message = font.render('Press q to quit', True, redColor)
  surface.blit(message, [screenWidth / 4, (screenHeight / 4) + 200])
  
def startGame():
  isGameOver = False
  isGameQuit = False

  snakeHeadX = screenWidth / 2
  snakeHeadY = screenHeight / 2

  changeX = 0
  changeY = 0

  snakePath = []
  snakeLength = 1

  appleX = round(random.randrange(0, screenWidth - snakeSize) / 10.0) * 10.0
  appleY = round(random.randrange(0, screenHeight - snakeSize) / 10.0) * 10.0

  while not isGameQuit:

    if isGameOver:
      while isGameOver:
        displayGameOverMessage()
        updateScore(len(snakePath) - 1)
        pygame.display.update()

        for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
              isGameQuit = True
              isGameOver = False
            elif event.key == pygame.K_SPACE:
                isGameQuit = True
                startGame()
      return

    surface.fill(blueColor)
    pygame.draw.rect(surface, greenColor, [appleX, appleY, snakeSize, snakeSize])

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        isGameQuit = True
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          changeX = -snakeSize
          changeY = 0
        elif event.key == pygame.K_RIGHT:
          changeX = snakeSize
          changeY = 0
        elif event.key == pygame.K_UP:
          changeX = 0
          changeY = -snakeSize
        elif event.key == pygame.K_DOWN:
          changeX = 0
          changeY = snakeSize

    snakeHeadX += changeX
    snakeHeadY += changeY

    if snakeHeadX >= screenWidth or snakeHeadX < 0 or snakeHeadY >= screenHeight or snakeHeadY < 0: isGameOver = True  

    newPathItem = [snakeHeadX, snakeHeadY]
    snakePath.append(newPathItem)

    if (len(snakePath) > snakeLength): del snakePath[0]
    
    for item in snakePath[:-1]:
      if item == newPathItem:
        isGameOver = True
        break

    updateSnake(snakePath)
    updateScore(snakeLength - 1)

    if snakeHeadX == appleX and snakeHeadY == appleY:
      appleX = round(random.randrange(0, screenWidth - snakeSize) / 10.0) * 10.0
      appleY = round(random.randrange(0, screenHeight - snakeSize) / 10.0) * 10.0
      snakeLength += 1

    clock.tick(snakeSpeed)

    pygame.display.update()

  pygame.quit()
 
init()
startGame()