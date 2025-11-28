package main

import (
	"fmt"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {

	domain := r.URL.Query().Get("domain")

	if domain == "" {
		return
	}
	fmt.Print(domain)

}

func main() {

	http.HandleFunc("/lookup", func(w http.ResponseWriter, r *http.Request) {
		handler(w, r)
	})

	if err := http.ListenAndServe(":8080", nil); err != nil {
		fmt.Println("Failed to start service.")
	} else {
		fmt.Println("Service started and listening at port 8080.")
	}

}
