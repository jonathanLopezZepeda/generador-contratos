# Este código es compatible en entornos que no soportan el módulo 'ssl'
# Se elimina el uso directo de openai y se simula la respuesta para pruebas locales

from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Permitir CORS para frontend local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ContratoInput(BaseModel):
    nombreContrato: str
    tipoContrato: str
    contratante: str
    contratado: str
    duracion: str
    clausulas: str = ""

@app.post("/generar-contrato")
async def generar_contrato(data: ContratoInput):
    # Simulación local de contrato generado (remplazar con llamada real en producción)
    contrato_generado = f"""
CONTRATO DE {data.tipoContrato.upper()}

Entre {data.contratante} (\"EL CONTRATANTE\") y {data.contratado} (\"EL CONTRATADO\").

Este contrato tiene una duración de {data.duracion}.

Ambas partes acuerdan las siguientes cláusulas:
1. El contratado se compromete a cumplir con los términos del contrato.
2. El contratante se compromete a realizar los pagos acordados.
{f"3. {data.clausulas}" if data.clausulas else ""}

Firmado en conformidad por ambas partes conforme a la legislación de los Estados Unidos Mexicanos.
"""

    return {"contrato": contrato_generado.strip()}
