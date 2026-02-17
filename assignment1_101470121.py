"""
Author: Emir Sadi
Assignment: #1
"""

# Step b: Create 4 variables

# gym_member is a string (str)
gym_member = "Alex Alliton"

# preferred_weight_kg is a float
preferred_weight_kg = 20.5

# highest_reps is an integer (int)
highest_reps = 25

# membership_active is a boolean (bool)
membership_active = True


# Step c: Create a dictionary named workout_stats
# workout_stats is a dictionary (dict) with string keys and tuple values

workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (40, 35, 25),
    "Taylor": (25, 50, 30)
}


# Step d: Calculate total workout minutes and add to dictionary

for friend in list(workout_stats.keys()):
    total_minutes = sum(workout_stats[friend])
    workout_stats[friend + "_Total"] = total_minutes


# Step e: Create a 2D nested list called workout_list
# workout_list is a list of lists

workout_list = []

for friend in ["Alex", "Jamie", "Taylor"]:
    workout_list.append(list(workout_stats[friend]))


# Step f: Slice the workout_list

# Yoga and Running for all friends
print("Yoga and Running minutes for all friends:")
for row in workout_list:
    print(row[:2])

print()

# Weightlifting for last two friends
print("Weightlifting minutes for last two friends:")
for row in workout_list[-2:]:
    print(row[2])

print()


# Step g: Check if any friend's total >= 120

for friend in ["Alex", "Jamie", "Taylor"]:
    if workout_stats[friend + "_Total"] >= 120:
        print(f"Great job staying active, {friend}!")

print()


# Step h: User input lookup

user_input = input("Enter a friend's name: ")

if user_input in workout_stats:
    minutes = workout_stats[user_input]
    total = workout_stats[user_input + "_Total"]
    print(f"{user_input}'s workout minutes (Yoga, Running, Weightlifting): {minutes}")
    print(f"Total workout minutes: {total}")
else:
    print(f"Friend {user_input} not found in the records.")

print()


# Step i: Highest and lowest total workout minutes

highest_friend = ""
lowest_friend = ""
highest_total = -1
lowest_total = float('inf')

for friend in ["Alex", "Jamie", "Taylor"]:
    total = workout_stats[friend + "_Total"]
    
    if total > highest_total:
        highest_total = total
        highest_friend = friend
        
    if total < lowest_total:
        lowest_total = total
        lowest_friend = friend

print("Friend with highest total workout minutes:", highest_friend)
print("Friend with lowest total workout minutes:", lowest_friend)
