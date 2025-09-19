// Random TypeScript function generated on 2025-09-19

interface HandleValue {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function process_result(data_dju: HandleValue[]): HandleValue[] {
    const multiplier: number = 5;
    
    return data_dju
        .filter((item: HandleValue) => item.active)
        .map((item: HandleValue, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: HandleValue[] = [
    { id: 1, name: "Item1", value: 72, active: true },
    { id: 2, name: "Item2", value: 86, active: false }
];

const result = process_result(testData);
console.log('Processed items:', result);

export { process_result, HandleValue };
