// Random C# function generated on 2025-08-11
using System;
using System.Collections.Generic;
using System.Linq;

public class CreateResult
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public CreateResult(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Get_configProcessor
{
    public static List<CreateResult> Get_config(IEnumerable<CreateResult> items)
    {
        const double multiplier = 5.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new CreateResult(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<CreateResult>
        {
            new CreateResult(1, "Item1", 92),
            new CreateResult(2, "Item2", 81)
        };
        
        var result = Get_config(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
