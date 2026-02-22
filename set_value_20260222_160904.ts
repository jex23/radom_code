// Random TypeScript function generated on 2026-02-22

interface SetRequest {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function process_user(count_tue: SetRequest[]): SetRequest[] {
    const multiplier: number = 7;
    
    return count_tue
        .filter((item: SetRequest) => item.active)
        .map((item: SetRequest, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: SetRequest[] = [
    { id: 1, name: "Item1", value: 65, active: true },
    { id: 2, name: "Item2", value: 56, active: false }
];

const result = process_user(testData);
console.log('Processed items:', result);

export { process_user, SetRequest };
