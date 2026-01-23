// Random Go struct generated on 2026-01-23
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type DeleteRequest struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewDeleteRequest(name string, value int) *DeleteRequest {
    return &DeleteRequest{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *DeleteRequest) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *DeleteRequest) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewDeleteRequest("sample", 85)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
