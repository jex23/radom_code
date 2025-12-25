// Random C# function generated on 2025-12-25
using System;
using System.Collections.Generic;
using System.Linq;

public class SetItem
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public SetItem(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Update_resultProcessor
{
    public static List<SetItem> Update_result(IEnumerable<SetItem> items)
    {
        const double multiplier = 5.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new SetItem(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<SetItem>
        {
            new SetItem(1, "Item1", 97),
            new SetItem(2, "Item2", 69)
        };
        
        var result = Update_result(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
