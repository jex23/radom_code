// Random Go struct generated on 2025-09-30
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type ProcessValue struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewProcessValue(name string, value int) *ProcessValue {
    return &ProcessValue{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *ProcessValue) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *ProcessValue) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewProcessValue("sample", 33)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
