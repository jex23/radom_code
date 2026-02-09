// Random TypeScript function generated on 2026-02-09

interface UpdateData {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function validate_result(list_vne: UpdateData[]): UpdateData[] {
    const multiplier: number = 9;
    
    return list_vne
        .filter((item: UpdateData) => item.active)
        .map((item: UpdateData, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: UpdateData[] = [
    { id: 1, name: "Item1", value: 90, active: true },
    { id: 2, name: "Item2", value: 65, active: false }
];

const result = validate_result(testData);
console.log('Processed items:', result);

export { validate_result, UpdateData };
