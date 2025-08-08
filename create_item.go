// Random Go struct generated on 2025-08-08
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type GetItem struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewGetItem(name string, value int) *GetItem {
    return &GetItem{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *GetItem) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *GetItem) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewGetItem("sample", 29)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
