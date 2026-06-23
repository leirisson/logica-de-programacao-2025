import type { FastifyReply, FastifyRequest } from "fastify";
import type { PrismaClient } from "../generated/prisma/client.js";
import { z } from 'zod'



export class TarefaController {
    constructor(private prisma: PrismaClient) { }

    async create(request: FastifyRequest, reply: FastifyReply) {
        const taskSchema = z.object({
            titulo: z.string(),
            proprietario: z.string()
        })
        const {
            titulo,
            proprietario
        } = taskSchema.parse(request.body)

        try {
            await this.prisma.task.create({
                data: {
                    titulo,
                    proprietario
                }
            })

            return reply.code(201).send()

        } catch (error) {
            console.log(error)
        }
    }

    async listTasks(_: FastifyRequest, reply: FastifyReply) {
        try {
            const tasks = await this.prisma.task.findMany()
            if (tasks.length == 0) {
                reply.code(200).send([])
            }
            reply.send(tasks)
        } catch (error) {
            console.log(error)
        }
    }

    async getTask(request: FastifyRequest, reply: FastifyReply) {
        const idSchemaValidation = z.object({
            id: z.string()
        })
        const id = idSchemaValidation.parse(request.params)
        try {
            const task = await this.prisma.task.findUnique({ where: id})
            if (!task) {
                return reply.code(404).send()
            }
            return reply.send(task)
        } catch (error) {
            console.log(error)
        }
    }
}