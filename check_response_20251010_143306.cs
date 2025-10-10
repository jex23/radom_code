// Random C# function generated on 2025-10-10
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

public static class Delete_dataProcessor
{
    public static List<CreateData> Delete_data(IEnumerable<CreateData> items)
    {
        const double multiplier = 9.0;
        
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
            new CreateData(1, "Item1", 76),
            new CreateData(2, "Item2", 99)
        };
        
        var result = Delete_data(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
