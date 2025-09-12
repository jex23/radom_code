// Random C# class generated on 2025-09-12
using System;
using System.Collections.Generic;
using System.ComponentModel;

public class HandleRequest : INotifyPropertyChanged
{
    private string _name;
    private int _value;
    private readonly List<string> _history;
    
    public event PropertyChangedEventHandler PropertyChanged;
    
    public HandleRequest(string name, int value = 70)
    {
        _name = name;
        _value = value;
        _history = new List<string>();
        CreatedAt = DateTime.Now;
        AddToHistory($"Created with name: {name}, value: {value}");
    }
    
    public string Name
    {
        get => _name;
        set
        {
            if (_name != value)
            {
                var oldValue = _name;
                _name = value;
                AddToHistory($"Name changed from {oldValue} to {value}");
                OnPropertyChanged(nameof(Name));
            }
        }
    }
    
    public int Value
    {
        get => _value;
        set
        {
            if (_value != value)
            {
                var oldValue = _value;
                _value = value;
                AddToHistory($"Value changed from {oldValue} to {value}");
                OnPropertyChanged(nameof(Value));
            }
        }
    }
    
    public DateTime CreatedAt { get; }
    
    public IReadOnlyList<string> History => _history.AsReadOnly();
    
    private void AddToHistory(string entry)
    {
        _history.Add($"{DateTime.Now:yyyy-MM-dd HH:mm:ss} - {entry}");
    }
    
    protected virtual void OnPropertyChanged(string propertyName)
    {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
    }
    
    public override string ToString()
    {
        return $"HandleRequest { Name = {Name}, Value = {Value}, CreatedAt = {CreatedAt} }";
    }
}
