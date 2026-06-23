import z from 'zod'
import 'dotenv/config'

const envSchemaValidade = z.object({
    DATABASE_URL: z.string(),
    NODE_ENV:z.enum(['dev', 'test', 'production']),
    PORT: z.coerce.number().default(3334)
})


const _env = envSchemaValidade.safeParse(process.env)


if (_env.success === false) {
    console.error("❌ Erro de validação nas variaveis de ambiente", _env.error.format())
    throw new Error("❌ Erro de validação nas variaveis de ambiente")
}


export const env = _env.data