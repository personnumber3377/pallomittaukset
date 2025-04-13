
# The first stuff:

# The speed of the ball is 950mm/s so 0.95m/s

def ek(mass, v):
	return 1/2*mass*(v**2) # Kinetic energy formula

ball_1_v1 = 0.95 # meters per second.
ball_mass = 0.24 / 1000.0 # grams to kilograms. This is the mass of an airsoft bb.

initial_energy = ek(ball_mass, ball_1_v1) # Calculate kinetic energy at the start...

ball_1_v2 = 0.330 # 330mm/s average taken from the tail end...

ball_2_v2 = 0.500 # 500mm/s average taken from the tail end of the graph

# Now calculate the difference in kinetic energy.

d_Ek = initial_energy - (ek(ball_mass, ball_1_v2) + ek(ball_mass, ball_2_v2)) # Now do the stuff..

assert d_Ek >= 0 # Energy should be lost...

print("Difference in kinetic energy: "+str(d_Ek))

# Now calculate the percentage of energy lost.

quotient = d_Ek / initial_energy

print(quotient*100)

# The second measurements (coming soon)




