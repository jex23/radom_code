// Random C# function generated on 2026-01-19
using System;
using System.Collections.Generic;
using System.Linq;

public class ProcessValue
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public ProcessValue(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Handle_requestProcessor
{
    public static List<ProcessValue> Handle_request(IEnumerable<ProcessValue> items)
    {
        const double multiplier = 3.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new ProcessValue(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<ProcessValue>
        {
            new ProcessValue(1, "Item1", 35),
            new ProcessValue(2, "Item2", 32)
        };
        
        var result = Handle_request(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
