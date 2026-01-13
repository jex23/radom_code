// Random TypeScript function generated on 2026-01-13

interface SetRequest {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function validate_config(list_nbd: SetRequest[]): SetRequest[] {
    const multiplier: number = 3;
    
    return list_nbd
        .filter((item: SetRequest) => item.active)
        .map((item: SetRequest, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: SetRequest[] = [
    { id: 1, name: "Item1", value: 80, active: true },
    { id: 2, name: "Item2", value: 27, active: false }
];

const result = validate_config(testData);
console.log('Processed items:', result);

export { validate_config, SetRequest };
