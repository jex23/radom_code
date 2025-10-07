// Random C# function generated on 2025-10-07
using System;
using System.Collections.Generic;
using System.Linq;

public class DeleteResponse
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public DeleteResponse(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Delete_dataProcessor
{
    public static List<DeleteResponse> Delete_data(IEnumerable<DeleteResponse> items)
    {
        const double multiplier = 5.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new DeleteResponse(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<DeleteResponse>
        {
            new DeleteResponse(1, "Item1", 37),
            new DeleteResponse(2, "Item2", 99)
        };
        
        var result = Delete_data(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
