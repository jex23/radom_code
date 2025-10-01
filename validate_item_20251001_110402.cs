// Random C# function generated on 2025-10-01
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

public static class Check_dataProcessor
{
    public static List<UpdateData> Check_data(IEnumerable<UpdateData> items)
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
            new UpdateData(1, "Item1", 28),
            new UpdateData(2, "Item2", 13)
        };
        
        var result = Check_data(testData);
        Console.WriteLine($"Processed {result.Count} items");
    }
}
