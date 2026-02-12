// Random TypeScript function generated on 2026-02-12

interface UpdateResponse {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function create_request(key_dar: UpdateResponse[]): UpdateResponse[] {
    const multiplier: number = 2;
    
    return key_dar
        .filter((item: UpdateResponse) => item.active)
        .map((item: UpdateResponse, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: UpdateResponse[] = [
    { id: 1, name: "Item1", value: 41, active: true },
    { id: 2, name: "Item2", value: 18, active: false }
];

const result = create_request(testData);
console.log('Processed items:', result);

export { create_request, UpdateResponse };
