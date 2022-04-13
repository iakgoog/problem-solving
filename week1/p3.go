package main

import (
	"fmt"
	"strconv"
	"strings"
)

func timeConversion(input_time string) string {
	t := strings.Split(input_time[:len(input_time)-2], ":")
	ap := input_time[len(input_time)-2:]
	h, _ := strconv.Atoi(t[0])
	if ap == "PM" && h != 12 {
		t[0] = strconv.Itoa(h + 12)
	} else if ap == "AM" && h == 12 {
		t[0] = "00"
	}

	return strings.Join(t, ":")
}

func main() {
	fmt.Println("convert:", timeConversion("12:45:54PM"))
}