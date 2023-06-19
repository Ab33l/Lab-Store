package handlers

import (
	"fmt"
	"net/http"
)

func Handler1(w http.ResponseWriter, r *http.Request) {
	// Handler logic for route 1
	fmt.Fprintln(w, "Handler 1")
}
