// Random JavaScript function generated on 2025-06-03

function check_data(string_fcv) {
    const result = [];
    const multiplier = 4;
    
    if (!Array.isArray(string_fcv)) {
        string_fcv = [string_fcv];
    }
    
    string_fcv.forEach((item, index) => {
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
const testData = [7, 56, 15, 20, 90];
const processed = check_data(testData);
console.log('Processed data:', processed);

module.exports = check_data;
