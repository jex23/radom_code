// Random JavaScript function generated on 2025-11-08

function check_response(params_pha) {
    const result = [];
    const multiplier = 5;
    
    if (!Array.isArray(params_pha)) {
        params_pha = [params_pha];
    }
    
    params_pha.forEach((item, index) => {
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
const testData = [41, 61, 37, 28, 2];
const processed = check_response(testData);
console.log('Processed data:', processed);

module.exports = check_response;
