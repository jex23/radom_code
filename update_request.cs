// Random C# function generated on 2025-07-03
using System;
using System.Collections.Generic;
using System.Linq;

public class HandleValue
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public HandleValue(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Validate_configProcessor
{
    public static List<HandleValue> Validate_config(IEnumerable<HandleValue> items)
    {
        const double multiplier = 6.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new HandleValue(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<HandleValue>
        {
            new HandleValue(1, "Item1", 36),
            new HandleValue(2, "Item2", 32)
        };
        
        var result = Validate_config(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
