// Random Go struct generated on 2025-06-23
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type ProcessItem struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewProcessItem(name string, value int) *ProcessItem {
    return &ProcessItem{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *ProcessItem) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *ProcessItem) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewProcessItem("sample", 72)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
