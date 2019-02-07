// Recreate linux 'echo' command

package main

import (
	"fmt"
	"os"
	"strconv"
)

// Echo in a line, with the index and arg
func main() {
	sep := " "

	for idx, arg := range os.Args[1:] {
		str_idx := strconv.Itoa(idx)
		fmt.Println(str_idx+sep+arg)
	}
}
