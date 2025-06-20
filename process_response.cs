// Random C# function generated on 2025-06-20
using System;
using System.Collections.Generic;
using System.Linq;

public class GetConfig
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public GetConfig(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Check_requestProcessor
{
    public static List<GetConfig> Check_request(IEnumerable<GetConfig> items)
    {
        const double multiplier = 3.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new GetConfig(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<GetConfig>
        {
            new GetConfig(1, "Item1", 28),
            new GetConfig(2, "Item2", 17)
        };
        
        var result = Check_request(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
