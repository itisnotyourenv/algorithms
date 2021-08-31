from main import func_timer

A = [25, 1, 19, 22, 9, 18, 30, 24, 34, 25, 49, 15, 13, 10, 1, 0, 32, 6, 40, 34]


@func_timer
def insertion_sort(sort_list: list) -> list:
    for i in range(1, len(sort_list)):
        while sort_list[i] < sort_list[i - 1] and i != 0:
            sort_list[i - 1], sort_list[i] = sort_list[i], sort_list[i - 1]
            i -= 1
    return sort_list


print(insertion_sort(A))
