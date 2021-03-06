from gpiozero import LED, Button
from time import sleep
from signal import pause


# coordinates LEDs
coords = 2

# controller pinouts
r = Button(2)
l = Button(3)

# LED pin outs
led1 = LED(23)
led2 = LED(22)
led3 = LED(27)
led4 = LED(18)
led5 = LED(17)


# LEDs action
def led1_on():
    led1.on()
    led2.off()
    led3.off()
    led4.off()
    led5.off()
    
def led2_on():
    led1.off()
    led2.on()
    led3.off()
    led4.off()
    led5.off()

def led3_on():
    led1.off()
    led2.off()
    led3.on()
    led4.off()
    led5.off()
    
def led4_on():
    led1.off()
    led2.off()
    led3.off()
    led4.on()
    led5.off()

def led5_on():
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    led5.on()

    
# right button
def pressed_right():
    print("Right is pressed")
    
    global coords
    if coords < 4:
        coords += 1
        
    if coords == 0:
        led1_on()
    
    if coords == 1:
        led2_on()
    
    if coords == 2:
        led3_on()
        
    if coords == 3:
        led4_on()
        
    if coords == 4:
        led5_on()
    print("Coords: " + str(coords))


# left button    
def pressed_left():
    print("Left is pressed")
    
    global coords
    if coords > 0:
        coords -= 1
        
    if coords == 0:
        led1_on()
    
    if coords == 1:
        led2_on()
    
    if coords == 2:
        led3_on()
        
    if coords == 3:
        led4_on()
        
    if coords == 4:
        led5_on()
    print("Coords: " + str(coords))    


# controller
r.when_pressed = pressed_right
l.when_pressed = pressed_left
pause()

#led_action = [led1_on(), led2_on(), led3_on(), led4_on(), led5_on()]
#led_action[1]
