from codrone_edu.drone import *

drone = Drone()
drone.pair()

print("Battery:", drone.get_battery(), "%")

drone.set_drone_LED(255, 0, 0, 100)
drone.drone_buzzer(440, 500)    # 440 Hz for 500 milliseconds
drone.takeoff()      # lift to about 80 cm and hover
drone.set_drone_LED(0, 255, 0, 100)
drone.hover(3)       # stay there for 3 seconds
drone.land()         # settle down
drone.set_drone_LED(255, 0, 0, 100)

drone.close()