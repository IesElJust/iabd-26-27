"""API docent local per a la consulta extractiva del laboratori RAG."""
from pathlib import Path
import importlib.util
from typing import Literal
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, Field, field_validator

lab = Path(__file__).resolve().parents[1] / 'rag-i-embeddings' / 'laboratori.py'
spec = importlib.util.spec_from_file_location('recuperacio_helpdesk', lab)
recuperacio = importlib.util.module_from_spec(spec)
spec.loader.exec_module(recuperacio)
app = FastAPI(title='Helpdesk: laboratori extractiu')


class Consulta(BaseModel):
    model_config = ConfigDict(extra='forbid', str_strip_whitespace=True)
    pregunta: str = Field(strict=True, min_length=1, max_length=1000)

    @field_validator('pregunta')
    @classmethod
    def no_buida(cls, value):
        if not value.strip():
            raise ValueError('La pregunta no pot estar buida.')
        return value.strip()


class Font(BaseModel):
    document_id: str
    fragment_id: str
    versio: str


class Resposta(BaseModel):
    estat: Literal['derivar', 'fragment_recuperat']
    resposta: str
    fonts: list[Font]
    puntuacio: float


@app.post('/consulta', response_model=Resposta)
def consulta(entrada: Consulta):
    try:
        return recuperacio.consultar(entrada.pregunta)
    except OSError as exc:
        raise HTTPException(status_code=503, detail='Corpus temporalment no disponible.') from exc
