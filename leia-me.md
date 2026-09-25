==================================================
          SISTEMA DE ORGANIZAÇÃO DE TAREFAS
==================================================
Disciplina: Análise e Desenvolvimento de Sistemas
Projeto Extensionista II — Tecnologia Aplicada à Inclusão Digital

Autor(es):
  Seu Nome Completo        — RU: 000000
  Nome do Segundo Aluno    — RU: 000000

ODS Relacionados:
  ✅ ODS 4 — Educação de Qualidade
  ✅ ODS 9 — Indústria, Inovação e Infraestrutura

==================================================
💡 SOBRE O SISTEMA
==================================================
Este sistema foi desenvolvido para ajudar estudantes a
organizar, registrar e acompanhar suas tarefas e prazos
acadêmicos de forma simples e prática.

Tecnologias utilizadas:
  • Linguagem Python
  • Framework Flask (Interface Web)
  • Banco de Dados SQLite (em arquivo, sem instalação)

Diferencial: O banco de dados é criado automaticamente!
Não é necessário instalar nem configurar nenhum programa
extra de banco de dados.

==================================================
🚀 COMO USAR — PASSO A PASSO
==================================================

1️⃣ PRÉ-REQUISITO: Ter o Python instalado
   — Baixe em: https://www.python.org/downloads/
   ⚠️ Durante a instalação, MARQUE a opção:
        "Add Python to PATH"

2️⃣ Instalar a biblioteca Flask (uma vez só):
   Abra o terminal dentro da pasta do projeto e digite:

     py -m pip install flask

3️⃣ Executar o sistema:
   No mesmo terminal, digite:

     py app.py

4️⃣ Acessar no navegador:
   Abra o endereço abaixo no Chrome, Edge ou Firefox:

     http://127.0.0.1:5000

✅ Pronto! O sistema já está funcionando!
   O arquivo "tarefas.db" será criado automaticamente
   na pasta do projeto na primeira execução.

==================================================
📋 FUNCIONALIDADES
==================================================
  ✅ Cadastrar nova tarefa:
     • Título
     • Disciplina
     • Descrição / Detalhes
     • Data e Hora do Prazo

  ✅ Visualizar todas as tarefas
     • Ordenadas pela data do prazo (mais próximas primeiro)
     • Destaque visual: pendente (laranja) / concluída (verde)

  ✅ Marcar tarefa como concluída
  ✅ Excluir tarefa

==================================================
📂 ESTRUTURA DO PROJETO
==================================================
sistema-tarefas/
├── app.py              ← Código principal do sistema
├── LEIA-ME.txt         ← Este arquivo de instruções
├── tarefas.db          ← Banco de dados (cria sozinho)
└── templates/
    ├── index.html      ← Página inicial / lista de tarefas
    └── cadastrar.html  ← Formulário de cadastro

==================================================
ℹ️ OBSERVAÇÕES IMPORTANTES
==================================================
• O arquivo "tarefas.db" armazena TODOS os dados.
  Se apagar este arquivo, os cadastros serão perdidos.

• Para fazer backup, basta copiar o arquivo "tarefas.db"
  para outro local.

• Funciona em qualquer computador com Python instalado.
  Não há caminhos fixos do computador de origem.

• Para encerrar o sistema: no terminal, pressione
  Ctrl + C e feche a janela.

==================================================
💬 SUPORTE
==================================================
Em caso de dúvidas:
  1. Confirme que o Python está instalado: digite
     "py --version" no terminal
  2. Reinstale as bibliotecas:
     "py -m pip install --upgrade flask"
  3. Exclua o arquivo "tarefas.db" e execute novamente

==================================================