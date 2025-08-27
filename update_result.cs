// Random C# interface generated on 2025-08-27
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

public interface IHandleData<T> where T : class
{
    Task<T> CreateAsync(T entity);
    Task<T> GetByIdAsync(int id);
    Task<IEnumerable<T>> GetAllAsync();
    Task<T> UpdateAsync(T entity);
    Task<bool> DeleteAsync(int id);
    Task<int> CountAsync();
}

public class HandleDataEntity
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Status { get; set; }
    public DateTime CreatedAt { get; set; }
    public DateTime? UpdatedAt { get; set; }
}

public class HandleDataService : IHandleData<HandleDataEntity>
{
    private readonly Dictionary<int, HandleDataEntity> _storage;
    private int _nextId;
    
    public HandleDataService()
    {
        _storage = new Dictionary<int, HandleDataEntity>();
        _nextId = 1;
    }
    
    public async Task<HandleDataEntity> CreateAsync(HandleDataEntity entity)
    {
        await Task.Delay(97);
        
        entity.Id = _nextId++;
        entity.CreatedAt = DateTime.Now;
        _storage[entity.Id] = entity;
        
        return entity;
    }
    
    public async Task<HandleDataEntity> GetByIdAsync(int id)
    {
        await Task.Delay(13);
        return _storage.TryGetValue(id, out var entity) ? entity : null;
    }
    
    public async Task<IEnumerable<HandleDataEntity>> GetAllAsync()
    {
        await Task.Delay(52);
        return _storage.Values;
    }
    
    public async Task<HandleDataEntity> UpdateAsync(HandleDataEntity entity)
    {
        await Task.Delay(49);
        
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
        await Task.Delay(45);
        return _storage.Remove(id);
    }
    
    public async Task<int> CountAsync()
    {
        await Task.Delay(26);
        return _storage.Count;
    }
}
