// Random C# function generated on 2025-08-06
using System;
using System.Collections.Generic;
using System.Linq;

public class UpdateValue
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public UpdateValue(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Update_valueProcessor
{
    public static List<UpdateValue> Update_value(IEnumerable<UpdateValue> items)
    {
        const double multiplier = 3.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new UpdateValue(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<UpdateValue>
        {
            new UpdateValue(1, "Item1", 33),
            new UpdateValue(2, "Item2", 60)
        };
        
        var result = Update_value(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
