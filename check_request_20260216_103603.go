// Random Go struct generated on 2026-02-16
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type SetResult struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewSetResult(name string, value int) *SetResult {
    return &SetResult{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *SetResult) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *SetResult) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewSetResult("sample", 30)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
