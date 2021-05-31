import copy


def shift(array, turns):
    if turns < 0:
        turns = abs(turns)
        for i in range(turns):
            array.append(array.pop(0))
    else:
        for i in range(turns):
            array.insert(0, array.pop())


def make_tau_list():
    tau = list(range(-500, 500))
    return tau


def make_new_list(array, turns):
    new_array = copy.deepcopy(array)
    shift(new_array, turns)
    return new_array


def count_sum(first, second):
    sum = 0
    for i in range(len(first)):
        sum += first[i] * second[i]
    return sum


def isNaN(num):
    return num != num


def delete_nan(first, second):
    temp1 = copy.deepcopy(first)
    temp2 = copy.deepcopy(second)
    for i in range(len(temp1)):
        if isNaN(temp1[i]):
            temp1[i] = 0
        if isNaN(temp2[i]):
            temp2[i] = 0
    return temp1, temp2


def correlation_function(first, second):
    correlation_function = []
    tau = make_tau_list()
    temp1, temp2 = delete_nan(first, second)
    for step in tau:
        new_array = make_new_list(temp2, step)
        correlation_function.append(count_sum(temp1, new_array))
    return tau, correlation_function


def normalization(correlation_function):
    norm_correlation_function = []
    minimal_elem = min(correlation_function)
    maximal_elem = max(correlation_function)
    for i in range(len(correlation_function)):
        norm_correlation_function.append((correlation_function[i] - minimal_elem) / (maximal_elem - minimal_elem))
    return norm_correlation_function

