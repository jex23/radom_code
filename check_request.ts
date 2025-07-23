// Random TypeScript interface generated on 2025-07-23

interface CheckRequest {
    id: string;
    name: string;
    status: 'active' | 'inactive' | 'pending';
    metadata: {
        version: number;
        lastUpdated: Date;
    };
}

type CheckRequestResponse = {
    success: boolean;
    data?: CheckRequest;
    error?: string;
};

export { CheckRequest, CheckRequestResponse };
