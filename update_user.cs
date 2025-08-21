// Random C# function generated on 2025-08-21
using System;
using System.Collections.Generic;
using System.Linq;

public class CreateResponse
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public CreateResponse(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Delete_configProcessor
{
    public static List<CreateResponse> Delete_config(IEnumerable<CreateResponse> items)
    {
        const double multiplier = 9.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new CreateResponse(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<CreateResponse>
        {
            new CreateResponse(1, "Item1", 72),
            new CreateResponse(2, "Item2", 63)
        };
        
        var result = Delete_config(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
