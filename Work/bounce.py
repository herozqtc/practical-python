# bounce.py
#
# Exercise 1.5
ball_height = 100 # in meters
bounce_factor = 0.6
num_bounces = 0

for i in range(10):
    ball_height = ball_height * bounce_factor
    num_bounces = num_bounces + 1
    print('Bounce', num_bounces, 'Height', round(ball_height, 4))