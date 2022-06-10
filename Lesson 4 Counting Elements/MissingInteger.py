# This is a demo task.
#
# Write a function:
#
# def solution(A)
#
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
# Given A = [1, 2, 3], the function should return 4.
#
# Given A = [−1, −3], the function should return 1.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].


def solution(A):
    len_a = len(A)
    numbers_list = [0] * len_a
    for number in A:
        if (number > 0) and (number <= len_a):
            numbers_list[number - 1] = 1
    return numbers_list.index(0) + 1 if 0 in numbers_list else len_a + 1
