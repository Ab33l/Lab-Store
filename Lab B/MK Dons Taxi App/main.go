package main

import (
	"log"
	"mktaxi/handlers"
	"mktaxi/utils"
	"net/http"

	"github.com/gorilla/mux"
)

func main() {
	db, err := utils.GetDB()
	if err != nil {
		log.Fatal(err)
	}

	// Create a new instance of your handler and pass the database connection
	handler := handlers.NewHandler(db)

	router := mux.NewRouter()
	router.HandleFunc("/api/route1", handler.Handler1).Methods("GET")

	log.Fatal(http.ListenAndServe(":5001", router))
}
