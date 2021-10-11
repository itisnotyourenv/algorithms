package main

import "fmt"

func main() {
	A := []int{25, 1, 19, 22, 9, 18, 30, 24, 34, 25, 49, 15, 13, 10, 1, 0, 32, 6, 40, 34}
	sort_result := bubbleSort(A)
	fmt.Println(sort_result)
}

func bubbleSort(sort_list []int) []int {
	length := len(sort_list) - 1
	for i := 0; i < length; i++ {
		for j := 0; j < length; j++ {
			if sort_list[j] > sort_list[j+1] {
				sort_list[j+1], sort_list[j] = sort_list[j], sort_list[j+1]
			}
		}
	}
	return sort_list
}
