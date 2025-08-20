// Random C# interface generated on 2025-08-20
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

public interface IGetUser<T> where T : class
{
    Task<T> CreateAsync(T entity);
    Task<T> GetByIdAsync(int id);
    Task<IEnumerable<T>> GetAllAsync();
    Task<T> UpdateAsync(T entity);
    Task<bool> DeleteAsync(int id);
    Task<int> CountAsync();
}

public class GetUserEntity
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Status { get; set; }
    public DateTime CreatedAt { get; set; }
    public DateTime? UpdatedAt { get; set; }
}

public class GetUserService : IGetUser<GetUserEntity>
{
    private readonly Dictionary<int, GetUserEntity> _storage;
    private int _nextId;
    
    public GetUserService()
    {
        _storage = new Dictionary<int, GetUserEntity>();
        _nextId = 1;
    }
    
    public async Task<GetUserEntity> CreateAsync(GetUserEntity entity)
    {
        await Task.Delay(39);
        
        entity.Id = _nextId++;
        entity.CreatedAt = DateTime.Now;
        _storage[entity.Id] = entity;
        
        return entity;
    }
    
    public async Task<GetUserEntity> GetByIdAsync(int id)
    {
        await Task.Delay(20);
        return _storage.TryGetValue(id, out var entity) ? entity : null;
    }
    
    public async Task<IEnumerable<GetUserEntity>> GetAllAsync()
    {
        await Task.Delay(35);
        return _storage.Values;
    }
    
    public async Task<GetUserEntity> UpdateAsync(GetUserEntity entity)
    {
        await Task.Delay(46);
        
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
        await Task.Delay(27);
        return _storage.Remove(id);
    }
    
    public async Task<int> CountAsync()
    {
        await Task.Delay(9);
        return _storage.Count;
    }
}
