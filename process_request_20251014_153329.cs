// Random C# interface generated on 2025-10-14
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

public interface ICreateResponse<T> where T : class
{
    Task<T> CreateAsync(T entity);
    Task<T> GetByIdAsync(int id);
    Task<IEnumerable<T>> GetAllAsync();
    Task<T> UpdateAsync(T entity);
    Task<bool> DeleteAsync(int id);
    Task<int> CountAsync();
}

public class CreateResponseEntity
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Status { get; set; }
    public DateTime CreatedAt { get; set; }
    public DateTime? UpdatedAt { get; set; }
}

public class CreateResponseService : ICreateResponse<CreateResponseEntity>
{
    private readonly Dictionary<int, CreateResponseEntity> _storage;
    private int _nextId;
    
    public CreateResponseService()
    {
        _storage = new Dictionary<int, CreateResponseEntity>();
        _nextId = 1;
    }
    
    public async Task<CreateResponseEntity> CreateAsync(CreateResponseEntity entity)
    {
        await Task.Delay(74);
        
        entity.Id = _nextId++;
        entity.CreatedAt = DateTime.Now;
        _storage[entity.Id] = entity;
        
        return entity;
    }
    
    public async Task<CreateResponseEntity> GetByIdAsync(int id)
    {
        await Task.Delay(13);
        return _storage.TryGetValue(id, out var entity) ? entity : null;
    }
    
    public async Task<IEnumerable<CreateResponseEntity>> GetAllAsync()
    {
        await Task.Delay(92);
        return _storage.Values;
    }
    
    public async Task<CreateResponseEntity> UpdateAsync(CreateResponseEntity entity)
    {
        await Task.Delay(48);
        
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
        await Task.Delay(42);
        return _storage.Remove(id);
    }
    
    public async Task<int> CountAsync()
    {
        await Task.Delay(18);
        return _storage.Count;
    }
}
