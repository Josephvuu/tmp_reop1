# Name: Joseph Vu
# Student ID: 887091577
# Section: 07
# Assignment: Module 6 Assignment 5

def comp_avg(*args):
    total = 0
    count = 0
    for num in args:
        total += num
        count += 1
    return total / count if count > 0 else 0


def comp_max(*args):
    largest = args[0]
    for num in args:
        if num > largest:
            largest = num
    return largest


def comp_min(*args):
    smallest = args[0]
    for num in args:
        if num < smallest:
            smallest = num
    return smallest