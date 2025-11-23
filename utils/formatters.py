"""Formatting utilities for invoice data.

This module provides functions to format invoice data for display,
including CNPJ formatting and currency formatting.
"""


def format_cnpj(cnpj: str) -> str:
    """Format CNPJ string with dots, slash and hyphen.

    Args:
        cnpj: CNPJ string with only digits (14 digits).

    Returns:
        Formatted CNPJ string (XX.XXX.XXX/XXXX-XX).

    Raises:
        ValueError: If CNPJ doesn't have 14 digits.
    """
    # Remove any existing formatting
    cnpj_clean = "".join(filter(str.isdigit, cnpj))
    
    if len(cnpj_clean) != 14:
        raise ValueError(f"CNPJ must have 14 digits, received {len(cnpj_clean)}")
    
    # Format: XX.XXX.XXX/XXXX-XX
    return f"{cnpj_clean[:2]}.{cnpj_clean[2:5]}.{cnpj_clean[5:8]}/{cnpj_clean[8:12]}-{cnpj_clean[12:]}"


def format_cpf(cpf: str) -> str:
    """Format CPF string with dots and hyphen.

    Args:
        cpf: CPF string with only digits (11 digits).

    Returns:
        Formatted CPF string (XXX.XXX.XXX-XX).

    Raises:
        ValueError: If CPF doesn't have 11 digits.
    """
    # Remove any existing formatting
    cpf_clean = "".join(filter(str.isdigit, cpf))
    
    if len(cpf_clean) != 11:
        raise ValueError(f"CPF must have 11 digits, received {len(cpf_clean)}")
    
    # Format: XXX.XXX.XXX-XX
    return f"{cpf_clean[:3]}.{cpf_clean[3:6]}.{cpf_clean[6:9]}-{cpf_clean[9:]}"


def format_cnpj_or_cpf(value: str | None) -> str | None:
    """Format CNPJ or CPF based on length.

    Args:
        value: CNPJ or CPF string with only digits.

    Returns:
        Formatted CNPJ or CPF string, or None if value is None.
    """
    if value is None:
        return None
    
    value_clean = "".join(filter(str.isdigit, value))
    
    if len(value_clean) == 14:
        return format_cnpj(value_clean)
    elif len(value_clean) == 11:
        return format_cpf(value_clean)
    else:
        # Return as is if doesn't match expected lengths
        return value


def format_currency(value: float | None) -> str | None:
    """Format float value as Brazilian currency (R$).

    Args:
        value: Float value to format.

    Returns:
        Formatted currency string (R$ X.XXX,XX), or None if value is None.
    """
    if value is None:
        return None
    
    # Format with 2 decimal places
    # Split integer and decimal parts
    integer_part = int(value)
    decimal_part = round((value - integer_part) * 100)
    
    # Format integer part with dots as thousands separator
    integer_str = f"{integer_part:,}".replace(",", ".")
    
    # Format decimal part with 2 digits
    decimal_str = f"{decimal_part:02d}"
    
    return f"R$ {integer_str},{decimal_str}"

