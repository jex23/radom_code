// Random Go struct generated on 2025-11-20
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type ProcessResult struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewProcessResult(name string, value int) *ProcessResult {
    return &ProcessResult{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *ProcessResult) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *ProcessResult) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewProcessResult("sample", 72)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
