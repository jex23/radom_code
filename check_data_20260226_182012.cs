// Random C# function generated on 2026-02-26
using System;
using System.Collections.Generic;
using System.Linq;

public class CheckItem
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public CheckItem(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Get_responseProcessor
{
    public static List<CheckItem> Get_response(IEnumerable<CheckItem> items)
    {
        const double multiplier = 10.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new CheckItem(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<CheckItem>
        {
            new CheckItem(1, "Item1", 95),
            new CheckItem(2, "Item2", 89)
        };
        
        var result = Get_response(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
