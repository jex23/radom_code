// Random C# interface generated on 2025-12-24
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

public interface IDeleteData<T> where T : class
{
    Task<T> CreateAsync(T entity);
    Task<T> GetByIdAsync(int id);
    Task<IEnumerable<T>> GetAllAsync();
    Task<T> UpdateAsync(T entity);
    Task<bool> DeleteAsync(int id);
    Task<int> CountAsync();
}

public class DeleteDataEntity
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Status { get; set; }
    public DateTime CreatedAt { get; set; }
    public DateTime? UpdatedAt { get; set; }
}

public class DeleteDataService : IDeleteData<DeleteDataEntity>
{
    private readonly Dictionary<int, DeleteDataEntity> _storage;
    private int _nextId;
    
    public DeleteDataService()
    {
        _storage = new Dictionary<int, DeleteDataEntity>();
        _nextId = 1;
    }
    
    public async Task<DeleteDataEntity> CreateAsync(DeleteDataEntity entity)
    {
        await Task.Delay(92);
        
        entity.Id = _nextId++;
        entity.CreatedAt = DateTime.Now;
        _storage[entity.Id] = entity;
        
        return entity;
    }
    
    public async Task<DeleteDataEntity> GetByIdAsync(int id)
    {
        await Task.Delay(13);
        return _storage.TryGetValue(id, out var entity) ? entity : null;
    }
    
    public async Task<IEnumerable<DeleteDataEntity>> GetAllAsync()
    {
        await Task.Delay(36);
        return _storage.Values;
    }
    
    public async Task<DeleteDataEntity> UpdateAsync(DeleteDataEntity entity)
    {
        await Task.Delay(72);
        
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
        await Task.Delay(50);
        return _storage.Remove(id);
    }
    
    public async Task<int> CountAsync()
    {
        await Task.Delay(11);
        return _storage.Count;
    }
}
