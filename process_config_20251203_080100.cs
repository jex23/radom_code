// Random C# function generated on 2025-12-03
using System;
using System.Collections.Generic;
using System.Linq;

public class UpdateResult
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public UpdateResult(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Set_userProcessor
{
    public static List<UpdateResult> Set_user(IEnumerable<UpdateResult> items)
    {
        const double multiplier = 9.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new UpdateResult(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<UpdateResult>
        {
            new UpdateResult(1, "Item1", 86),
            new UpdateResult(2, "Item2", 67)
        };
        
        var result = Set_user(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
