// Random TypeScript function generated on 2026-01-27

interface UpdateRequest {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function update_data(name_vnc: UpdateRequest[]): UpdateRequest[] {
    const multiplier: number = 10;
    
    return name_vnc
        .filter((item: UpdateRequest) => item.active)
        .map((item: UpdateRequest, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: UpdateRequest[] = [
    { id: 1, name: "Item1", value: 69, active: true },
    { id: 2, name: "Item2", value: 33, active: false }
];

const result = update_data(testData);
console.log('Processed items:', result);

export { update_data, UpdateRequest };
