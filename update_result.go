// Random Go struct generated on 2025-06-27
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type HandleConfig struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewHandleConfig(name string, value int) *HandleConfig {
    return &HandleConfig{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *HandleConfig) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *HandleConfig) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewHandleConfig("sample", 44)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
