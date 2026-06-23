import type { FastifyInstance, FastifyReply, FastifyRequest } from "fastify";
import { TarefaController } from "../controllers/tarefaController.js";
import { prisma } from "../../lib/prisma/index.js";


const tarefaController = new TarefaController(prisma);

export async function appRoutes(app: FastifyInstance) {
    app.get('/helth', (_: FastifyRequest, reply: FastifyReply) => {
        return reply.code(200).send({ msg: "api online" })
    })

    app.post('/tarefas', (request: FastifyRequest, reply: FastifyReply) => tarefaController.create(request, reply))
    app.get('/tarefas', (request: FastifyRequest, reply: FastifyReply) => tarefaController.listTasks(request, reply))
    app.get('/tarefas/:id', (request: FastifyRequest, reply: FastifyReply) => tarefaController.getTask(request, reply))
}