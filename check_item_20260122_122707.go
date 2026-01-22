// Random Go struct generated on 2026-01-22
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type CreateResult struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewCreateResult(name string, value int) *CreateResult {
    return &CreateResult{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *CreateResult) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *CreateResult) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewCreateResult("sample", 89)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
