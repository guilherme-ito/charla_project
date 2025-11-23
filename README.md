# Extração de Dados de Nota Fiscal com IA

Projeto para extração automatizada de informações estruturadas de notas fiscais brasileiras usando PydanticAI e Groq.

## Requisitos

- Python 3.10 ou superior
- Conta no Groq para obter API key

## Instalação

1. Clone o repositório e entre na pasta:
```bash
git clone <url-do-repositorio>
cd charla_project
```

2. Crie e ative um ambiente virtual:
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar (Windows)
venv\Scripts\activate

# Ativar (Linux/Mac)
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Configuração

1. Obtenha sua API key do Groq:
   - Acesse https://groq.com/
   - Crie uma conta e obtenha sua chave gratuita

2. Crie um arquivo `.env` na raiz do projeto:
```env
GROQ_API_KEY=sua_api_key_aqui
```

3. Crie a pasta `pdfs/` na raiz e coloque seus PDFs lá:
```bash
mkdir pdfs
```

## Uso

### Processar um único PDF

```bash
python extract_invoice.py pdfs/nota_fiscal.pdf
```

### Processar todos os PDFs

```bash
# Python (recomendado)
python process_all_pdfs.py

# Linux/Mac (Bash)
chmod +x process_all_pdfs.sh
./process_all_pdfs.sh
```

Os dados extraídos serão exibidos em formato JSON no console.

## Dados Extraídos

- Descrição do serviço/produto
- Valor do serviço e valor total
- Número da nota fiscal e data de emissão
- CNPJ do prestador e nome
- CNPJ/CPF do destinatário e nome
- Série da nota, chave de acesso
- Município e UF de emissão
- Valor dos impostos

## Estrutura do Projeto

```
charla_project/
├── extract_invoice.py          # Script principal (um PDF)
├── process_all_pdfs.py          # Script para múltiplos PDFs
├── process_all_pdfs.sh          # Script bash
├── config/                      # Configurações
│   ├── settings.py              # Configurações e API key
│   └── prompts.py               # Prompts do sistema
├── schemas/                     # Modelos de dados
│   ├── models.py                # Modelo Pydantic principal
│   ├── types.py                 # Tipos customizados
│   └── validators.py            # Validadores
├── services/                    # Lógica de negócio
│   └── extraction_service.py    # Serviço de extração
├── repositories/                # Acesso a dados
│   └── pdf_repository.py        # Leitura de PDFs
├── utils/                       # Utilitários
│   └── formatters.py            # Formatação de dados
├── pdfs/                        # Pasta para PDFs
├── requirements.txt             # Dependências
└── README.md                    # Este arquivo
```

## Tecnologias

- **PydanticAI**: Framework para agentes de IA com validação
- **Groq**: Provedor de LLM (Llama 3.3 70B)
- **pdfplumber**: Extração de texto de PDFs
- **Pydantic**: Validação e serialização de dados
