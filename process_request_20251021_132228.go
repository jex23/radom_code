// Random Go struct generated on 2025-10-21
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type DeleteItem struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewDeleteItem(name string, value int) *DeleteItem {
    return &DeleteItem{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *DeleteItem) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *DeleteItem) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewDeleteItem("sample", 42)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
