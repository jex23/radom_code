// Random TypeScript function generated on 2025-10-28

interface HandleResult {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function validate_data(data_era: HandleResult[]): HandleResult[] {
    const multiplier: number = 6;
    
    return data_era
        .filter((item: HandleResult) => item.active)
        .map((item: HandleResult, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: HandleResult[] = [
    { id: 1, name: "Item1", value: 93, active: true },
    { id: 2, name: "Item2", value: 26, active: false }
];

const result = validate_data(testData);
console.log('Processed items:', result);

export { validate_data, HandleResult };
