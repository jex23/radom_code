// Random C# interface generated on 2026-02-18
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

public interface IGetResult<T> where T : class
{
    Task<T> CreateAsync(T entity);
    Task<T> GetByIdAsync(int id);
    Task<IEnumerable<T>> GetAllAsync();
    Task<T> UpdateAsync(T entity);
    Task<bool> DeleteAsync(int id);
    Task<int> CountAsync();
}

public class GetResultEntity
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Status { get; set; }
    public DateTime CreatedAt { get; set; }
    public DateTime? UpdatedAt { get; set; }
}

public class GetResultService : IGetResult<GetResultEntity>
{
    private readonly Dictionary<int, GetResultEntity> _storage;
    private int _nextId;
    
    public GetResultService()
    {
        _storage = new Dictionary<int, GetResultEntity>();
        _nextId = 1;
    }
    
    public async Task<GetResultEntity> CreateAsync(GetResultEntity entity)
    {
        await Task.Delay(58);
        
        entity.Id = _nextId++;
        entity.CreatedAt = DateTime.Now;
        _storage[entity.Id] = entity;
        
        return entity;
    }
    
    public async Task<GetResultEntity> GetByIdAsync(int id)
    {
        await Task.Delay(48);
        return _storage.TryGetValue(id, out var entity) ? entity : null;
    }
    
    public async Task<IEnumerable<GetResultEntity>> GetAllAsync()
    {
        await Task.Delay(80);
        return _storage.Values;
    }
    
    public async Task<GetResultEntity> UpdateAsync(GetResultEntity entity)
    {
        await Task.Delay(40);
        
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
        await Task.Delay(41);
        return _storage.Remove(id);
    }
    
    public async Task<int> CountAsync()
    {
        await Task.Delay(26);
        return _storage.Count;
    }
}
