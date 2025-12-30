// Random TypeScript function generated on 2025-12-30

interface ValidateResponse {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function update_data(response_vdb: ValidateResponse[]): ValidateResponse[] {
    const multiplier: number = 4;
    
    return response_vdb
        .filter((item: ValidateResponse) => item.active)
        .map((item: ValidateResponse, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: ValidateResponse[] = [
    { id: 1, name: "Item1", value: 42, active: true },
    { id: 2, name: "Item2", value: 89, active: false }
];

const result = update_data(testData);
console.log('Processed items:', result);

export { update_data, ValidateResponse };
