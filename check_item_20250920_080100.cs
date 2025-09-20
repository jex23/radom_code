// Random C# function generated on 2025-09-20
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

public static class Get_valueProcessor
{
    public static List<CreateUser> Get_value(IEnumerable<CreateUser> items)
    {
        const double multiplier = 5.0;
        
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
            new CreateUser(1, "Item1", 40),
            new CreateUser(2, "Item2", 94)
        };
        
        var result = Get_value(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
