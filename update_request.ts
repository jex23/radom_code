// Random TypeScript interface generated on 2025-08-14

interface CreateUser {
    id: string;
    name: string;
    status: 'active' | 'inactive' | 'pending';
    metadata: {
        version: number;
        lastUpdated: Date;
    };
}

type CreateUserResponse = {
    success: boolean;
    data?: CreateUser;
    error?: string;
};

export { CreateUser, CreateUserResponse };
