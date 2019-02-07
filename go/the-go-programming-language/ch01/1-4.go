/*
Modify duplicate finder to print the name of the files
containing duplicates.
*/

package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	counts := make(map[string]int)
	files := os.Args[1:]

	for _, arg := range files {
		f, err := os.Open(arg)
		if err != nil {
			continue
		}
		if checkDuplicates(f, counts) {
			fmt.Println(arg)
		}
		f.Close()
	}
}

func checkDuplicates(f *os.File, counts map[string]int) bool{
	input := bufio.NewScanner(f)
	for input.Scan() {
		counts[input.Text()]++
	}

	var res bool

	for _, n := range counts{
		if n > 1 {
			res = true
		} else {
			res = false
		}
	}
	return res
}

