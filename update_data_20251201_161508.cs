// Random C# function generated on 2025-12-01
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

public static class Set_responseProcessor
{
    public static List<ProcessValue> Set_response(IEnumerable<ProcessValue> items)
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
            new ProcessValue(1, "Item1", 95),
            new ProcessValue(2, "Item2", 55)
        };
        
        var result = Set_response(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
