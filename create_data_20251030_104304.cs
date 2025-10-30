// Random C# function generated on 2025-10-30
using System;
using System.Collections.Generic;
using System.Linq;

public class UpdateRequest
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public UpdateRequest(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Update_itemProcessor
{
    public static List<UpdateRequest> Update_item(IEnumerable<UpdateRequest> items)
    {
        const double multiplier = 9.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new UpdateRequest(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<UpdateRequest>
        {
            new UpdateRequest(1, "Item1", 47),
            new UpdateRequest(2, "Item2", 63)
        };
        
        var result = Update_item(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
