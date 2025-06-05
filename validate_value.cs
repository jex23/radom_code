// Random C# interface generated on 2025-06-05
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

public interface IDeleteRequest<T> where T : class
{
    Task<T> CreateAsync(T entity);
    Task<T> GetByIdAsync(int id);
    Task<IEnumerable<T>> GetAllAsync();
    Task<T> UpdateAsync(T entity);
    Task<bool> DeleteAsync(int id);
    Task<int> CountAsync();
}

public class DeleteRequestEntity
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Status { get; set; }
    public DateTime CreatedAt { get; set; }
    public DateTime? UpdatedAt { get; set; }
}

public class DeleteRequestService : IDeleteRequest<DeleteRequestEntity>
{
    private readonly Dictionary<int, DeleteRequestEntity> _storage;
    private int _nextId;
    
    public DeleteRequestService()
    {
        _storage = new Dictionary<int, DeleteRequestEntity>();
        _nextId = 1;
    }
    
    public async Task<DeleteRequestEntity> CreateAsync(DeleteRequestEntity entity)
    {
        await Task.Delay(36);
        
        entity.Id = _nextId++;
        entity.CreatedAt = DateTime.Now;
        _storage[entity.Id] = entity;
        
        return entity;
    }
    
    public async Task<DeleteRequestEntity> GetByIdAsync(int id)
    {
        await Task.Delay(49);
        return _storage.TryGetValue(id, out var entity) ? entity : null;
    }
    
    public async Task<IEnumerable<DeleteRequestEntity>> GetAllAsync()
    {
        await Task.Delay(33);
        return _storage.Values;
    }
    
    public async Task<DeleteRequestEntity> UpdateAsync(DeleteRequestEntity entity)
    {
        await Task.Delay(35);
        
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
        await Task.Delay(30);
        return _storage.Remove(id);
    }
    
    public async Task<int> CountAsync()
    {
        await Task.Delay(7);
        return _storage.Count;
    }
}
