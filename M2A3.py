# Name: Joseph Vu
# Student ID: 887091577
# Section: 07
# Assignment: Module 2 Assignment 3

uber_list = list(range(100, 200, 2))

start_slice = int(input("What is the start of your slice? "))
end_slice = int(input("What is the end of your slice? "))

data_list = uber_list[start_slice:end_slice]

total_int = 0
for num in data_list:
    total_int += num

average_value = total_int / len(data_list) if len(data_list) > 0 else 0.0

print(f"Your slice contains {len(data_list)} values and has an average value of {average_value}")


