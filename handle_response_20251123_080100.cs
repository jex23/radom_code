// Random C# function generated on 2025-11-23
using System;
using System.Collections.Generic;
using System.Linq;

public class CheckUser
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public CheckUser(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Get_configProcessor
{
    public static List<CheckUser> Get_config(IEnumerable<CheckUser> items)
    {
        const double multiplier = 10.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new CheckUser(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<CheckUser>
        {
            new CheckUser(1, "Item1", 20),
            new CheckUser(2, "Item2", 54)
        };
        
        var result = Get_config(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
