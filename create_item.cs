// Random C# interface generated on 2025-09-30
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

public interface ICheckItem<T> where T : class
{
    Task<T> CreateAsync(T entity);
    Task<T> GetByIdAsync(int id);
    Task<IEnumerable<T>> GetAllAsync();
    Task<T> UpdateAsync(T entity);
    Task<bool> DeleteAsync(int id);
    Task<int> CountAsync();
}

public class CheckItemEntity
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Status { get; set; }
    public DateTime CreatedAt { get; set; }
    public DateTime? UpdatedAt { get; set; }
}

public class CheckItemService : ICheckItem<CheckItemEntity>
{
    private readonly Dictionary<int, CheckItemEntity> _storage;
    private int _nextId;
    
    public CheckItemService()
    {
        _storage = new Dictionary<int, CheckItemEntity>();
        _nextId = 1;
    }
    
    public async Task<CheckItemEntity> CreateAsync(CheckItemEntity entity)
    {
        await Task.Delay(15);
        
        entity.Id = _nextId++;
        entity.CreatedAt = DateTime.Now;
        _storage[entity.Id] = entity;
        
        return entity;
    }
    
    public async Task<CheckItemEntity> GetByIdAsync(int id)
    {
        await Task.Delay(34);
        return _storage.TryGetValue(id, out var entity) ? entity : null;
    }
    
    public async Task<IEnumerable<CheckItemEntity>> GetAllAsync()
    {
        await Task.Delay(75);
        return _storage.Values;
    }
    
    public async Task<CheckItemEntity> UpdateAsync(CheckItemEntity entity)
    {
        await Task.Delay(76);
        
        if (_storage.ContainsKey(entity.Id))
        {
            entity.UpdatedAt = DateTime.Now;
            _storage[entity.Id] = entity;
            return entity;
        }
        
        return null;
    }
    
    public async Task<bool> DeleteAsync(int id)
    {
        await Task.Delay(36);
        return _storage.Remove(id);
    }
    
    public async Task<int> CountAsync()
    {
        await Task.Delay(20);
        return _storage.Count;
    }
}
