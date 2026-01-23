// Random Go struct generated on 2026-01-24
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type UpdateResult struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewUpdateResult(name string, value int) *UpdateResult {
    return &UpdateResult{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *UpdateResult) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *UpdateResult) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewUpdateResult("sample", 41)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
