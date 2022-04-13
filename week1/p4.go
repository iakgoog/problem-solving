package main

import "fmt"

func matchingStrings(strings []string, queries []string) []int {
	count := make(map[string]int)
	var result []int
	for _, v := range strings {
		if _, ok := count[v]; ok {
			count[v] += 1
		} else {
			count[v] = 1
		}
	}
	for _, v := range queries {
		if val, ok := count[v]; ok {
			result = append(result, val)
		} else {
			result = append(result, 0)
		}
	}

	return result
}

func main() {
	strings := []string{"abcde", "sdaklfj", "asdjf", "na", "basdn", "sdaklfj", "asdjf", "na", "asdjf", "na", "basdn", "sdaklfj", "asdjf"}
	queries := []string{"abcde", "sdaklfj", "asdjf", "na", "basdn"}

	fmt.Println(matchingStrings(strings, queries))
}