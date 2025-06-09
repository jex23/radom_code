// Random C# interface generated on 2025-06-09
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

public interface IGetRequest<T> where T : class
{
    Task<T> CreateAsync(T entity);
    Task<T> GetByIdAsync(int id);
    Task<IEnumerable<T>> GetAllAsync();
    Task<T> UpdateAsync(T entity);
    Task<bool> DeleteAsync(int id);
    Task<int> CountAsync();
}

public class GetRequestEntity
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Status { get; set; }
    public DateTime CreatedAt { get; set; }
    public DateTime? UpdatedAt { get; set; }
}

public class GetRequestService : IGetRequest<GetRequestEntity>
{
    private readonly Dictionary<int, GetRequestEntity> _storage;
    private int _nextId;
    
    public GetRequestService()
    {
        _storage = new Dictionary<int, GetRequestEntity>();
        _nextId = 1;
    }
    
    public async Task<GetRequestEntity> CreateAsync(GetRequestEntity entity)
    {
        await Task.Delay(29);
        
        entity.Id = _nextId++;
        entity.CreatedAt = DateTime.Now;
        _storage[entity.Id] = entity;
        
        return entity;
    }
    
    public async Task<GetRequestEntity> GetByIdAsync(int id)
    {
        await Task.Delay(26);
        return _storage.TryGetValue(id, out var entity) ? entity : null;
    }
    
    public async Task<IEnumerable<GetRequestEntity>> GetAllAsync()
    {
        await Task.Delay(45);
        return _storage.Values;
    }
    
    public async Task<GetRequestEntity> UpdateAsync(GetRequestEntity entity)
    {
        await Task.Delay(53);
        
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
        await Task.Delay(12);
        return _storage.Count;
    }
}
