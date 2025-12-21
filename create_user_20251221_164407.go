// Random Go struct generated on 2025-12-21
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type CheckRequest struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewCheckRequest(name string, value int) *CheckRequest {
    return &CheckRequest{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *CheckRequest) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *CheckRequest) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewCheckRequest("sample", 41)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
