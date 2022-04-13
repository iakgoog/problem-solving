package main

import (
	"fmt"
	"sort"
)

type arr32 []int32

func miniMaxSum(arr []int32) string {
	var s arr32 = arr
	sort.Slice(s, func(i, j int) bool { return s[i] < s[j]})
	var minSet []int32 = s[0:len(s)-1]
	var maxSet []int32 = s[1:]
	var minVal int64 = 0
	for _, v := range minSet {
		minVal += int64(v)
	}
	var maxVal int64 = 0
	for _, v := range maxSet {
		maxVal += int64(v)
	}
	
	return fmt.Sprintf("%d %d", minVal, maxVal)
}

func main() {
	fmt.Println("Welcome to the playground!")

	// fmt.Println(miniMaxSum(arr32{256741038, 623958417, 467905213, 714532089, 938071625}))
	fmt.Println(miniMaxSum(arr32{1, 2, 3, 4, 5}))
}
