// Random Go struct generated on 2026-02-16
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type CreateConfig struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewCreateConfig(name string, value int) *CreateConfig {
    return &CreateConfig{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *CreateConfig) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *CreateConfig) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewCreateConfig("sample", 44)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
