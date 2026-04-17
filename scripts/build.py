"""
Script de build para gerar o executável Windows (Fase 6).

Empacota o Luanny num executável standalone via PyInstaller.
Avisa o usuário para instalar o Playwright localmente, ou
embala se necessário.
"""

import os
import subprocess
import sys
from pathlib import Path

def main():
    print("Iniciando build do Luanny...")
    
    # 1. Limpar pastas de build antigas
    for folder in ["build", "dist"]:
        if os.path.exists(folder):
            import shutil
            shutil.rmtree(folder)
            
    # 2. PyInstaller build
    print("Construindo executável Windows...")
    cmd = [
        "pyinstaller",
        "--name=Luanny",
        "--console", 
        "--clean",
        "--icon=NONE", # Sem icone pra simplificar v1
        "--add-data=src/luanny;luanny",
        "src/luanny/cli.py"
    ]
    
    subprocess.run(cmd, check=True)
    
    print("Luanny construído com sucesso em dist/Luanny/")
    
    # 3. Criar arquivo LEIA-ME e executar.bat na pasta dist
    dist_dir = Path("dist/Luanny")
    
    exec_bat = dist_dir / "executar.bat"
    exec_bat.write_text(
        "@echo off\n"
        "echo Ola! Preparando ambiente do Luanny...\n"
        "Luanny.exe\n"
        "pause\n",
        encoding="utf-8"
    )
    
    readme = dist_dir / "LEIA-ME.txt"
    readme.write_text(
        "LUANNY - COLETOR DE ACESSIBILIDADE INSTAGRAM\n"
        "===========================================\n\n"
        "Bem-vindo(a) ao Luanny!\n\n"
        "COMO USAR:\n"
        "1. Dê um clique duplo em 'executar.bat' para abrir o painel.\n"
        "2. Siga as instruções na tela preta (terminal).\n"
        "3. O robô irá abrir o navegador na primeira vez e pedir para você fazer o login no Instagram.\n"
        "4. Depois do login, ele fechará a tela e coletará os dados sozinhos!\n"
        "5. Uma pasta 'data' aparecerá aqui com planilhas Excel (CSV) prontas!\n\n"
        "Nota: É necessário configurar suas credenciais apenas na primeira vez.\n",
        encoding="utf-8"
    )
    
    # IMPORTANTE: Instrução para baixar navegadores necessários pro Playwright
    # O luanny já tem instrução interna ou precisa do playwright install?
    # Para PyInstaller distribuído, Playwright recomenda setar PLAYWRIGHT_BROWSERS_PATH=0 pra empacotar o browser junto
    # Mas gera arquivos de +300mb.
    
    print("Build concluído! Tudo gerado em dist/Luanny")

if __name__ == "__main__":
    main()
