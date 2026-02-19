// Random Go struct generated on 2026-02-19
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type CheckUser struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewCheckUser(name string, value int) *CheckUser {
    return &CheckUser{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *CheckUser) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *CheckUser) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewCheckUser("sample", 54)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
