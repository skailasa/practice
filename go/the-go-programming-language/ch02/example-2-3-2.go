/*
Demonstration of pointers, for a simple echo command
 */
package main

import (
	"flag"
	"fmt"
	"strings"
)

// Both stored in pointers
var n = flag.Bool("n", false, "omit trailing newline")
var sep = flag.String("s", " ", "value of separator")

func main() {
	flag.Parse()
	fmt.Print(strings.Join(flag.Args(), *sep))
	if !*n {
		fmt.Println()
	}
}
