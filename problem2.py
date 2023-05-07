# Problem 2: Sum of even Fibonacci numbers
def calc_fibs(values):
    new = values[-1] + values[-2]
    values.append(new)
    return values


def fibonacci_numbers(last):
    fibs = [1, 1]
    while fibs[-1] < last:
        fibs = calc_fibs(fibs)
    print(sum_evens(fibs, last))


def sum_evens(fibs, last):
    sum_of_evens = 0
    for number in fibs:
        if number % 2 == 0 and number < last:
            sum_of_evens += number
    return sum_of_evens


if __name__ == '__main__':
    fibonacci_numbers(4000000)  # Answer: 4613732
