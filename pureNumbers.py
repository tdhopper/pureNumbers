
import math


# pureNumbers calculates the amount of green coffee and each batch size necessary for
# roasting a particular wholesale customer coffee exactly.

#Variables


# pure coffee recipe

# 60% org nic nortena

# green to roasted coffee yields

# nic = 0.83870968

#determine roasted coffee individual

total_coffee_needed = 500
nic_needed = total_coffee_needed * 0.6

#determine green coffee individual

greennic = nic_needed / 0.83870968

#declare last batch



while(lb < 45):
    b = 62
    nic = nic / 0.83870968
    tr = math.ceil(nic)
    n = tr / b
    x = [x for x in range(10000) if n - x > 0][-1]
    r = n - x
    lb = r * b
    n = x + 1


print("You need to do " + str(n) + " batches total.")
print("You should do " +  str(n-1) + " batches of " + str(b) + " and 1 batch of " + str(lb))