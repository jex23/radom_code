// Random Go struct generated on 2026-01-30
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type SetItem struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewSetItem(name string, value int) *SetItem {
    return &SetItem{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *SetItem) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *SetItem) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewSetItem("sample", 68)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
