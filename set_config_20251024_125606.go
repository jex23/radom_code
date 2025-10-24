// Random Go struct generated on 2025-10-24
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type CreateUser struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewCreateUser(name string, value int) *CreateUser {
    return &CreateUser{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *CreateUser) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *CreateUser) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewCreateUser("sample", 73)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
