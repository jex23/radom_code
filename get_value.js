// Random JavaScript function generated on 2025-07-01

function handle_data(result_euw) {
    const result = [];
    const multiplier = 2;
    
    if (!Array.isArray(result_euw)) {
        result_euw = [result_euw];
    }
    
    result_euw.forEach((item, index) => {
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
const testData = [53, 17, 65, 39, 64];
const processed = handle_data(testData);
console.log('Processed data:', processed);

module.exports = handle_data;
