/*
Program to fetch a URL, and print contents
 */

package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {
	for _, url := range os.Args[1:] {

		var query string

		if pref := url[:8]; pref != "https://" {
			query = "https://" + url
		} else {
			query = url
		}

		resp, err := http.Get(query)
		if err != nil {
			fmt.Fprint(os.Stderr, "fetch: %v\n", err)
			os.Exit(1)
		}
		defer resp.Body.Close()

		_, err1 := io.Copy(os.Stdout, resp.Body)
		if err1 != nil {
			fmt.Fprintf(os.Stderr, "fetch: reading %s: %v\n", url, err1)
			os.Exit(1)
		}
	}
}