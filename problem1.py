# Problem 1
def multiples_of_3_or_5(last):
    # If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    # The sum of these multiples is 23.
    # Find the sum of all the multiples of 3 or 5 below 1000.

    multiples = []
    sum_of_all_multiples = 0

    # find the multiples of 3 and 5 and store in a list
    for i in range(1, last):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)

    # iterate through the list and cumulatively sum them
    # (Could just do this in the for loop above instead of
    #  making a list)
    for multiple in multiples:
        sum_of_all_multiples += multiple
    print(sum_of_all_multiples)


if __name__ == '__main__':
    multiples_of_3_or_5(1000)     # Answer: 233168
