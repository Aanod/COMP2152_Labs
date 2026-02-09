# a:
# Author: Aanod Mohamed
# Assignment 1


# b:
gym_member = "Nia Decosta" # data type: string
preferred_weight_kg = 61.2 # data type: double
highest_reps = 20 # data type: integer
membership_active = True # data type: boolean

gym_member = "Bill Gunn" # data type: string
preferred_weight_kg = 92.2 # data type: double
highest_reps = 45 # data type: integer
membership_active = True # data type: boolean

gym_member = "Kassi Lemons" # data type: string
preferred_weight_kg = 51.3 # data type: double
highest_reps = 18 # data type: integer
membership_active = True # data type: boolean

gym_member = "Barry Jenkins" # data type: string
preferred_weight_kg = 76.7 # data type: double
highest_reps = 21 # data type: integer
membership_active = True # data type: boolean

# c:
# data type: dict
# in order of minutes on, yoga then running then weight lifting 
workout_stats = {"Nia Decosta":(20, 40, 25), "Bill Gunn":(10, 60, 30), "Kassi Lemons":(61, 30, 12), "Barry Jenkins":(33, 40, 50)}

# d:
for friend in list(workout_stats):
    stats = workout_stats[friend]  
    sum = 0
    for stat in stats:
        sum = sum + stat
    workout_stats[friend + "_total"] = sum

# e:
# data type: list, specifically it is a 2 dimensional list but its data type is still list
workout_list = []

workout_minutes = list(workout_stats.values())
for minutes in workout_minutes [0:4]:
    workout_list.append(list(minutes))

# f:
yoga_running_minutes = [] 
for friends in workout_list:
    for friend in friends [0:2]:
        yoga_running_minutes.append(friend)
print(yoga_running_minutes)


lifting_minutes = []
for friends in workout_list[2:4]:
    for friend in friends [2:3]:
        lifting_minutes.append(friend)
print(lifting_minutes)

# g:
for friend in list(workout_stats)[4:8]:
    total_min = workout_stats[friend]
    if total_min >= 120:
        name = friend.replace("_total", "")
        print("Great job staying active, " + name)

# h:        
name = input("Enter a friend's name to see if they are in the system: ")

if name in workout_stats:
    fdata = workout_stats[name] 
    print("-------------------------------------------------------------------------")
    yoga_int = fdata[0]
    yoga = str(yoga_int)
    print("Yoga: " + yoga + " minutes")
    running_int = fdata[1]
    running = str(running_int)
    print("Running: " + running + " minutes")
    lifting_int = fdata[2]
    lifting = str(lifting_int)
    print("Weight lifting: " + lifting + " minutes")
    total_int = yoga_int + running_int + lifting_int
    total = str(total_int)
    print("Total: " + total + " minutes")
    print("-------------------------------------------------------------------------")
else:
    print("Sorry " + name + " is not found in the records.")
# i:
total_keys = list(workout_stats)[4:8]
highest_total = total_keys[0]
lowest_total = total_keys[0]
for friend in total_keys:
    if workout_stats[friend] > workout_stats[highest_total]:
         highest_total = friend
    if workout_stats[friend] < workout_stats[lowest_total]:
         lowest_total = friend

highest_int = workout_stats[highest_total]
highest = str(workout_stats[highest_total])
highest_friend = highest_total.replace("_total", " ")
print("The highest total workout minutes: " + highest + " by " + highest_friend)

lowest_int = workout_stats[lowest_total]
lowest = str(workout_stats[lowest_total])
lowest_friend = lowest_total.replace("_total", " ")
print("The lowest total workout minutes: " + lowest + " by " + lowest_friend)
