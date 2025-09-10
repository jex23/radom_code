// Random C# interface generated on 2025-09-10
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

public interface IValidateUser<T> where T : class
{
    Task<T> CreateAsync(T entity);
    Task<T> GetByIdAsync(int id);
    Task<IEnumerable<T>> GetAllAsync();
    Task<T> UpdateAsync(T entity);
    Task<bool> DeleteAsync(int id);
    Task<int> CountAsync();
}

public class ValidateUserEntity
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Status { get; set; }
    public DateTime CreatedAt { get; set; }
    public DateTime? UpdatedAt { get; set; }
}

public class ValidateUserService : IValidateUser<ValidateUserEntity>
{
    private readonly Dictionary<int, ValidateUserEntity> _storage;
    private int _nextId;
    
    public ValidateUserService()
    {
        _storage = new Dictionary<int, ValidateUserEntity>();
        _nextId = 1;
    }
    
    public async Task<ValidateUserEntity> CreateAsync(ValidateUserEntity entity)
    {
        await Task.Delay(74);
        
        entity.Id = _nextId++;
        entity.CreatedAt = DateTime.Now;
        _storage[entity.Id] = entity;
        
        return entity;
    }
    
    public async Task<ValidateUserEntity> GetByIdAsync(int id)
    {
        await Task.Delay(29);
        return _storage.TryGetValue(id, out var entity) ? entity : null;
    }
    
    public async Task<IEnumerable<ValidateUserEntity>> GetAllAsync()
    {
        await Task.Delay(55);
        return _storage.Values;
    }
    
    public async Task<ValidateUserEntity> UpdateAsync(ValidateUserEntity entity)
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
        await Task.Delay(55);
        return _storage.Remove(id);
    }
    
    public async Task<int> CountAsync()
    {
        await Task.Delay(23);
        return _storage.Count;
    }
}
