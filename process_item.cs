// Random C# function generated on 2025-08-19
using System;
using System.Collections.Generic;
using System.Linq;

public class ValidateResult
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public ValidateResult(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Create_dataProcessor
{
    public static List<ValidateResult> Create_data(IEnumerable<ValidateResult> items)
    {
        const double multiplier = 3.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new ValidateResult(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<ValidateResult>
        {
            new ValidateResult(1, "Item1", 75),
            new ValidateResult(2, "Item2", 76)
        };
        
        var result = Create_data(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
