// Random C# function generated on 2025-06-24
using System;
using System.Collections.Generic;
using System.Linq;

public class CreateUser
{
    public int Id { get; set; }
    public string Name { get; set; }
    public double Value { get; set; }
    public DateTime CreatedAt { get; set; }
    
    public CreateUser(int id, string name, double value)
    {
        Id = id;
        Name = name;
        Value = value;
        CreatedAt = DateTime.Now;
    }
}

public static class Validate_valueProcessor
{
    public static List<CreateUser> Validate_value(IEnumerable<CreateUser> items)
    {
        const double multiplier = 7.0;
        
        return items
            .Where(item => item.Value > 0)
            .Select(item => new CreateUser(
                item.Id,
                $"{item.Name}_processed",
                item.Value * multiplier))
            .ToList();
    }
    
    public static void Main()
    {
        var testData = new List<CreateUser>
        {
            new CreateUser(1, "Item1", 35),
            new CreateUser(2, "Item2", 19)
        };
        
        var result = Validate_value(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
