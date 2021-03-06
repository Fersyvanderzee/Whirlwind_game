from gpiozero import LEDBoard, Button
from time import sleep
from signal import pause

# Buttons
lbutton = Button(3)
rbutton = Button(2)

# Leds
leds = LEDBoard(21, 20, 16, 26, 19, 13, 6, 12, 5)


#sleep
s = 0.05


#main menu
def main_menu():
    main_menu = True

    while main_menu == True:    
        for led in leds:
            if lbutton.is_pressed and rbutton.is_pressed:
                leds.on(2)
                leds.on(6)
                sleep(1)
                leds.off()
                leds.on(3)
                leds.on(5)
                sleep(1)
                leds.off()
                leds.on(4)
                main_menu = False
                break
            led.on()
            sleep(1)
            led.off()


def game():
    #score [left p, right p]
    p1_score = 0
    p2_score = 0
    game_active = True
    lights_up = True
    i = 0
    while game_active == True:
        for led in leds:
            if i==0 and lbutton.is_pressed:
                p1_score = p1_score + 1
                game_active = False
            elif i==8 and rbutton.is_pressed:
                p2_score = p2_score + 1
                game_active = False
                
            
            if i < 9 and lights_up == True:
                leds[i].on()
                sleep(s)
                leds.off()
                i += 1
                if i == 8:
                    lights_up = False
            
            if i > -1 and lights_up == False:
                leds[i].on()
                sleep(s)
                leds.off()
                i -= 1
                if i == 0:
                    lights_up = True         


#triggers
main_menu()
game()



# Controller

def lbutton_press():
    print("Left test")
    
def rbutton_press():
    print("Right test")

lbutton.when_pressed = lbutton_press
rbutton.when_pressed = rbutton_press
pause()





