// Random Go struct generated on 2025-07-07
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type GetData struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewGetData(name string, value int) *GetData {
    return &GetData{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *GetData) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *GetData) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewGetData("sample", 17)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
