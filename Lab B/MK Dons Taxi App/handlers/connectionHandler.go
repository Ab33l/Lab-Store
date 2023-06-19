package handlers

import (
	"database/sql"
	"fmt"
	"net/http"

	_ "github.com/go-sql-driver/mysql"
)

type Handler struct {
	db *sql.DB
}

func NewHandler(db *sql.DB) *Handler {
	return &Handler{
		db: db,
	}
}

func (h *Handler) Handler1(w http.ResponseWriter, r *http.Request) {
	// Handler logic for route 1
	fmt.Fprintln(w, "Handler 1")
}
