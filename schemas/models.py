from pydantic import BaseModel, Field
from datetime import date

from schemas.types import (
    CNPJ,
    CNPJOrCPF,
    Currency,
    CurrencyOptional,
    InvoiceDate,
    UF,
)


class InvoiceData(BaseModel):
    descricao_servico: str = Field(
        ...,
        description="Service or product description",
        alias="descricao_servico",
    )
    valor_servico: Currency = Field(
        ...,
        description="Service or product value",
        alias="valor_servico",
    )
    numero_nota: str = Field(
        ...,
        description="Invoice number",
        alias="numero_nota",
    )
    data_emissao: InvoiceDate = Field(
        ...,
        description="Invoice issuance date",
        alias="data_emissao",
    )
    valor_total: Currency = Field(
        ...,
        description="Total invoice value",
        alias="valor_total",
    )
    cnpj_prestador: CNPJ = Field(
        ...,
        description="Service provider CNPJ",
        alias="cnpj_prestador",
    )
    nome_prestador: str | None = Field(
        None,
        description="Provider/issuer name or company name",
        alias="nome_prestador",
    )
    serie_nota: str | None = Field(
        None,
        description="Invoice series",
        alias="serie_nota",
    )
    chave_acesso: str | None = Field(
        None,
        description="Invoice access key (usually 44 digits)",
        alias="chave_acesso",
    )
    cnpj_destinatario: CNPJOrCPF = Field(
        None,
        description="Recipient CNPJ or CPF",
        alias="cnpj_destinatario",
    )
    nome_destinatario: str | None = Field(
        None,
        description="Recipient name or company name",
        alias="nome_destinatario",
    )
    municipio_emissao: str | None = Field(
        None,
        description="Invoice issuance municipality",
        alias="municipio_emissao",
    )
    uf_emissao: UF = Field(
        None,
        description="State (UF) of invoice issuance",
        alias="uf_emissao",
    )
    valor_impostos: CurrencyOptional = Field(
        None,
        description="Total taxes value",
        alias="valor_impostos",
    )

    class Config:
        """Pydantic configuration."""

        json_encoders = {
            date: lambda v: v.isoformat(),
        }
        populate_by_name = True

