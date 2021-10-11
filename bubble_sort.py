from services import func_timer

A = [25, 1, 19, 22, 9, 18, 30, 24, 34, 25, 49, 15, 13, 10, 1, 0, 32, 6, 40, 34]


@func_timer
def bubble_sort(sort_list: list) -> list:
    array_list = len(sort_list) - 1
    for i in range(array_list):
        for j in range(array_list - i):
            if sort_list[j] > sort_list[j + 1]:
                sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]
    return sort_list


print(bubble_sort(A))
