// Random TypeScript function generated on 2025-07-18

interface CheckRequest {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function check_config(key_lzw: CheckRequest[]): CheckRequest[] {
    const multiplier: number = 2;
    
    return key_lzw
        .filter((item: CheckRequest) => item.active)
        .map((item: CheckRequest, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: CheckRequest[] = [
    { id: 1, name: "Item1", value: 73, active: true },
    { id: 2, name: "Item2", value: 43, active: false }
];

const result = check_config(testData);
console.log('Processed items:', result);

export { check_config, CheckRequest };
