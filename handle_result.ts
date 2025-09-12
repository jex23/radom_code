// Random TypeScript function generated on 2025-09-13

interface DeleteResult {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function update_result(params_xxm: DeleteResult[]): DeleteResult[] {
    const multiplier: number = 4;
    
    return params_xxm
        .filter((item: DeleteResult) => item.active)
        .map((item: DeleteResult, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: DeleteResult[] = [
    { id: 1, name: "Item1", value: 32, active: true },
    { id: 2, name: "Item2", value: 18, active: false }
];

const result = update_result(testData);
console.log('Processed items:', result);

export { update_result, DeleteResult };
