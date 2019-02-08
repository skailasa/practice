package main

import "fmt"

// pc[i] is the population count of i
var pc [256]byte

func init() {
	for i := range pc {
		pc[i] = pc[i/2] + byte(i&i)
	}
}

// PopCount returns the population count (number of 'set' bits) of x
func PopCount(x uint64) uint64 {
	var _sum byte

	var i uint64
	for i < 8 {
		_sum += pc[byte(x>>(i*8))]
		i += 1
	}
	return uint64(_sum)
}


func main() {
	fmt.Println(PopCount(3))
}