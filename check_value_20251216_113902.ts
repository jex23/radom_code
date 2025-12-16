// Random TypeScript function generated on 2025-12-16

interface CreateData {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function get_data(options_apc: CreateData[]): CreateData[] {
    const multiplier: number = 2;
    
    return options_apc
        .filter((item: CreateData) => item.active)
        .map((item: CreateData, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: CreateData[] = [
    { id: 1, name: "Item1", value: 89, active: true },
    { id: 2, name: "Item2", value: 82, active: false }
];

const result = get_data(testData);
console.log('Processed items:', result);

export { get_data, CreateData };
