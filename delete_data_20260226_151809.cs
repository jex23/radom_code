// Random C# interface generated on 2026-02-26
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

public interface IDeleteResponse<T> where T : class
{
    Task<T> CreateAsync(T entity);
    Task<T> GetByIdAsync(int id);
    Task<IEnumerable<T>> GetAllAsync();
    Task<T> UpdateAsync(T entity);
    Task<bool> DeleteAsync(int id);
    Task<int> CountAsync();
}

public class DeleteResponseEntity
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Status { get; set; }
    public DateTime CreatedAt { get; set; }
    public DateTime? UpdatedAt { get; set; }
}

public class DeleteResponseService : IDeleteResponse<DeleteResponseEntity>
{
    private readonly Dictionary<int, DeleteResponseEntity> _storage;
    private int _nextId;
    
    public DeleteResponseService()
    {
        _storage = new Dictionary<int, DeleteResponseEntity>();
        _nextId = 1;
    }
    
    public async Task<DeleteResponseEntity> CreateAsync(DeleteResponseEntity entity)
    {
        await Task.Delay(91);
        
        entity.Id = _nextId++;
        entity.CreatedAt = DateTime.Now;
        _storage[entity.Id] = entity;
        
        return entity;
    }
    
    public async Task<DeleteResponseEntity> GetByIdAsync(int id)
    {
        await Task.Delay(15);
        return _storage.TryGetValue(id, out var entity) ? entity : null;
    }
    
    public async Task<IEnumerable<DeleteResponseEntity>> GetAllAsync()
    {
        await Task.Delay(48);
        return _storage.Values;
    }
    
    public async Task<DeleteResponseEntity> UpdateAsync(DeleteResponseEntity entity)
    {
        await Task.Delay(51);
        
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
        await Task.Delay(16);
        return _storage.Remove(id);
    }
    
    public async Task<int> CountAsync()
    {
        await Task.Delay(20);
        return _storage.Count;
    }
}
