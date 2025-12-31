// Random Go struct generated on 2025-12-31
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type CheckData struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewCheckData(name string, value int) *CheckData {
    return &CheckData{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *CheckData) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *CheckData) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewCheckData("sample", 45)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
