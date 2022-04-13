package main

import (
	"fmt"
	"strconv"
)

func lonelyinteger(arr []int32) int {
	count := make(map[string]int)
	for _, v := range arr {
    i := strconv.Itoa(int(v))
    if _, ok := count[i]; ok {
      count[i] += 1
    } else {
      count[i] = 1
    }
	}
	for k, v := range count {
    if v == 1 {
      ct, err := strconv.Atoi(k)
      if err == nil {
        return ct
      }
    }
	}
	return -1
}

// [1,2,3,4,3,2,1]

func main() {
	fmt.Println(lonelyinteger([]int32{1,2,3,4,3,2,1}))
}