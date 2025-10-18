// Random Go struct generated on 2025-10-18
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type HandleResponse struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewHandleResponse(name string, value int) *HandleResponse {
    return &HandleResponse{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *HandleResponse) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *HandleResponse) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewHandleResponse("sample", 67)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
