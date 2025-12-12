// Random Go struct generated on 2025-12-12
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type DeleteConfig struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewDeleteConfig(name string, value int) *DeleteConfig {
    return &DeleteConfig{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *DeleteConfig) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *DeleteConfig) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewDeleteConfig("sample", 53)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
