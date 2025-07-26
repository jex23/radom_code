// Random Go struct generated on 2025-07-26
package main

import (
    "encoding/json"
    "fmt"
    "time"
)

type CreateResponse struct {
    Name      string    `json:"name"`
    Value     int       `json:"value"`
    Active    bool      `json:"active"`
    CreatedAt time.Time `json:"created_at"`
}

func NewCreateResponse(name string, value int) *CreateResponse {
    return &CreateResponse{
        Name:      name,
        Value:     value,
        Active:    true,
        CreatedAt: time.Now(),
    }
}

func (s *CreateResponse) UpdateValue(newValue int) {
    s.Value = newValue
}

func (s *CreateResponse) ToJSON() ([]byte, error) {
    return json.Marshal(s)
}

func main() {
    obj := NewCreateResponse("sample", 69)
    data, _ := obj.ToJSON()
    fmt.Println(string(data))
}
