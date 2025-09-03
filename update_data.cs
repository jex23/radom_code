// Random C# function generated on 2025-09-03
using System;
using System.Collections.Generic;
using System.Linq;

public class UpdateData
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public UpdateData(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Delete_itemProcessor
{
    public static List<UpdateData> Delete_item(IEnumerable<UpdateData> items)
    {
        const double multiplier = 2.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new UpdateData(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<UpdateData>
        {
            new UpdateData(1, "Item1", 33),
            new UpdateData(2, "Item2", 44)
        };
        
        var result = Delete_item(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
