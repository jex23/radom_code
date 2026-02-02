// Random C# function generated on 2026-02-02
using System;
using System.Collections.Generic;
using System.Linq;

public class HandleUser
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public HandleUser(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Check_resultProcessor
{
    public static List<HandleUser> Check_result(IEnumerable<HandleUser> items)
    {
        const double multiplier = 6.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new HandleUser(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<HandleUser>
        {
            new HandleUser(1, "Item1", 66),
            new HandleUser(2, "Item2", 77)
        };
        
        var result = Check_result(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
