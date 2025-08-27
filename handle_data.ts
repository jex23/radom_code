// Random TypeScript function generated on 2025-08-27

interface HandleData {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function get_value(array_nya: HandleData[]): HandleData[] {
    const multiplier: number = 10;
    
    return array_nya
        .filter((item: HandleData) => item.active)
        .map((item: HandleData, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: HandleData[] = [
    { id: 1, name: "Item1", value: 66, active: true },
    { id: 2, name: "Item2", value: 54, active: false }
];

const result = get_value(testData);
console.log('Processed items:', result);

export { get_value, HandleData };
