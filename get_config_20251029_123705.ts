// Random TypeScript function generated on 2025-10-29

interface UpdateData {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function validate_response(options_pio: UpdateData[]): UpdateData[] {
    const multiplier: number = 9;
    
    return options_pio
        .filter((item: UpdateData) => item.active)
        .map((item: UpdateData, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: UpdateData[] = [
    { id: 1, name: "Item1", value: 62, active: true },
    { id: 2, name: "Item2", value: 38, active: false }
];

const result = validate_response(testData);
console.log('Processed items:', result);

export { validate_response, UpdateData };
