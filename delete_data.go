// Random Go struct generated on 2025-06-03
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type DeleteUser struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewDeleteUser(name string, value int) *DeleteUser {
    return &DeleteUser{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *DeleteUser) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *DeleteUser) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewDeleteUser("sample", 70)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
