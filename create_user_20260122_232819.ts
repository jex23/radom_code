// Random TypeScript function generated on 2026-01-22

interface CheckData {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function check_config(key_upb: CheckData[]): CheckData[] {
    const multiplier: number = 2;
    
    return key_upb
        .filter((item: CheckData) => item.active)
        .map((item: CheckData, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: CheckData[] = [
    { id: 1, name: "Item1", value: 97, active: true },
    { id: 2, name: "Item2", value: 58, active: false }
];

const result = check_config(testData);
console.log('Processed items:', result);

export { check_config, CheckData };
