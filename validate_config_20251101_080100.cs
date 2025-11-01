// Random C# function generated on 2025-11-01
using System;
using System.Collections.Generic;
using System.Linq;

public class CheckRequest
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public CheckRequest(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Update_userProcessor
{
    public static List<CheckRequest> Update_user(IEnumerable<CheckRequest> items)
    {
        const double multiplier = 3.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new CheckRequest(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<CheckRequest>
        {
            new CheckRequest(1, "Item1", 51),
            new CheckRequest(2, "Item2", 63)
        };
        
        var result = Update_user(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
