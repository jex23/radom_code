// Random TypeScript function generated on 2025-07-28

interface CheckResponse {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function update_value(params_nwa: CheckResponse[]): CheckResponse[] {
    const multiplier: number = 9;
    
    return params_nwa
        .filter((item: CheckResponse) => item.active)
        .map((item: CheckResponse, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: CheckResponse[] = [
    { id: 1, name: "Item1", value: 13, active: true },
    { id: 2, name: "Item2", value: 60, active: false }
];

const result = update_value(testData);
console.log('Processed items:', result);

export { update_value, CheckResponse };
