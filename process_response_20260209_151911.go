// Random Go struct generated on 2026-02-09
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type DeleteResult struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewDeleteResult(name string, value int) *DeleteResult {
    return &DeleteResult{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *DeleteResult) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *DeleteResult) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewDeleteResult("sample", 21)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
