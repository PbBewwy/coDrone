from codrone_edu.drone import *

drone = Drone()
drone.pair()

drone.takeoff()
drone.hover(1)

gurt = 0.68

drone.move_forward(88 * gurt, "in", 1)
drone.turn_right(90)
drone.move_forward(40 * gurt, "in", 1)
drone.turn_left(90)
drone.move_forward(80 * gurt, "in", 1)
drone.turn_right(90)
drone.move_forward(80 * gurt, "in", 1)

drone.land()
drone.close()
# 88 R 46 L 72 R 91