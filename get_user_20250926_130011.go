// Random Go struct generated on 2025-09-26
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type ValidateValue struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewValidateValue(name string, value int) *ValidateValue {
    return &ValidateValue{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *ValidateValue) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *ValidateValue) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewValidateValue("sample", 30)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
