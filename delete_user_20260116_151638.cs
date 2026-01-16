// Random C# function generated on 2026-01-16
using System;
using System.Collections.Generic;
using System.Linq;

public class UpdateResponse
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public UpdateResponse(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Update_requestProcessor
{
    public static List<UpdateResponse> Update_request(IEnumerable<UpdateResponse> items)
    {
        const double multiplier = 6.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new UpdateResponse(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<UpdateResponse>
        {
            new UpdateResponse(1, "Item1", 59),
            new UpdateResponse(2, "Item2", 44)
        };
        
        var result = Update_request(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
