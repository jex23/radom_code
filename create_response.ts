// Random TypeScript function generated on 2025-09-14

interface DeleteRequest {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function check_data(list_evc: DeleteRequest[]): DeleteRequest[] {
    const multiplier: number = 4;
    
    return list_evc
        .filter((item: DeleteRequest) => item.active)
        .map((item: DeleteRequest, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: DeleteRequest[] = [
    { id: 1, name: "Item1", value: 43, active: true },
    { id: 2, name: "Item2", value: 43, active: false }
];

const result = check_data(testData);
console.log('Processed items:', result);

export { check_data, DeleteRequest };
