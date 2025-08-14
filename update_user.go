// Random Go struct generated on 2025-08-14
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type CheckConfig struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewCheckConfig(name string, value int) *CheckConfig {
    return &CheckConfig{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *CheckConfig) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *CheckConfig) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewCheckConfig("sample", 69)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
