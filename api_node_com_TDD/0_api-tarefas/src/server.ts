import { createApp } from "./app";
import { env } from "./env";

const app = createApp();

function startServer() {
    try {
        app.listen({
            port: env.PORT,
            host: '0.0.0.0'
        })
        console.log(`server is runing => http://localhost:${env.PORT}`)
    } catch (error) {
        console.log('Erro ao tentar rodar o servidor: 🚨🚨' + '\n' + error)
    }
}

startServer()