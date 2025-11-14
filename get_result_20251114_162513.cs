// Random C# interface generated on 2025-11-14
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

public interface IHandleUser<T> where T : class
{
    Task<T> CreateAsync(T entity);
    Task<T> GetByIdAsync(int id);
    Task<IEnumerable<T>> GetAllAsync();
    Task<T> UpdateAsync(T entity);
    Task<bool> DeleteAsync(int id);
    Task<int> CountAsync();
}

public class HandleUserEntity
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Status { get; set; }
    public DateTime CreatedAt { get; set; }
    public DateTime? UpdatedAt { get; set; }
}

public class HandleUserService : IHandleUser<HandleUserEntity>
{
    private readonly Dictionary<int, HandleUserEntity> _storage;
    private int _nextId;
    
    public HandleUserService()
    {
        _storage = new Dictionary<int, HandleUserEntity>();
        _nextId = 1;
    }
    
    public async Task<HandleUserEntity> CreateAsync(HandleUserEntity entity)
    {
        await Task.Delay(32);
        
        entity.Id = _nextId++;
        entity.CreatedAt = DateTime.Now;
        _storage[entity.Id] = entity;
        
        return entity;
    }
    
    public async Task<HandleUserEntity> GetByIdAsync(int id)
    {
        await Task.Delay(33);
        return _storage.TryGetValue(id, out var entity) ? entity : null;
    }
    
    public async Task<IEnumerable<HandleUserEntity>> GetAllAsync()
    {
        await Task.Delay(50);
        return _storage.Values;
    }
    
    public async Task<HandleUserEntity> UpdateAsync(HandleUserEntity entity)
    {
        await Task.Delay(13);
        
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
        await Task.Delay(21);
        return _storage.Remove(id);
    }
    
    public async Task<int> CountAsync()
    {
        await Task.Delay(22);
        return _storage.Count;
    }
}
