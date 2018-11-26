# Randomly creates a list of numbers between 0-10 of length between 5-8 elements.
# Check if the generated list can be partitioned into 2 sub-lists of equal sums.


import random


def partition(inp_list):
    sorted_inp = sorted(inp_list, reverse=True)
    first_list = []
    second_list = []
    for num in sorted_inp:
        if sum(first_list) < sum(second_list):
            first_list.append(num)
        else:
            second_list.append(num)

    print('Sublists are {} and {}'.format(first_list, second_list))

    return sum(first_list) == sum(second_list)


if __name__ == '__main__':
    random_length = random.randint(5, 8)
    input_list = random.sample(range(10), random_length)  # Generate a random List of length random_length
    print('Input List is : {}'.format(input_list))
    if partition(input_list):
        print('The list can be split into 2 lists with equal sums..!')
    else:
        print('The list can not be split into 2 lists with equal sums..!')
