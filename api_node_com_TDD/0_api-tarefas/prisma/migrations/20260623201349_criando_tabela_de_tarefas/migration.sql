-- CreateEnum
CREATE TYPE "PRIORIDADE" AS ENUM ('ALTA', 'BAIXA', 'MEDIA');

-- CreateTable
CREATE TABLE "Task" (
    "id" TEXT NOT NULL,
    "titulo" TEXT NOT NULL,
    "descricao" TEXT,
    "emAberto" BOOLEAN NOT NULL DEFAULT true,
    "proprietario" TEXT NOT NULL,
    "prioridade" "PRIORIDADE" NOT NULL DEFAULT 'BAIXA',
    "dataCriacao" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "dataConclusao" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "Task_pkey" PRIMARY KEY ("id")
);
