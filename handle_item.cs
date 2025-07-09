// Random C# function generated on 2025-07-09
using System;
using System.Collections.Generic;
using System.Linq;

public class ValidateItem
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public ValidateItem(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Create_dataProcessor
{
    public static List<ValidateItem> Create_data(IEnumerable<ValidateItem> items)
    {
        const double multiplier = 9.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new ValidateItem(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<ValidateItem>
        {
            new ValidateItem(1, "Item1", 55),
            new ValidateItem(2, "Item2", 11)
        };
        
        var result = Create_data(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
