// Random C# function generated on 2026-01-12
using System;
using System.Collections.Generic;
using System.Linq;

public class GetItem
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public GetItem(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Update_configProcessor
{
    public static List<GetItem> Update_config(IEnumerable<GetItem> items)
    {
        const double multiplier = 4.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new GetItem(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<GetItem>
        {
            new GetItem(1, "Item1", 79),
            new GetItem(2, "Item2", 66)
        };
        
        var result = Update_config(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
