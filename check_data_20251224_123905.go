// Random Go struct generated on 2025-12-24
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type DeleteValue struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewDeleteValue(name string, value int) *DeleteValue {
    return &DeleteValue{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *DeleteValue) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *DeleteValue) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewDeleteValue("sample", 37)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
