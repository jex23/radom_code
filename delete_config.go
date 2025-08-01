// Random Go struct generated on 2025-08-01
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type ValidateData struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewValidateData(name string, value int) *ValidateData {
    return &ValidateData{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *ValidateData) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *ValidateData) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewValidateData("sample", 61)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
