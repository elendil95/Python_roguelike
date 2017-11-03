# X FIRST, Y SECOND!!!

###########
# Convention is to use underscores for variables instead of camel case in Python, however i'm not gonna 
# touch it in case they are standard functions from libtcod
# Note to Self: end of fuctions and control-flow constructs is determined by indentation, not curly braces!
#
# Python is not object oriented like Java! define functions before you call them, even when using classes 
# and/or inheritance!
###########
import libtcodpy as libtcod # Can the name be arbitrary?

SCREEN_WIDTH=80
SCREEN_HEIGHT=50
#MAX_FPS=20

class Object:
    def __init__(self, x, y, char, color): # This is basically a constructor # there's two underscores!
        self.x=x
        self.y=y
        self.char=char
        self.color=color

    def move (self, distance_x, distance_y):
        self.x += distance_x
        self.y += distance_y

    def draw(self):
        libtcod.console_set_default_foreground(con, self.color)
        libtcod.console_put_char(con, self.x, self.y, self.char, libtcod.BKGND_NONE)

    def clear(self):
        libtcod.console_put_char(con, self.x, self.y, ' ', libtcod.BKGND_NONE)

# Function (Java's "method") to define wich key correspond to what action. Does it modify the player_*pos outside the function aswell? is  it limited in scope?
def handle_keys():
    key = libtcod.console_wait_for_keypress(True) 
    if key.vk == libtcod.KEY_ESCAPE:
        return True

    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        player.move(0, -1)
    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        player.move(0, 1)
    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        player.move(-1, 0)
    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        player.move(1, 0)           


# SCREEN INIT
libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Test', False) # the 'root' console will be number 0 (stdout). 3rd parameters is window title, 4th is fullscreen bool
con=libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT) # secondary console
# Setting up player and npc
player=Object(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, '@', libtcod.white)
npc=Object(SCREEN_WIDTH/2-5, SCREEN_HEIGHT/2, '@', libtcod.yellow)
objects=[npc, player]        

#MAIN LOOP: setup console, place @ and wait for presses. The second console_put_char applies to the previous coordinates, to avoid having a trail of @.
while not libtcod.console_is_window_closed():
    libtcod.console_set_default_foreground(0, libtcod.white) # the 0 parameter should be output device, aka stdout
    for object in objects:
    	object.draw()

    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
    libtcod.console_flush() #look this up
    
    for object in objects:
    	object.clear()
    
    exit=handle_keys()
    if exit:
        break

#####
# I don't understand why exit=handle_keys() is after the flush() function, and also what's up with the way we call the handle_keys() function
#####



#MAIN LOOP: setup console, place @ and wait for presses. The second console_put_char applies to the previous coordinates, to avoid having a trail of @.
# while not libtcod.console_is_window_closed():
#    libtcod.console_set_default_foreground(0, libtcod.white) # the 0 parameter should be output device, aka stdout
#    libtcod.console_put_char(con, player_xpos, player_ypos, '@', libtcod.BKGND_NONE) # X FIRST, Y SECOND!
#    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
#    libtcod.console_flush() #look this up
#    libtcod.console_put_char(con, player_xpos, player_ypos, ' ', libtcod.BKGND_NONE)
#    exit=handle_keys()
#    if exit:
#        break
