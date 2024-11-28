# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 
# Task 1
def f_to_c(f_temp):
  temp_c = (f_temp - 32) * 5/9
  return temp_c

# Task 2
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

# Task 3
def c_to_f(c_temp):
  temp_f = c_temp * (9/5) + 32
  return temp_f

# Task 4
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# Task 5
def get_force(mass, acceleration):
  return mass * acceleration

# Task 6
train_force = get_force(train_mass, train_acceleration)

# Task 6 & 7
print(f"The GE train supplies {train_force} Newtons of force.")

# Task 8
def get_energy(mass, c=3*10**8):
  return mass * c

# Task 9
bomb_energy = get_energy(bomb_mass)

# Task 10
print(f"A 1kg bomb supplies {bomb_energy} Joules")

# Task 11
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  work = force * distance
  return work

# Task 12
train_work = get_work(train_mass, train_acceleration, train_distance)

# Task 13
print(f'The GE train does {train_work} Joules of work over {train_distance} meters.')


