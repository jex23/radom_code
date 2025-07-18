// Random C# function generated on 2025-06-19
using System;
using System.Collections.Generic;
using System.Linq;

public class GetData
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public GetData(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Get_valueProcessor
{
    public static List<GetData> Get_value(IEnumerable<GetData> items)
    {
        const double multiplier = 3.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new GetData(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<GetData>
        {
            new GetData(1, "Item1", 77),
            new GetData(2, "Item2", 64)
        };
        
        var result = Get_value(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
