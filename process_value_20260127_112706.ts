// Random TypeScript function generated on 2026-01-27

interface ValidateData {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function update_config(request_hss: ValidateData[]): ValidateData[] {
    const multiplier: number = 9;
    
    return request_hss
        .filter((item: ValidateData) => item.active)
        .map((item: ValidateData, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: ValidateData[] = [
    { id: 1, name: "Item1", value: 52, active: true },
    { id: 2, name: "Item2", value: 26, active: false }
];

const result = update_config(testData);
console.log('Processed items:', result);

export { update_config, ValidateData };
