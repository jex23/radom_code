// Random C# function generated on 2025-12-23
using System;
using System.Collections.Generic;
using System.Linq;

public class CreateData
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public CreateData(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Update_resultProcessor
{
    public static List<CreateData> Update_result(IEnumerable<CreateData> items)
    {
        const double multiplier = 3.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new CreateData(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<CreateData>
        {
            new CreateData(1, "Item1", 82),
            new CreateData(2, "Item2", 40)
        };
        
        var result = Update_result(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
