// Random C# interface generated on 2025-09-03
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

public interface ICheckResponse<T> where T : class
{
    Task<T> CreateAsync(T entity);
    Task<T> GetByIdAsync(int id);
    Task<IEnumerable<T>> GetAllAsync();
    Task<T> UpdateAsync(T entity);
    Task<bool> DeleteAsync(int id);
    Task<int> CountAsync();
}

public class CheckResponseEntity
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Status { get; set; }
    public DateTime CreatedAt { get; set; }
    public DateTime? UpdatedAt { get; set; }
}

public class CheckResponseService : ICheckResponse<CheckResponseEntity>
{
    private readonly Dictionary<int, CheckResponseEntity> _storage;
    private int _nextId;
    
    public CheckResponseService()
    {
        _storage = new Dictionary<int, CheckResponseEntity>();
        _nextId = 1;
    }
    
    public async Task<CheckResponseEntity> CreateAsync(CheckResponseEntity entity)
    {
        await Task.Delay(71);
        
        entity.Id = _nextId++;
        entity.CreatedAt = DateTime.Now;
        _storage[entity.Id] = entity;
        
        return entity;
    }
    
    public async Task<CheckResponseEntity> GetByIdAsync(int id)
    {
        await Task.Delay(40);
        return _storage.TryGetValue(id, out var entity) ? entity : null;
    }
    
    public async Task<IEnumerable<CheckResponseEntity>> GetAllAsync()
    {
        await Task.Delay(41);
        return _storage.Values;
    }
    
    public async Task<CheckResponseEntity> UpdateAsync(CheckResponseEntity entity)
    {
        await Task.Delay(42);
        
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
        await Task.Delay(24);
        return _storage.Remove(id);
    }
    
    public async Task<int> CountAsync()
    {
        await Task.Delay(10);
        return _storage.Count;
    }
}
