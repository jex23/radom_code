// Random TypeScript interface generated on 2025-09-16

interface UpdateUser {
    id: string;
    name: string;
    status: 'active' | 'inactive' | 'pending';
    metadata: {
        version: number;
        lastUpdated: Date;
    };
}

type UpdateUserResponse = {
    success: boolean;
    data?: UpdateUser;
    error?: string;
};

export { UpdateUser, UpdateUserResponse };
