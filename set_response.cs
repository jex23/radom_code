// Random C# function generated on 2025-07-02
using System;
using System.Collections.Generic;
using System.Linq;

public class HandleConfig
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public HandleConfig(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Set_valueProcessor
{
    public static List<HandleConfig> Set_value(IEnumerable<HandleConfig> items)
    {
        const double multiplier = 8.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new HandleConfig(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<HandleConfig>
        {
            new HandleConfig(1, "Item1", 89),
            new HandleConfig(2, "Item2", 76)
        };
        
        var result = Set_value(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
