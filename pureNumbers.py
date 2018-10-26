



# pureNumbers calculates the amount of green coffee and each batch size necessary for
# roasting a particular wholesale customer coffee exactly.

#Variables

# tr = total roast (ex. 500 pounds of costa rica are needed)
# nic = org nic nortena
# costa = org costa rica lig
# col = org colombia la prima
# green = green coffee
# brown = roasted coffee
# b = batch size (ex. the roaster can roast 62 lbs at a time)
# n = number of roasts
# r = remainder
# lb = last batch

# pure coffee recipe

# 60% org nic nortena
# 15% org costa rica lig
# 25% org colombia la prima

# green to roasted coffee yields

# nic = 0.83870968
# costa = 0.8483871
# col = 0.8483871 *arbitrary*

#determine roasted coffee individual

nic = 500 * 0.6
costa = 500 * 0.15
col = 500 * 0.25

#determine green coffee individual

nic = nic / 0.83870968
costa = costa / 0.8483871
col = col / 0.8483871

#declare last batch

lb = 0

while(lb < 45):
    b = 62
    nic = 500 * 0.6
    nic = nic / 0.83870968
    tr = nic
    n = tr / b
    x = [x for x in range(10000) if n - x > 0][-1]
    r = n - x
    lb = r * b
    n = x + 1
    b - 1
print("You need to do " + str(n) + " batches total.")
print(b)
print(lb)