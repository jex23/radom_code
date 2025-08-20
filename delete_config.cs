// Random C# interface generated on 2025-08-20
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

public interface ICheckUser<T> where T : class
{
    Task<T> CreateAsync(T entity);
    Task<T> GetByIdAsync(int id);
    Task<IEnumerable<T>> GetAllAsync();
    Task<T> UpdateAsync(T entity);
    Task<bool> DeleteAsync(int id);
    Task<int> CountAsync();
}

public class CheckUserEntity
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Status { get; set; }
    public DateTime CreatedAt { get; set; }
    public DateTime? UpdatedAt { get; set; }
}

public class CheckUserService : ICheckUser<CheckUserEntity>
{
    private readonly Dictionary<int, CheckUserEntity> _storage;
    private int _nextId;
    
    public CheckUserService()
    {
        _storage = new Dictionary<int, CheckUserEntity>();
        _nextId = 1;
    }
    
    public async Task<CheckUserEntity> CreateAsync(CheckUserEntity entity)
    {
        await Task.Delay(17);
        
        entity.Id = _nextId++;
        entity.CreatedAt = DateTime.Now;
        _storage[entity.Id] = entity;
        
        return entity;
    }
    
    public async Task<CheckUserEntity> GetByIdAsync(int id)
    {
        await Task.Delay(48);
        return _storage.TryGetValue(id, out var entity) ? entity : null;
    }
    
    public async Task<IEnumerable<CheckUserEntity>> GetAllAsync()
    {
        await Task.Delay(97);
        return _storage.Values;
    }
    
    public async Task<CheckUserEntity> UpdateAsync(CheckUserEntity entity)
    {
        await Task.Delay(76);
        
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
        await Task.Delay(52);
        return _storage.Remove(id);
    }
    
    public async Task<int> CountAsync()
    {
        await Task.Delay(15);
        return _storage.Count;
    }
}
