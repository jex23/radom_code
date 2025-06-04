// Random TypeScript interface generated on 2025-06-04

interface CheckUser {
    id: string;
    name: string;
    status: 'active' | 'inactive' | 'pending';
    metadata: {
        version: number;
        lastUpdated: Date;
    };
}

type CheckUserResponse = {
    success: boolean;
    data?: CheckUser;
    error?: string;
};

export { CheckUser, CheckUserResponse };
