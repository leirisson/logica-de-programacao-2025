import { PrismaClient } from "../../src/generated/prisma/client.js";
import { PrismaPg } from '@prisma/adapter-pg'
import { env } from "../../src/env/index.js";

const adapter = new PrismaPg({ connectionString: process.env.DATABASE_URL })

export const prisma = new PrismaClient({
    adapter, 
    log:  env.NODE_ENV === 'dev' ? ['query'] : []
})

