// Random TypeScript function generated on 2026-01-06

interface ValidateRequest {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function set_config(list_yfg: ValidateRequest[]): ValidateRequest[] {
    const multiplier: number = 6;
    
    return list_yfg
        .filter((item: ValidateRequest) => item.active)
        .map((item: ValidateRequest, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: ValidateRequest[] = [
    { id: 1, name: "Item1", value: 82, active: true },
    { id: 2, name: "Item2", value: 39, active: false }
];

const result = set_config(testData);
console.log('Processed items:', result);

export { set_config, ValidateRequest };
