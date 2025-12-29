// Random C# function generated on 2025-12-29
using System;
using System.Collections.Generic;
using System.Linq;

public class HandleItem
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public HandleItem(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Check_dataProcessor
{
    public static List<HandleItem> Check_data(IEnumerable<HandleItem> items)
    {
        const double multiplier = 6.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new HandleItem(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<HandleItem>
        {
            new HandleItem(1, "Item1", 26),
            new HandleItem(2, "Item2", 75)
        };
        
        var result = Check_data(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
