// Random C# function generated on 2025-12-03
using System;
using System.Collections.Generic;
using System.Linq;

public class CheckResult
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public CheckResult(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Get_responseProcessor
{
    public static List<CheckResult> Get_response(IEnumerable<CheckResult> items)
    {
        const double multiplier = 10.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new CheckResult(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<CheckResult>
        {
            new CheckResult(1, "Item1", 41),
            new CheckResult(2, "Item2", 20)
        };
        
        var result = Get_response(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
