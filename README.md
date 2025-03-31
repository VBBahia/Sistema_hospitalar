<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Cadastro de Pacientes</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container mt-5">
        <div class="text-center mb-4">
            <h1 class="text-primary">Sistema de Cadastro de Pacientes</h1>
            <p class="text-muted">Gerencie informações de pacientes de forma simples e eficiente.</p>
        </div>

        <div class="card shadow-sm">
            <div class="card-body">
                <h2 class="card-title text-success">Descrição</h2>
                <p>Este programa em Python permite cadastrar informações de pacientes, como nome, idade, altura, peso, CPF, contato, estado civil, alergias e motivo da consulta. Os dados são validados e armazenados em um arquivo CSV.</p>
            </div>
        </div>

        <div class="card shadow-sm mt-4">
            <div class="card-body">
                <h2 class="card-title text-info">Funções</h2>
                <ul>
                    <li>Validação de dados de entrada (nome, idade, altura, peso, CPF, contato).</li>
                    <li>Armazenamento dos dados em um arquivo CSV.</li>
                    <li>Interface interativa via console para coleta de dados.</li>
                </ul>
            </div>
        </div>

        <div class="card shadow-sm mt-4">
            <div class="card-body">
                <h2 class="card-title text-warning">Como Usar</h2>
                <ol>
                    <li>Certifique-se de ter o Python instalado.</li>
                    <li>Salve os arquivos <code>Pacientes.py</code> e <code>Main.py</code> no mesmo diretório.</li>
                    <li>Execute o comando <code>python Main.py</code> no terminal.</li>
                    <li>Siga as instruções no terminal.</li>
                </ol>
            </div>
        </div>

        <div class="card shadow-sm mt-4">
            <div class="card-body">
                <h2 class="card-title text-danger">Estrutura de Arquivos</h2>
                <ul>
                    <li><code>Pacientes.py</code>: Contém a classe Pacientes e suas subclasses para validação de dados.</li>
                    <li><code>Main.py</code>: Contém a lógica principal do programa e a interação com o usuário.</li>
                    <li><code>dadosPacientes.csv</code>: Arquivo CSV onde os dados dos pacientes são armazenados.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
