// Random C# function generated on 2025-06-16
using System;
using System.Collections.Generic;
using System.Linq;

public class ValidateData
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public ValidateData(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Check_dataProcessor
{
    public static List<ValidateData> Check_data(IEnumerable<ValidateData> items)
    {
        const double multiplier = 5.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new ValidateData(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<ValidateData>
        {
            new ValidateData(1, "Item1", 20),
            new ValidateData(2, "Item2", 88)
        };
        
        var result = Check_data(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
