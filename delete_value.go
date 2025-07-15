// Random Go struct generated on 2025-07-16
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type ValidateUser struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewValidateUser(name string, value int) *ValidateUser {
    return &ValidateUser{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *ValidateUser) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *ValidateUser) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewValidateUser("sample", 24)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
