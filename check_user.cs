// Random C# function generated on 2025-08-13
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

public static class Handle_requestProcessor
{
    public static List<HandleValue> Handle_request(IEnumerable<HandleValue> items)
    {
        const double multiplier = 5.0;
        
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
            new HandleValue(1, "Item1", 58),
            new HandleValue(2, "Item2", 69)
        };
        
        var result = Handle_request(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
