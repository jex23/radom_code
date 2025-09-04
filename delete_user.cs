// Random C# function generated on 2025-09-04
using System;
using System.Collections.Generic;
using System.Linq;

public class SetResult
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public SetResult(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Set_dataProcessor
{
    public static List<SetResult> Set_data(IEnumerable<SetResult> items)
    {
        const double multiplier = 7.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new SetResult(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<SetResult>
        {
            new SetResult(1, "Item1", 17),
            new SetResult(2, "Item2", 86)
        };
        
        var result = Set_data(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
