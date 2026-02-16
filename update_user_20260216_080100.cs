// Random C# function generated on 2026-02-16
using System;
using System.Collections.Generic;
using System.Linq;

public class HandleRequest
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public HandleRequest(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Update_itemProcessor
{
    public static List<HandleRequest> Update_item(IEnumerable<HandleRequest> items)
    {
        const double multiplier = 4.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new HandleRequest(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<HandleRequest>
        {
            new HandleRequest(1, "Item1", 58),
            new HandleRequest(2, "Item2", 35)
        };
        
        var result = Update_item(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
