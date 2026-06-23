import fastify, { type FastifyInstance } from 'fastify'
import { appRoutes } from './routes/index.js'


export function createApp(): FastifyInstance {
    const app = fastify({ logger: true })

    app.register(appRoutes)

    return app
}

