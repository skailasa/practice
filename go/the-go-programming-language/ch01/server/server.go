/*
A minimal web server
 */

package main

import (
	"fmt"
	"log"
	"net/http"
	"strconv"
	"sync"

	)

var mu sync.Mutex
var count int

func main() {
	http.HandleFunc("/", handler) //each request calls handler
	http.HandleFunc("/count", counter) //A url that returns num of requests
	http.HandleFunc("/lissajous", func(w http.ResponseWriter, r *http.Request) {
		query_vals := r.URL.Query()
		scycles := query_vals.Get("cycles")

		fcycles, _ := strconv.ParseFloat(scycles, 64)
		lissajous(w, fcycles)
	})
	log.Fatal(http.ListenAndServe("localhost:8000", nil))
}


// Echoes the Path component of the requested URL
func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "%s %s %s %s\n", r.Method, r.URL, r.Proto)
	for k, v := range r.Header {
		fmt.Fprint(w, "Header[%q] = %q\n", k, v)
	}
	fmt.Fprintf(w, "Host = %q\n", r.Host)
	fmt.Fprintf(w, "RemoteAddr = %q\n", r.RemoteAddr)
	if err := r.ParseForm(); err != nil {
		log.Print(err)
	}
	for k, v := range r.Form {
		fmt.Fprintf(w, "Form[%q] = %q\n", k, v)
	}
}


// Echoes the number of calls so far
func counter(w http.ResponseWriter, r *http.Request) {
	mu.Lock()
	fmt.Fprintf(w, "Count %d\n", count)
	mu.Unlock()
}
