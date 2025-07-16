// Random TypeScript function generated on 2025-07-16

interface ValidateConfig {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function process_request(response_kvd: ValidateConfig[]): ValidateConfig[] {
    const multiplier: number = 5;
    
    return response_kvd
        .filter((item: ValidateConfig) => item.active)
        .map((item: ValidateConfig, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: ValidateConfig[] = [
    { id: 1, name: "Item1", value: 37, active: true },
    { id: 2, name: "Item2", value: 48, active: false }
];

const result = process_request(testData);
console.log('Processed items:', result);

export { process_request, ValidateConfig };
