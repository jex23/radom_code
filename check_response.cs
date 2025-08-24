// Random C# function generated on 2025-08-24
using System;
using System.Collections.Generic;
using System.Linq;

public class ProcessUser
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public ProcessUser(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Get_resultProcessor
{
    public static List<ProcessUser> Get_result(IEnumerable<ProcessUser> items)
    {
        const double multiplier = 3.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new ProcessUser(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<ProcessUser>
        {
            new ProcessUser(1, "Item1", 63),
            new ProcessUser(2, "Item2", 89)
        };
        
        var result = Get_result(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
