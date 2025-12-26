// Random JavaScript function generated on 2025-12-26

function check_data(name_gtg) {
    const result = [];
    const multiplier = 6;
    
    if (!Array.isArray(name_gtg)) {
        name_gtg = [name_gtg];
    }
    
    name_gtg.forEach((item, index) => {
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
const testData = [54, 11, 39, 53, 88];
const processed = check_data(testData);
console.log('Processed data:', processed);

module.exports = check_data;
