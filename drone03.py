from codrone_edu.drone import *

drone = Drone()
drone.connect()

# Build your own buzzer

# Starting hertz (262 is middle C)
start = 262
# Ending hertz (523 is one octave above middle C)
end = 523
# Total duration (250 ms will play the entire song through that 250 ms)
# 300 should be a rough minimum (bare minimum, it kind of breaks at 300)
duration = 400
# How many different notes play
split = 4

length = end - start
print(length)
soundChange = int(length / split)
print(soundChange)

drone.set_drone_LED(255, 0, 0, 100)
time.sleep(1)
drone.set_drone_LED(0, 255, 0, 100)

for i in range(split):
    drone.drone_buzzer(start + (i * soundChange), int(duration / split))

drone.set_drone_LED(0, 0, 255, 100)
drone.drone_buzzer(end, 500)

drone.disconnect()