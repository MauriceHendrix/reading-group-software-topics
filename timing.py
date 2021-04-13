import time

def square_of_negative_in_list(lst):
    squares_in_list = True
    for v in lst:
        if v < 0:
            square_found = False
            for v2 in lst:
                square_found = square_found or v2 == v**2
            squares_in_list = squares_in_list and square_found
    return squares_in_list

def square_of_negative_in_list2(lst):
    found_squares = set()
    for v in lst:
        if v > 0:
            found_squares.add(v)
    for v in lst:
        if v < 0 and not v**2 in found_squares:
            return False
    return True

    

def time_call(lst, func, reps):
    tic = time.time()
    for i in range(reps):
        func(lst)
    toc = time.time()
    return float((toc-tic) / reps)

list1 = [-1, -6, -9, 0, 148, 1, 36, 81, 148]
list2 = [-v for v in range(2000)]
list2 = list2 + [v**2 for v in list2]


print('square_of_negative_in_list on list1 takes: %s s' % time_call(list1, square_of_negative_in_list, 1000))
print('square_of_negative_in_list3 on list1 takes: %s s' % time_call(list1, square_of_negative_in_list2, 1000))
print()
print('square_of_negative_in_list on list2 takes: %s s' % time_call(list2, square_of_negative_in_list, 5))
print('square_of_negative_in_list3 on list2 takes: %s s' % time_call(list2, square_of_negative_in_list2, 5))

def list_test(rng):
    lst = []
    for i in range(rng):
        lst.append(i)

def tuple_test(rng):
    tpl = tuple()
    for i in range(rng):
        tpl = tpl + (i, )

print()
print('adding numbers to list takes: %s s' % time_call(50000, list_test, 5))
print('creating new tuple takes: %s s' % time_call(50000, tuple_test, 5))


example_dist_list = [{'name': 'Earth', 'num_moons': 1},
                     {'name': 'Jupiter', 'num_moons': 53},
                     {'name': 'Saturn', 'num_moons': 53},
                     {'name': 'Uranus', 'num_moons': 27},
                     {'name': 'Neptune', 'num_moons': 14}]

example_dist_list.sort(key=lambda p: p['num_moons'], reverse=True)
print(example_dist_list)

                     