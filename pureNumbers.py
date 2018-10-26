
import math


# pureNumbers calculates the amount of green coffee and each batch size necessary for
# roasting a particular wholesale customer coffee exactly.

#Variables


# pure coffee recipe

# 60% org nic nortena

# green to roasted coffee yields

# nic = 0.83870968

#determine roasted coffee individual

total_coffee_needed = 400
nic_needed = total_coffee_needed * 0.6

#determine green coffee individual

greennic_needed = nic_needed / 0.83870968

#declare min/max_batch

min_batch = 45
max_batch = 62

#round up green nic needed and add 3 for margin of error

greennic_needed = math.ceil(greennic_needed)

# number of roasts

n_of_roasts = greennic_needed / max_batch

# x is batch number minus remainder

x = [x for x in range(10000) if n_of_roasts - x > 0][-1]

# calculate remaining amount needed

remainder = n_of_roasts - x

# calculate last batch size

last_batch = remainder * max_batch

print(n_of_roasts)
print(x +1)
print(remainder)
print(last_batch)
