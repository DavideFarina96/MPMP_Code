# Solved by Davide Farina. Github: https://github.com/DavideFarina96
# My logic is that in the first train run, you can go maximum to train_range distance
# If you use a second run, you could take train_range/3 to distance train_range/3, and then come back
# In this case, then, you could go to a distance of train_range + 1/3*train_range
# In general, the rule is that every new run, you can go:
# 1, 1/3, 1/5, 1/7, ... further each time
# I keep the denominator value in variable "denominator"
# I increase it by 2 every time I decide to do a new train run
# If i see that I will need more runs after this one (aka, this run is not enough to reach my destination),
# then I fill the train to the max when leaving. This is calculated in the "if" block
# If i see that this would be the final run, I may be ok with using less than train_range fuel
# This is calculated in the "else" block
train_range = 500
total_distance = 800

distance_still_to_cover = total_distance
used_fuel = 0
denominator = 1

while(distance_still_to_cover > 0):
    max_distance_this_run = 1/denominator * train_range 
    if(max_distance_this_run <= distance_still_to_cover): 
        distance_still_to_cover -= 1/denominator * train_range
        used_fuel += train_range 
    else: 
        used_fuel += denominator * distance_still_to_cover
        distance_still_to_cover = 0
    denominator += 2
print(used_fuel)
