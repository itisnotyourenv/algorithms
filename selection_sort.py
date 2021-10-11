from services import func_timer

A = [25, 1, 19, 22, 9, 18, 30, 24, 34, 25, 49, 15, 13, 10, 1, 0, 32, 6, 40, 34]


@func_timer
def selection_sort(sort_list: list) -> list:
    for i in range(len(sort_list)):
        min_value = i
        for j in range(i, len(sort_list)):
            if sort_list[j] < sort_list[min_value]:
                min_value = j
        sort_list[i], sort_list[min_value] = sort_list[min_value], sort_list[i]
    return sort_list


print(selection_sort(A))