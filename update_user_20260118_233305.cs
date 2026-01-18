// Random C# interface generated on 2026-01-18
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

public interface IGetResponse<T> where T : class
{
    Task<T> CreateAsync(T entity);
    Task<T> GetByIdAsync(int id);
    Task<IEnumerable<T>> GetAllAsync();
    Task<T> UpdateAsync(T entity);
    Task<bool> DeleteAsync(int id);
    Task<int> CountAsync();
}

public class GetResponseEntity
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Status { get; set; }
    public DateTime CreatedAt { get; set; }
    public DateTime? UpdatedAt { get; set; }
}

public class GetResponseService : IGetResponse<GetResponseEntity>
{
    private readonly Dictionary<int, GetResponseEntity> _storage;
    private int _nextId;
    
    public GetResponseService()
    {
        _storage = new Dictionary<int, GetResponseEntity>();
        _nextId = 1;
    }
    
    public async Task<GetResponseEntity> CreateAsync(GetResponseEntity entity)
    {
        await Task.Delay(37);
        
        entity.Id = _nextId++;
        entity.CreatedAt = DateTime.Now;
        _storage[entity.Id] = entity;
        
        return entity;
    }
    
    public async Task<GetResponseEntity> GetByIdAsync(int id)
    {
        await Task.Delay(45);
        return _storage.TryGetValue(id, out var entity) ? entity : null;
    }
    
    public async Task<IEnumerable<GetResponseEntity>> GetAllAsync()
    {
        await Task.Delay(38);
        return _storage.Values;
    }
    
    public async Task<GetResponseEntity> UpdateAsync(GetResponseEntity entity)
    {
        await Task.Delay(37);
        
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
        await Task.Delay(60);
        return _storage.Remove(id);
    }
    
    public async Task<int> CountAsync()
    {
        await Task.Delay(9);
        return _storage.Count;
    }
}
