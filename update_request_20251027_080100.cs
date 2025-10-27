// Random C# function generated on 2025-10-27
using System;
using System.Collections.Generic;
using System.Linq;

public class ProcessItem
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public ProcessItem(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Delete_valueProcessor
{
    public static List<ProcessItem> Delete_value(IEnumerable<ProcessItem> items)
    {
        const double multiplier = 9.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new ProcessItem(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<ProcessItem>
        {
            new ProcessItem(1, "Item1", 11),
            new ProcessItem(2, "Item2", 76)
        };
        
        var result = Delete_value(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
