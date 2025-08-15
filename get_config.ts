// Random TypeScript function generated on 2025-08-15

interface ProcessUser {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function process_request(array_isz: ProcessUser[]): ProcessUser[] {
    const multiplier: number = 5;
    
    return array_isz
        .filter((item: ProcessUser) => item.active)
        .map((item: ProcessUser, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: ProcessUser[] = [
    { id: 1, name: "Item1", value: 92, active: true },
    { id: 2, name: "Item2", value: 75, active: false }
];

const result = process_request(testData);
console.log('Processed items:', result);

export { process_request, ProcessUser };
