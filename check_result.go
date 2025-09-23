// Random Go struct generated on 2025-09-24
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type SetValue struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewSetValue(name string, value int) *SetValue {
    return &SetValue{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *SetValue) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *SetValue) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewSetValue("sample", 97)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
