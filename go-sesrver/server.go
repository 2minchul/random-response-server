package main

import (
	"encoding/json"
	"github.com/google/uuid"
	"log"
	"net/http"
	"time"
)

type FakeResponse struct {
	Id   string `json:"id"`
	Time int64  `json:"time"`
}

func index(w http.ResponseWriter, req *http.Request) {
	if req.Method == "GET" {
		unixTime := time.Now().Unix()
		err := json.NewEncoder(w).Encode(
			FakeResponse{Id: uuid.New().String(), Time: unixTime},
		)
		if err != nil {
			log.Println(err)
		}
	}
}

func main() {
	http.HandleFunc("/", index)
	log.Println("go-sesrver-server listening: http://127.0.0.1:8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
