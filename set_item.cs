// Random C# function generated on 2025-06-23
using System;
using System.Collections.Generic;
using System.Linq;

public class GetValue
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public GetValue(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Create_valueProcessor
{
    public static List<GetValue> Create_value(IEnumerable<GetValue> items)
    {
        const double multiplier = 3.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new GetValue(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<GetValue>
        {
            new GetValue(1, "Item1", 23),
            new GetValue(2, "Item2", 71)
        };
        
        var result = Create_value(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
