<br>
<p align="center">
  <a href="https://ant.design">
    <img width="400" src="assets/header.avif">
  </a>
</p>

<p align="center"><del>This book is the property of the Exiled Prince</p>

# SYCP (Solyd Certified Pentester)
<p><del>Repositório com anotações das atividades de todos os módulos realizados durante meus estudos na área de Cybersecurity através da Solyd, sinta-se livre para clonar e estudar, você vai precisar.</p>

O objetivo deste projeto é servir como um complemento para alunos da certificação [SYCP](https://solyd.com.br/cursos/pentest-do-zero-ao-profissional-v2024/), detalhando ao máximo cada tópico do curso.

<br/>

---

### Caso precise reconstruir o ambiente para as páginas
#### Sobre o ambiente

Todo este projeto é gerenciado pelo Poetry, a versão usada durante o momento da escrita é `1.8.2`:

A versão do Python é a 3.11.7:
```bash
pyenv local 3.11.7
```

Para configurar todo o ambiente basta executar:
```bash
poetry install
```

#### Sobre os comandos

Os comandos para executar funções como deploy, servidor local, etc. Estão sendo feitas pelo `taskipy`:

```bash
task --list
serve executa o servidor do local do mkdocs
build 

```
Para executar qualquer comando, basta usar: `task <comando>`
