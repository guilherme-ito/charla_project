"""Reusable type definitions for invoice data.

This module provides annotated types for invoice fields using
Pydantic's Annotated with validators and constraints.
"""

from datetime import date
from typing import Annotated

from pydantic import AfterValidator, BeforeValidator, Field

from schemas.validators import (
    parse_date,
    validate_cnpj,
    validate_cnpj_or_cpf,
    validate_uf,
)

CNPJ = Annotated[
    str,
    AfterValidator(validate_cnpj),
    Field(
        description="Service provider CNPJ (accepts formatted: XX.XXX.XXX/XXXX-XX)",
        min_length=14,
        max_length=18,  # Accepts formatted CNPJ (14 digits + formatting)
    ),
]

CNPJOrCPF = Annotated[
    str | None,
    BeforeValidator(validate_cnpj_or_cpf),
    Field(
        default=None,
        description="CNPJ or CPF (11 or 14 digits)",
    ),
]

UF = Annotated[
    str | None,
    AfterValidator(validate_uf),
    Field(
        default=None,
        description="State (UF) of issuance",
        max_length=2,
    ),
]

InvoiceDate = Annotated[
    date,
    BeforeValidator(parse_date),
    Field(
        description="Invoice issuance date",
    ),
]

Currency = Annotated[
    float,
    Field(
        description="Monetary value",
        ge=0,
    ),
]

CurrencyOptional = Annotated[
    float | None,
    Field(
        default=None,
        description="Optional monetary value",
        ge=0,
    ),
]

