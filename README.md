# 🥗 Diet Tracker API

Esse projeto foi criado para resolver um desafio da Rockeatseat da trilha de python para desenvolver uma API simples para registrar, listar, atualizar e excluir refeições, incluindo o controle se cada refeição está dentro da dieta ou não.

## 📦 Tecnologias Utilizadas

- Python 3.x
- Flask
- SQLAlchemy (ORM)
- SQLite (banco de dados local)

---

## 🚀 Como rodar o projeto

### Pré-requisitos

- Python 3 instalado
- `pip` (gerenciador de pacotes do Python)

### 1. Instale as dependências

```bash
pip install -r requirements.txt
```

Se não tiver o `requirements.txt`, crie um com:

```txt
Flask
Flask-SQLAlchemy
```

### 2. Rode o servidor

```bash
python app.py
```

A API estará disponível em: [http://localhost:5000](http://localhost:5000)

---

## 📚 Endpoints disponíveis

### ➕ Criar refeição

`POST /meals`

```json
{
  "name": "Café da manhã",
  "description": "Ovos mexidos e frutas",
  "datetime": "2025-06-02 08:00",
  "on_diet": true
}
```

### 📋 Listar todas as refeições

`GET /meals`

**Resposta:**

```json
[
  {
    "id": 1,
    "name": "Almoço",
    "description": "Arroz, feijão e frango",
    "datetime": "2025-06-02T12:00:00",
    "on_diet": false
  }
]
```

### 🔍 Obter uma refeição específica

`GET /meals/<meal_id>`

Exemplo: `GET /meals/1`

### ✏️ Atualizar uma refeição

`PUT /meals/<meal_id>`

```json
{
  "name": "Jantar",
  "description": "Salada e sopa",
  "datetime": "2025-06-02 19:00",
  "on_diet": true
}
```

### ❌ Deletar refeição

`DELETE /meals/<meal_id>`

---

## 🗃️ Estrutura do Projeto

```
diet-tracker/
│
├── app.py              # Aplicação principal Flask
├── models.py           # Modelo Meal com SQLAlchemy
├── database.py         # Inicialização do banco de dados
└── requirements.txt    # Dependências do projeto
```

---

## 🧠 Modelo de Dados

### Tabela `Meal`

| Campo       | Tipo         | Descrição                         |
|-------------|--------------|------------------------------------|
| id          | Integer      | ID da refeição (auto incremento)  |
| name        | String       | Nome da refeição                  |
| description | String       | Descrição do prato                |
| datetime    | DateTime     | Data e hora da refeição           |
| on_diet     | Boolean      | Está dentro da dieta?             |

---

## ✅ Futuras Melhorias

- Autenticação de usuários
- Filtros por data ou status (`on_diet`)
- Dashboard com estatísticas

---