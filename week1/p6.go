package main

import (
	"fmt"
	"strconv"
	"strings"
)

func dectobin(d int64) string {
	if d > 1 {
			return fmt.Sprintf("%s%d", dectobin(d / 2), d % 2)
	} else {
			return strconv.Itoa(int(d))
	}
}

func flippingBits(n int64) int {
	targetBin := dectobin(n)
	toFill := 32 - len(targetBin)
	targetBin = fmt.Sprintf("%s%s", strings.Repeat("0", toFill), targetBin)
	flip := ""
	for _, v := range targetBin {
			if string(v) == "1" {
					flip += "0"
			} else {
					flip += "1"
			}
	}
	output, _ := strconv.ParseInt(flip, 2, 64)
	return int(output)
}

func main() {
	// s := fmt.Sprintf("%0*d%s", 7, "HELLO")
	fmt.Printf("%-[2]*[1]s", "0", 7)
}