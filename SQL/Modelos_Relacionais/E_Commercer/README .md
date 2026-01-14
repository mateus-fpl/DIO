# Desafio de Modelagem de Dados: E-Commerce (Refinado) 🚀
Este repositório contém a evolução do modelo de banco de dados para um cenário de E-commerce, desenvolvido como parte da formação em Banco de Dados na **DIO (Digital Innovation One)**.

## 📋 Contexto do Desafio
O objetivo foi refinar um modelo conceitual/lógico básico, adicionando regras de negócio mais próximas do mundo real.

### Principais Implementações:
* **Diferenciação de Clientes (PF/PJ):** Uma conta de cliente pode ser de Pessoa Física (CPF) ou Pessoa Jurídica (CNPJ), mas nunca ambas simultaneamente.
* **Gestão de Pagamentos:** O cliente agora pode cadastrar e gerenciar múltiplas formas de pagamento (Cartões, PIX, Boleto).
* **Controle de Entregas:** Adição de uma entidade para rastreamento de pedidos, incluindo status e código de rastreio.

---

## 🏗️ Estrutura do Modelo Relacional

O modelo foi construído utilizando o **MySQL Workbench** e foca em integridade referencial e normalização.

### 1. Especialização de Cliente
Para evitar campos nulos e redundância, foi utilizada a técnica de **Herança/Especialização**:
* **Tabela `Cliente`**: Dados genéricos e comuns.
* **Tabela `Pessoa_Fisica`**: Dados específicos de PF (1:1 Identificador).
* **Tabela `Pessoa_Juridica`**: Dados específicos de PJ (1:1 Identificador).

### 2. Pagamentos e Entregas
* **Relação N:M (Muitos para Muitos):** Implementada entre `Cliente` e `Forma_Pagamento` através de uma tabela associativa, permitindo maior flexibilidade no checkout.
* **Entregas:** Uma nova entidade conectada a `Pedido` para gerenciar o ciclo de vida logístico do envio.

---

## 🛠️ Ferramentas Utilizadas
* [MySQL Workbench](https://www.mysql.com/products/workbench/) - Modelagem EER.
* Linguagem SQL (Preparado para Forward Engineering).
