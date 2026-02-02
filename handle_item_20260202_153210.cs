// Random C# interface generated on 2026-02-02
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

public interface ICreateUser<T> where T : class
{
    Task<T> CreateAsync(T entity);
    Task<T> GetByIdAsync(int id);
    Task<IEnumerable<T>> GetAllAsync();
    Task<T> UpdateAsync(T entity);
    Task<bool> DeleteAsync(int id);
    Task<int> CountAsync();
}

public class CreateUserEntity
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Status { get; set; }
    public DateTime CreatedAt { get; set; }
    public DateTime? UpdatedAt { get; set; }
}

public class CreateUserService : ICreateUser<CreateUserEntity>
{
    private readonly Dictionary<int, CreateUserEntity> _storage;
    private int _nextId;
    
    public CreateUserService()
    {
        _storage = new Dictionary<int, CreateUserEntity>();
        _nextId = 1;
    }
    
    public async Task<CreateUserEntity> CreateAsync(CreateUserEntity entity)
    {
        await Task.Delay(66);
        
        entity.Id = _nextId++;
        entity.CreatedAt = DateTime.Now;
        _storage[entity.Id] = entity;
        
        return entity;
    }
    
    public async Task<CreateUserEntity> GetByIdAsync(int id)
    {
        await Task.Delay(37);
        return _storage.TryGetValue(id, out var entity) ? entity : null;
    }
    
    public async Task<IEnumerable<CreateUserEntity>> GetAllAsync()
    {
        await Task.Delay(66);
        return _storage.Values;
    }
    
    public async Task<CreateUserEntity> UpdateAsync(CreateUserEntity entity)
    {
        await Task.Delay(55);
        
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
        await Task.Delay(59);
        return _storage.Remove(id);
    }
    
    public async Task<int> CountAsync()
    {
        await Task.Delay(11);
        return _storage.Count;
    }
}
