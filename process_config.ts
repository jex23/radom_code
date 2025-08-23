// Random TypeScript function generated on 2025-08-23

interface ValidateResult {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function get_config(array_zmu: ValidateResult[]): ValidateResult[] {
    const multiplier: number = 2;
    
    return array_zmu
        .filter((item: ValidateResult) => item.active)
        .map((item: ValidateResult, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: ValidateResult[] = [
    { id: 1, name: "Item1", value: 55, active: true },
    { id: 2, name: "Item2", value: 42, active: false }
];

const result = get_config(testData);
console.log('Processed items:', result);

export { get_config, ValidateResult };
