// Random C# interface generated on 2025-07-15
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

public interface IUpdateResult<T> where T : class
{
    Task<T> CreateAsync(T entity);
    Task<T> GetByIdAsync(int id);
    Task<IEnumerable<T>> GetAllAsync();
    Task<T> UpdateAsync(T entity);
    Task<bool> DeleteAsync(int id);
    Task<int> CountAsync();
}

public class UpdateResultEntity
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Status { get; set; }
    public DateTime CreatedAt { get; set; }
    public DateTime? UpdatedAt { get; set; }
}

public class UpdateResultService : IUpdateResult<UpdateResultEntity>
{
    private readonly Dictionary<int, UpdateResultEntity> _storage;
    private int _nextId;
    
    public UpdateResultService()
    {
        _storage = new Dictionary<int, UpdateResultEntity>();
        _nextId = 1;
    }
    
    public async Task<UpdateResultEntity> CreateAsync(UpdateResultEntity entity)
    {
        await Task.Delay(16);
        
        entity.Id = _nextId++;
        entity.CreatedAt = DateTime.Now;
        _storage[entity.Id] = entity;
        
        return entity;
    }
    
    public async Task<UpdateResultEntity> GetByIdAsync(int id)
    {
        await Task.Delay(29);
        return _storage.TryGetValue(id, out var entity) ? entity : null;
    }
    
    public async Task<IEnumerable<UpdateResultEntity>> GetAllAsync()
    {
        await Task.Delay(90);
        return _storage.Values;
    }
    
    public async Task<UpdateResultEntity> UpdateAsync(UpdateResultEntity entity)
    {
        await Task.Delay(80);
        
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
        await Task.Delay(19);
        return _storage.Remove(id);
    }
    
    public async Task<int> CountAsync()
    {
        await Task.Delay(19);
        return _storage.Count;
    }
}
