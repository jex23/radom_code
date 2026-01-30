// Random C# interface generated on 2026-01-30
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

public interface IDeleteUser<T> where T : class
{
    Task<T> CreateAsync(T entity);
    Task<T> GetByIdAsync(int id);
    Task<IEnumerable<T>> GetAllAsync();
    Task<T> UpdateAsync(T entity);
    Task<bool> DeleteAsync(int id);
    Task<int> CountAsync();
}

public class DeleteUserEntity
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Status { get; set; }
    public DateTime CreatedAt { get; set; }
    public DateTime? UpdatedAt { get; set; }
}

public class DeleteUserService : IDeleteUser<DeleteUserEntity>
{
    private readonly Dictionary<int, DeleteUserEntity> _storage;
    private int _nextId;
    
    public DeleteUserService()
    {
        _storage = new Dictionary<int, DeleteUserEntity>();
        _nextId = 1;
    }
    
    public async Task<DeleteUserEntity> CreateAsync(DeleteUserEntity entity)
    {
        await Task.Delay(43);
        
        entity.Id = _nextId++;
        entity.CreatedAt = DateTime.Now;
        _storage[entity.Id] = entity;
        
        return entity;
    }
    
    public async Task<DeleteUserEntity> GetByIdAsync(int id)
    {
        await Task.Delay(43);
        return _storage.TryGetValue(id, out var entity) ? entity : null;
    }
    
    public async Task<IEnumerable<DeleteUserEntity>> GetAllAsync()
    {
        await Task.Delay(95);
        return _storage.Values;
    }
    
    public async Task<DeleteUserEntity> UpdateAsync(DeleteUserEntity entity)
    {
        await Task.Delay(79);
        
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
        await Task.Delay(14);
        return _storage.Count;
    }
}
