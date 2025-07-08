// Random C# function generated on 2025-07-08
using System;
using System.Collections.Generic;
using System.Linq;

public class SetRequest
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public SetRequest(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Update_resultProcessor
{
    public static List<SetRequest> Update_result(IEnumerable<SetRequest> items)
    {
        const double multiplier = 3.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new SetRequest(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<SetRequest>
        {
            new SetRequest(1, "Item1", 82),
            new SetRequest(2, "Item2", 10)
        };
        
        var result = Update_result(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
