from datetime import date

from pydantic import BaseModel

from schemas.types import (
    CNPJ,
    CNPJOrCPF,
    Currency,
    CurrencyOptional,
    InvoiceDate,
    UF,
)


class InvoiceData(BaseModel):
    descricao_servico: str
    valor_servico: Currency
    numero_nota: str
    data_emissao: InvoiceDate
    valor_total: Currency
    cnpj_prestador: CNPJ
    nome_prestador: str | None = None
    serie_nota: str | None = None
    chave_acesso: str | None = None
    cnpj_destinatario: CNPJOrCPF = None
    nome_destinatario: str | None = None
    municipio_emissao: str | None = None
    uf_emissao: UF = None
    valor_impostos: CurrencyOptional = None

    class Config:
        """Pydantic configuration."""

        json_encoders = {
            date: lambda v: v.isoformat(),
        }
        populate_by_name = True

