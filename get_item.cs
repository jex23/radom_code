// Random C# function generated on 2025-08-29
using System;
using System.Collections.Generic;
using System.Linq;

public class ValidateRequest
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public ValidateRequest(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Set_responseProcessor
{
    public static List<ValidateRequest> Set_response(IEnumerable<ValidateRequest> items)
    {
        const double multiplier = 8.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new ValidateRequest(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<ValidateRequest>
        {
            new ValidateRequest(1, "Item1", 39),
            new ValidateRequest(2, "Item2", 65)
        };
        
        var result = Set_response(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
