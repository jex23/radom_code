// Random TypeScript interface generated on 2025-12-17

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
