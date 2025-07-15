// Random Go struct generated on 2025-07-15
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type GetResponse struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewGetResponse(name string, value int) *GetResponse {
    return &GetResponse{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *GetResponse) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *GetResponse) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewGetResponse("sample", 30)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
