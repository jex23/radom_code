// Random Go struct generated on 2025-07-16
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type HandleResult struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewHandleResult(name string, value int) *HandleResult {
    return &HandleResult{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *HandleResult) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *HandleResult) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewHandleResult("sample", 16)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
