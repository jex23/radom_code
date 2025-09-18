// Random TypeScript interface generated on 2025-09-18

interface DeleteRequest {
    id: string;
    name: string;
    status: 'active' | 'inactive' | 'pending';
    metadata: {
        version: number;
        lastUpdated: Date;
    };
}

type DeleteRequestResponse = {
    success: boolean;
    data?: DeleteRequest;
    error?: string;
};

export { DeleteRequest, DeleteRequestResponse };
