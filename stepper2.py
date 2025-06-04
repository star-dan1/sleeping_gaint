from wifi import Wifi
from communication import Communication
import stepper
from actions import Actions


stepper_motor5 = stepper.HalfStepMotor.frompins(IN17, IN18, IN19, IN20, stepms = 2) 
stepper_motor6 = stepper.HalfStepMotor.frompins(IN21, IN22, IN23, IN24, stepms = 2 )
stepper_motor7 = stepper.HalfStepMotor.frompins(IN25, IN26, IN27, IN28, stepms = 2)
stepper_motor8 = stepper.HalfStepMotor.frompins(IN29, IN30, IN31, IN32, stepms = 2)


def move(step=1000):
    for motor in [stepper_motor5, stepper_motor6, stepper_motor7, stepper_motor8]:
            motor.step(step)

def await_response():
    response = True
    while response:
        status, message = communicate.recieve_message()
        if status == "success" and message[0] == Actions.MOVE:
            move(message[1])
        elif status == "success" and message[0] == Actions.STOP:
            response = False
        response = False
    return True

wifi = Wifi()
wifi.set_AP()

communicate = Communication()
communicate.sendMessage("MOVE 500")
res = await_response()


