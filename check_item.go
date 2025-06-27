// Random Go struct generated on 2025-06-27
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type UpdateUser struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewUpdateUser(name string, value int) *UpdateUser {
    return &UpdateUser{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *UpdateUser) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *UpdateUser) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewUpdateUser("sample", 65)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
