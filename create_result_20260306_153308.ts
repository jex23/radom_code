// Random TypeScript function generated on 2026-03-06

interface DeleteResponse {
    id: number;
    name: string;
    value: number;
    active: boolean;
}

function process_config(count_xmv: DeleteResponse[]): DeleteResponse[] {
    const multiplier: number = 5;
    
    return count_xmv
        .filter((item: DeleteResponse) => item.active)
        .map((item: DeleteResponse, index: number) => ({
            ...item,
            value: item.value * multiplier
        }));
}

// Example usage
const testData: DeleteResponse[] = [
    { id: 1, name: "Item1", value: 65, active: true },
    { id: 2, name: "Item2", value: 28, active: false }
];

const result = process_config(testData);
console.log('Processed items:', result);

export { process_config, DeleteResponse };
