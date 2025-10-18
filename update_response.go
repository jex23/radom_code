// Random Go struct generated on 2025-10-19
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type HandleData struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewHandleData(name string, value int) *HandleData {
    return &HandleData{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *HandleData) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *HandleData) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewHandleData("sample", 57)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
