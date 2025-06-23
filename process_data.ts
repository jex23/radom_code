// Random TypeScript function generated on 2025-06-23

interface GetResult {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function update_value(request_nxd: GetResult[]): GetResult[] {
    const multiplier: number = 2;
    
    return request_nxd
        .filter((item: GetResult) => item.active)
        .map((item: GetResult, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: GetResult[] = [
    { id: 1, name: "Item1", value: 39, active: true },
    { id: 2, name: "Item2", value: 46, active: false }
];

const result = update_value(testData);
console.log('Processed items:', result);

export { update_value, GetResult };
