// Random TypeScript function generated on 2025-12-15

interface GetData {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function handle_config(index_sxs: GetData[]): GetData[] {
    const multiplier: number = 2;
    
    return index_sxs
        .filter((item: GetData) => item.active)
        .map((item: GetData, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: GetData[] = [
    { id: 1, name: "Item1", value: 69, active: true },
    { id: 2, name: "Item2", value: 28, active: false }
];

const result = handle_config(testData);
console.log('Processed items:', result);

export { handle_config, GetData };
