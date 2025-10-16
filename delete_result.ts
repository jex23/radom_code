// Random TypeScript function generated on 2025-10-16

interface UpdateRequest {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function validate_data(name_omb: UpdateRequest[]): UpdateRequest[] {
    const multiplier: number = 6;
    
    return name_omb
        .filter((item: UpdateRequest) => item.active)
        .map((item: UpdateRequest, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: UpdateRequest[] = [
    { id: 1, name: "Item1", value: 82, active: true },
    { id: 2, name: "Item2", value: 27, active: false }
];

const result = validate_data(testData);
console.log('Processed items:', result);

export { validate_data, UpdateRequest };
