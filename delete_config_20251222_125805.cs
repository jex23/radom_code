// Random C# function generated on 2025-12-22
using System;
using System.Collections.Generic;
using System.Linq;

public class SetResponse
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public SetResponse(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Process_resultProcessor
{
    public static List<SetResponse> Process_result(IEnumerable<SetResponse> items)
    {
        const double multiplier = 2.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new SetResponse(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<SetResponse>
        {
            new SetResponse(1, "Item1", 78),
            new SetResponse(2, "Item2", 34)
        };
        
        var result = Process_result(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
