// Random C# function generated on 2025-06-11
using System;
using System.Collections.Generic;
using System.Linq;

public class CheckValue
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public CheckValue(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Get_dataProcessor
{
    public static List<CheckValue> Get_data(IEnumerable<CheckValue> items)
    {
        const double multiplier = 3.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new CheckValue(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<CheckValue>
        {
            new CheckValue(1, "Item1", 17),
            new CheckValue(2, "Item2", 90)
        };
        
        var result = Get_data(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
