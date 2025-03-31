
'''

Notes:

ok, so the first run was filmed with 138.8 fps

'''

import matplotlib.pyplot as plt
import numpy as np

def load_data():
	import csv

	even_rows = []  # 0-based: index 0, 2, 4, ...
	odd_rows = []   # index 1, 3, 5, ...

	with open("data run 1.csv", newline='') as csvfile:
		reader = list(csv.reader(csvfile))
		header = reader[0]  # save the header if needed
		data = reader[1:]   # skip header
		# The data is stored in a funky way. Every other line is the other ball and every other is the other one.
		for i, row in enumerate(data):
			if i % 2 == 0:
				even_rows.append(row)
			else:
				odd_rows.append(row)

	# print("Even rows:", even_rows[:3])
	# print("Odd rows:", odd_rows[:3])
	# Only get the x coordinates, which matter.
	ball_1_x = [float(x[1]) for x in odd_rows]
	ball_2_x = [float(x[1]) for x in even_rows	]
	return ball_1_x, ball_2_x

def main():
	# Now do the thing...

	ball1, ball2 = load_data() # The ball1 is the first ball and ball2 is the second ball.
	# Now we have the x coordinates of both balls.
	# Now plot velocity.
	assert len(ball1) == len(ball2) # Should be equal.

	# Now plot position over time...

	# Time
	fps = 138.8 # The fps which we filmed with...
	time_in_frame = 1.0 / fps
	time_stuff = [i*time_in_frame for i in range(len(ball1))]

	plt.plot(time_stuff, ball1, label='Object 1')
	plt.plot(time_stuff, ball2, label='Object 2')

	# Use numpy.gradient to estimate derivative
	speed_even = np.gradient(ball1, time_stuff)
	speed_odd = np.gradient(ball2, time_stuff)

	# Plot the speed
	plt.plot(time_stuff, speed_even, label="Speed of Object 1 (even)")
	plt.plot(time_stuff, speed_odd, label="Speed of Object 2 (odd)")
	
	plt.xlabel("Time (seconds)")
	plt.ylabel("Position")
	plt.title("Position Over Time")
	plt.legend()
	plt.grid(True)
	plt.show()

	return

if __name__=="__main__":
	main()
	exit()
