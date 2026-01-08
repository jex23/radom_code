// Random C# interface generated on 2026-01-08
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

public interface IUpdateUser<T> where T : class
{
    Task<T> CreateAsync(T entity);
    Task<T> GetByIdAsync(int id);
    Task<IEnumerable<T>> GetAllAsync();
    Task<T> UpdateAsync(T entity);
    Task<bool> DeleteAsync(int id);
    Task<int> CountAsync();
}

public class UpdateUserEntity
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Status { get; set; }
    public DateTime CreatedAt { get; set; }
    public DateTime? UpdatedAt { get; set; }
}

public class UpdateUserService : IUpdateUser<UpdateUserEntity>
{
    private readonly Dictionary<int, UpdateUserEntity> _storage;
    private int _nextId;
    
    public UpdateUserService()
    {
        _storage = new Dictionary<int, UpdateUserEntity>();
        _nextId = 1;
    }
    
    public async Task<UpdateUserEntity> CreateAsync(UpdateUserEntity entity)
    {
        await Task.Delay(89);
        
        entity.Id = _nextId++;
        entity.CreatedAt = DateTime.Now;
        _storage[entity.Id] = entity;
        
        return entity;
    }
    
    public async Task<UpdateUserEntity> GetByIdAsync(int id)
    {
        await Task.Delay(41);
        return _storage.TryGetValue(id, out var entity) ? entity : null;
    }
    
    public async Task<IEnumerable<UpdateUserEntity>> GetAllAsync()
    {
        await Task.Delay(84);
        return _storage.Values;
    }
    
    public async Task<UpdateUserEntity> UpdateAsync(UpdateUserEntity entity)
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
        await Task.Delay(38);
        return _storage.Remove(id);
    }
    
    public async Task<int> CountAsync()
    {
        await Task.Delay(5);
        return _storage.Count;
    }
}
