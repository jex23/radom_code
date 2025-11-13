// Random C# interface generated on 2025-11-13
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

public interface IHandleResponse<T> where T : class
{
    Task<T> CreateAsync(T entity);
    Task<T> GetByIdAsync(int id);
    Task<IEnumerable<T>> GetAllAsync();
    Task<T> UpdateAsync(T entity);
    Task<bool> DeleteAsync(int id);
    Task<int> CountAsync();
}

public class HandleResponseEntity
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Status { get; set; }
    public DateTime CreatedAt { get; set; }
    public DateTime? UpdatedAt { get; set; }
}

public class HandleResponseService : IHandleResponse<HandleResponseEntity>
{
    private readonly Dictionary<int, HandleResponseEntity> _storage;
    private int _nextId;
    
    public HandleResponseService()
    {
        _storage = new Dictionary<int, HandleResponseEntity>();
        _nextId = 1;
    }
    
    public async Task<HandleResponseEntity> CreateAsync(HandleResponseEntity entity)
    {
        await Task.Delay(32);
        
        entity.Id = _nextId++;
        entity.CreatedAt = DateTime.Now;
        _storage[entity.Id] = entity;
        
        return entity;
    }
    
    public async Task<HandleResponseEntity> GetByIdAsync(int id)
    {
        await Task.Delay(47);
        return _storage.TryGetValue(id, out var entity) ? entity : null;
    }
    
    public async Task<IEnumerable<HandleResponseEntity>> GetAllAsync()
    {
        await Task.Delay(88);
        return _storage.Values;
    }
    
    public async Task<HandleResponseEntity> UpdateAsync(HandleResponseEntity entity)
    {
        await Task.Delay(69);
        
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
        await Task.Delay(25);
        return _storage.Remove(id);
    }
    
    public async Task<int> CountAsync()
    {
        await Task.Delay(24);
        return _storage.Count;
    }
}
