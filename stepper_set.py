# Rui Santos & Sara Santos - Random Nerd Tutorials
# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-stepper-motor-micropython/

import stepper
from time import sleep
import network

wlan = network.WLAN()
print(wlan.active())

# Define the stepper motor pin 1
IN1 = 13
IN2 = 12
IN3 = 14
IN4 = 27

# Define the stepper motor pin 2
IN5 = 26
IN6 = 25
IN7 = 33
IN8 = 32

# Define the stepper motor pin 3
IN9 = 2
IN10 = 4
IN11 = 23
IN12 = 22

# Define the stepper motor pin 4
IN13 = 21
IN14 = 19
IN15 = 18
IN16 = 5

# Define the stepper motor pin leg 1
IN17 = 13
IN18 = 12
IN19 = 14
IN20 = 27

# Define the stepper motor leg 2
IN21 = 26
IN22 = 25
IN23 = 33
IN24 = 32

# Define the stepper motor leg 3
IN25 = 2
IN26 = 4
IN27 = 23
IN28 = 22

# Define the stepper motor leg 4
IN29 = 21
IN30 = 19
IN31 = 18
IN32 = 5




# Initialize the stepper motor
stepper_motor1 = stepper.HalfStepMotor.frompins(IN1, IN2, IN3, IN4, stepms = 2) #stepms to add time to reduce overheating and ensure smoother operation
stepper_motor2 = stepper.HalfStepMotor.frompins(IN5, IN6, IN7, IN8, stepms = 2 )
stepper_motor3 = stepper.HalfStepMotor.frompins(IN9, IN10, IN11, IN12, stepms = 2)
stepper_motor4 = stepper.HalfStepMotor.frompins(IN13, IN14, IN15, IN16, stepms = 2)

# leg
stepper_motor5 = stepper.HalfStepMotor.frompins(IN17, IN18, IN19, IN20, stepms = 2) 
stepper_motor6 = stepper.HalfStepMotor.frompins(IN21, IN22, IN23, IN24, stepms = 2 )
stepper_motor7 = stepper.HalfStepMotor.frompins(IN25, IN26, IN27, IN28, stepms = 2)
stepper_motor8 = stepper.HalfStepMotor.frompins(IN29, IN30, IN31, IN32, stepms = 2)

# stepper_motor1, stepper_motor2, stepper_motor3, stepper_motor4 = my_stepper1  

# Set the current position as position 0
#stepper_motor.reset()

# stepper_motor.step_until_angle(30)
# sleep(0.5) # stop for a while

# stepper_motor.step(200)
# sleep(0.5)
# stepper_motor.step_degrees(60)
# sleep(0.5)

def angle():
    for motor in [stepper_motor1, stepper_motor2, stepper_motor3, stepper_motor4]:
            motor.step(200)
#             sleep(0.5)
#             motor.step(-200)
#             sleep(0.5)
def leg_base():
    for motor in [stepper_motor5, stepper_motor6, stepper_motor7, stepper_motor8]:
            motor.step_angle(70)
#             sleep(0.5)
#             motor.step(-200)
#             sleep(0.5)
leg_base()
    
# try:
#     while True:
#     angle()
#     sleep (1)
#     leg_base()
        
#         #Move 500 steps in clockwise direction
# #         stepper_motor.step(500)
# #         sleep(0.5) # stop for a while
        
#         # Move 500 steps in counterclockwise direction
#         #stepper_motor.step(-500)
#         #sleep(0.5) # stop for a while
        
#         # Go to a specific position (in steps)
#         #stepper_motor.step_until(2000)
#         #sleep(0.5) # stop for a while
        
#         # Force a direction using the dir paramter
#         #stepper_motor.step_until(2000, dir=-1)
#         #sleep(0.5) # stop for a while        
        
#         # Go to a specific position (angle, maximum is 359, otherwise it will spin indefinetely)
#         #sleep(0.5)
        
#         #stepper_motor.step_until_angle(30)
#         #sleep(0.5) # stop for a while
        
#         #stepper_motor.reset()
        
        
    
# except KeyboardInterrupt:
#     print('Keyboard interrupt')
