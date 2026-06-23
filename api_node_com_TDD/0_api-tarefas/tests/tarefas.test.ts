import {
    describe,
    it,
    afterEach,
    expect
} from 'vitest'
import { createApp } from '../src/app.js'
import { prisma } from '../lib/prisma/index.js'

describe("testar a rota de Tarefas", async () => {

    afterEach(async () => {
        await prisma.task.deleteMany()

    })

    it("criação de uma tarefa", async () => {
        const tarefa = {
            titulo: "Criação de uma nova tarefa",
            proprietario: "leirisson"
        }
        const app = createApp()

        const response = await app.inject({
            method: 'POST',
            url: "/tarefas",
            body: tarefa
        })

        console.log(response.statusCode)
        expect(response.statusCode).toEqual(201)
    })

    it('GET listar todas as tarefas', async () => {
        const tarefa = {
            titulo: "Criação de uma nova tarefa",
            proprietario: "leirisson"
        }

        await prisma.task.create({
            data: tarefa
        })

        const app = createApp()

        const response = await app.inject({
            method: 'GET',
            url: "/tarefas",
        })

        const body = JSON.parse(response.body)

        expect(response.statusCode).toEqual(200)
        expect(body).toHaveLength(1)
    })

    it("GET unica task", async () => {
        const tarefa = {
            titulo: "Criação de uma nova tarefa",
            proprietario: "leirisson"
        }

        const tarefa_ = await prisma.task.create({
            data: tarefa
        })


        const idTarefa = tarefa_?.id

        const app = createApp()

        const response = await app.inject({
            method: 'GET',
            url: `/tarefas/${idTarefa}`,
        })

        const tarefaEcontrada = JSON.parse(response.body)

        expect(response.statusCode).toEqual(200)
        expect(tarefaEcontrada.id).toEqual(tarefa_.id)

    })

    it("GET id não existe", async () => {
        const idTarefa = 1234;
        const app = createApp()

        const response = await app.inject({
            method: 'GET',
            url: `/tarefas/${idTarefa}`,
        })

        expect(response.statusCode).toEqual(404)
    })

})