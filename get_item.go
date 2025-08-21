// Random Go struct generated on 2025-08-21
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type UpdateConfig struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewUpdateConfig(name string, value int) *UpdateConfig {
    return &UpdateConfig{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *UpdateConfig) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *UpdateConfig) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewUpdateConfig("sample", 22)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
