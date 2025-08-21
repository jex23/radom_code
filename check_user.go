// Random Go struct generated on 2025-08-21
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type ProcessResponse struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewProcessResponse(name string, value int) *ProcessResponse {
    return &ProcessResponse{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *ProcessResponse) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *ProcessResponse) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewProcessResponse("sample", 77)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
