import {
    describe,
    it,
    expect
} from 'vitest'
import { createApp } from '../src/app.js'


describe('GET /helth', () => {
    const app = createApp()
    it('deve retornar o status 200', async () => {
        const response  = await app.inject({
            method: 'GET',
            url: '/helth'
        })

        expect(response.statusCode).toEqual(200)
    })
})