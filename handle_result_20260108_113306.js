// Random JavaScript function generated on 2026-01-08

function create_request(name_egk) {
    const result = [];
    const multiplier = 10;
    
    if (!Array.isArray(name_egk)) {
        name_egk = [name_egk];
    }
    
    name_egk.forEach((item, index) => {
        result.push({
            original: item,
            processed: item * multiplier,
            index: index,
            timestamp: new Date().toISOString()
        });
    });
    
    return result;
}

// Example usage
const testData = [58, 92, 93, 33, 7];
const processed = create_request(testData);
console.log('Processed data:', processed);

module.exports = create_request;
