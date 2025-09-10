// Random JavaScript function generated on 2025-09-10

function check_value(request_rhf) {
    const result = [];
    const multiplier = 6;
    
    if (!Array.isArray(request_rhf)) {
        request_rhf = [request_rhf];
    }
    
    request_rhf.forEach((item, index) => {
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
const testData = [25, 6, 72, 85, 80];
const processed = check_value(testData);
console.log('Processed data:', processed);

module.exports = check_value;
