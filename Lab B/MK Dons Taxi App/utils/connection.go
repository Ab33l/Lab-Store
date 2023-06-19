package utils

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"

	_ "github.com/go-sql-driver/mysql"
)

type Config struct {
	Database struct {
		Username string `json:"username"`
		Password string `json:"password"`
		Host     string `json:"host"`
		Port     string `json:"port"`
		Name     string `json:"name"`
	} `json:"database"`
}

func GetDB() (*sql.DB, error) {
	// Load the configuration file
	config, err := loadConfig("utils/config.json")
	if err != nil {
		return nil, err
	}

	// Construct the MySQL connection string
	connectionString := fmt.Sprintf("%s:%s@tcp(%s:%s)/%s",
		config.Database.Username,
		config.Database.Password,
		config.Database.Host,
		config.Database.Port,
		config.Database.Name)

	// Connect to the database
	db, err := sql.Open("mysql", connectionString)
	if err != nil {
		return nil, err
	}

	// Verify the database connection
	err = db.Ping()
	if err != nil {
		return nil, err
	}

	log.Println("Database connection successful")

	return db, nil
}

func loadConfig(filename string) (*Config, error) {
	data, err := ioutil.ReadFile(filename)
	if err != nil {
		return nil, err
	}

	var config Config
	err = json.Unmarshal(data, &config)
	if err != nil {
		return nil, err
	}

	return &config, nil
}
