"""Validators for invoice data fields.

This module provides validation functions for invoice data fields
like CNPJ, CPF, dates, and currency values.
"""

from datetime import date, datetime


def validate_cnpj(v: str) -> str:
    cnpj_clean = "".join(filter(str.isdigit, v))
    if len(cnpj_clean) != 14:
        raise ValueError(
            f"CNPJ must contain exactly 14 numeric digits, received {len(cnpj_clean)}"
        )
    return cnpj_clean


def validate_cnpj_or_cpf(v: str | None) -> str | None:
    """Validate and normalize CNPJ/CPF format.

    Args:
        v: CNPJ/CPF string that may contain formatting characters.

    Returns:
        Normalized CNPJ/CPF string with only digits, or None.

    Raises:
        ValueError: If CNPJ/CPF doesn't contain exactly 11 (CPF) or 14 (CNPJ) digits.
    """
    if v is None:
        return None
    # Remove common formatting characters
    value_clean = "".join(filter(str.isdigit, v))
    if len(value_clean) not in (11, 14):
        raise ValueError(
            f"CNPJ/CPF must contain exactly 11 (CPF) or 14 (CNPJ) numeric digits, received {len(value_clean)}"
        )
    return value_clean


def validate_uf(v: str | None) -> str | None:
    if v is None:
        return None
    v_upper = v.upper().strip()
    if len(v_upper) != 2:
        raise ValueError("UF must have exactly 2 characters")
    return v_upper


def parse_date(v: str | date) -> date:
    if isinstance(v, date):
        return v
    # Try common date formats
    formats = ["%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y"]
    for fmt in formats:
        try:
            return datetime.strptime(v, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Invalid date format: {v}")

