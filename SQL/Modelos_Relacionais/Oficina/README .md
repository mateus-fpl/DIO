# Desafio de Modelagem de Dados: Sistema de Oficina Mecânica 🔧
Este projeto faz parte da formação de Banco de Dados da **DIO**, focado em transformar uma narrativa de negócio em um modelo lógico de banco de dados.

## 📋 Narrativa e Requisitos
O objetivo foi criar um sistema para controle e gerenciamento de ordens de serviço (OS) em uma oficina, atendendo aos seguintes pontos:

* **Fluxo de Trabalho:** Clientes levam veículos para conserto ou revisão periódica.
* **Equipes de Mecânicos:** Os veículos são designados a equipes que avaliam e executam os serviços.
* **Ordem de Serviço (OS):** Registro com número, data de emissão, valor total, status e data de conclusão.
* **Composição de Custos:** O valor da OS é a soma dos serviços (tabela de referência de mão de obra) e das peças utilizadas.

## 🏗️ Estrutura do Modelo Relacional (Refinado)
O modelo foi desenvolvido no **MySQL Workbench** e apresenta as seguintes soluções:

### 1. Gestão de Veículos e Clientes
* **Veículo:** Atua como o centro da operação, ligado ao seu dono (Pessoa Física) e ao histórico de pedidos.

### 2. Equipes e Especialidades
* **Mecânicos:** Possuem especialidade individual.
* **Relação N:M:** Implementada entre Mecânicos e Equipes, permitindo que a oficina organize seus colaboradores de forma flexível.

### 3. Detalhamento da OS (Peças e Serviços)
Para atender à regra de que uma OS pode ter vários serviços e várias peças, foram criadas tabelas associativas:
* **`OS_tem_Peças`**: Armazena quais peças foram aplicadas em cada ordem específica.
* **`OS_tem_Serviços`**: Registra os serviços executados com base na tabela de referência de mão de obra.

---

## 🛠️ Ferramentas
* **MySQL Workbench** para o diagrama EER.
* **Markdown** para documentação.
