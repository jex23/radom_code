// Random Go struct generated on 2025-06-03
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type HandleValue struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewHandleValue(name string, value int) *HandleValue {
    return &HandleValue{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *HandleValue) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *HandleValue) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewHandleValue("sample", 67)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
