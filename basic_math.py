#######################
# Basic Math          #
#######################


def get_greatest(number_list):
    greatest_number = number_list[0]

    for i in number_list:
        if i > greatest_number:
            greatest_number = i

    return greatest_number


def get_smallest(number_list):
    smallest_number = number_list[0]

    for i in number_list:
        if i < smallest_number:
            smallest_number = i

    return smallest_number


def get_mean(number_list):
    mean = None
    sum = 0

    for i in number_list:
        sum += i
    mean = sum / len(number_list)

    return mean


def get_median(number_list):
    median = None
    length = len(number_list)

    number_list.sort()
    if length % 2:
        median = number_list[length / 2]
    else:
        median = float(
            (number_list[length / 2 - 1] + number_list[length / 2])) / 2

    return median
