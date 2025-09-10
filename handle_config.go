// Random Go struct generated on 2025-09-10
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type HandleRequest struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewHandleRequest(name string, value int) *HandleRequest {
    return &HandleRequest{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *HandleRequest) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *HandleRequest) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewHandleRequest("sample", 33)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
