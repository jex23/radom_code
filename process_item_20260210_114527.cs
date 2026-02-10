// Random C# function generated on 2026-02-10
using System;
using System.Collections.Generic;
using System.Linq;

public class UpdateConfig
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public UpdateConfig(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Process_requestProcessor
{
    public static List<UpdateConfig> Process_request(IEnumerable<UpdateConfig> items)
    {
        const double multiplier = 3.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new UpdateConfig(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<UpdateConfig>
        {
            new UpdateConfig(1, "Item1", 32),
            new UpdateConfig(2, "Item2", 69)
        };
        
        var result = Process_request(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
