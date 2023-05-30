import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers. 

# Initialize the pygame modules to get everything started.
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init() 

# The screen that will be created needs a width and a height.
screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

# This creates the player and gives it the image found in this folder (similarly with the enemy image). 
player = pygame.image.load("player.png")
enemy_1 = pygame.image.load("enemy_1.png")
enemy_2 = pygame.image.load("enemy_2.png")
enemy_3 = pygame.image.load("enemy_3.png")
prize = pygame.image.load("prize.png")

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).
image_height = player.get_height()
image_width = player.get_width()
enemy_height = enemy_1.get_height()
enemy_width = enemy_1.get_width()
enemy_height = enemy_2.get_height()
enemy_width = enemy_2.get_width()
enemy_height = enemy_3.get_height()
enemy_width = enemy_3.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()
print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

# Store the positions of the player and enemy as variables so that you can change them later. 
playerXPosition = 100
playerYPosition = 50

# Make the enemy start off screen and at a random y position.
enemy_1XPosition =  screen_width
enemy_1YPosition =  random.randint(0, screen_height - enemy_height)
enemy_2XPosition =  screen_width
enemy_2YPosition =  random.randint(0, screen_height - enemy_height)
enemy_3XPosition =  screen_width
enemy_3YPosition =  random.randint(0, screen_height - enemy_height)
prizeXPosition =  screen_width
prizeYPosition =  random.randint(0, screen_height - prize_height)

# This checks if the up or down key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False. 
# Boolean values are True or False values that can be used to test conditions and test states that are binary, i.e. either one way or the other. 

keyUp= False
keyDown = False
keyLeft= False
keyRight= False

# The Game Loop
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play. 

while 1: # This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting). In Python the int 1 has the boolean value of 'true'. In fact numbers greater than 0 also do. 0 on the other hand has a boolean value of false. You can test this out with the bool(...) function to see what boolean value types have. You will learn more about while loop structers later. 

    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(enemy_1, (enemy_1XPosition, enemy_1YPosition))
    screen.blit(enemy_2, (enemy_2XPosition, enemy_2YPosition))
    screen.blit(enemy_3, (enemy_3XPosition, enemy_3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.   
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program.         
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
           
        # This event checks if the user press a key down.       
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.            
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT: 
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        # This event checks if the key is up(i.e. not pressed by the user).        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False    

        # This event checks if the user press a key down.

              
    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position.    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1
    if keyLeft == True:
        if playerXPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerXPosition -= 1
    if keyRight == True:
        if playerXPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerXPosition += 1
            
    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image.     
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemy:    
    enemyBox = pygame.Rect(enemy_1.get_rect())
    enemyBox.top = enemy_1YPosition
    enemyBox.left = enemy_1XPosition
    enemyBox = pygame.Rect(enemy_2.get_rect())
    enemyBox.top = enemy_2YPosition
    enemyBox.left = enemy_2XPosition
    enemyBox = pygame.Rect(enemy_3.get_rect())
    enemyBox.top = enemy_3YPosition
    enemyBox.left = enemy_3XPosition
    
    # Bounding box and collision conditions for prize:    
    prizeBox = pygame.Rect(player.get_rect())

    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    
    # Test collision of the boxes:   
    if playerBox.colliderect(enemyBox): 
        
        print("You lose!")

        # Quite game and exit window:        
        pygame.quit()
        
        exit(0)
        

    elif playerBox.colliderect(prizeBox):
        print("You win!")
        # Quite game and exit window: 
        
        pygame.quit()
        
        exit(0)
        
    # If the enemy is off the screen the user wins the game:    
    if enemy_1XPosition < 0 - enemy_width:
        
     if enemy_2XPosition < 0 - enemy_width:
   
      if enemy_3XPosition < 0 - enemy_width:
         
        # Display wining status to the user:        
        print("You win!")
        
        # Quite game and exit window:
        
        pygame.quit()
        
        exit(0)

    
    # Make enemy approach the player.    
    enemy_1XPosition -= 0.10
    enemy_2XPosition -= 0.15
    enemy_3XPosition -= 0.20
    prizeXPosition -= 0.08
    
    # ================The game loop logic ends here. =============
  
