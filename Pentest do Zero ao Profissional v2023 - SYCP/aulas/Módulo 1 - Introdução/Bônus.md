# Recuperando a 💀 da shell

Nas novas versões do Kali, o separador do usuário e máquina foi alterado para ㉿. Para retornar ao antigo separador, execute os comandos abaixo individualmente com o seu usuário padrão:

```bash
$sed -i 's/prompt_symbol=㉿/prompt_symbol=💀/' ~/.zshrc
```

```bash
$source ~/.zshrc
```
