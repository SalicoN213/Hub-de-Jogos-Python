import os
import shutil
import sys
import subprocess

# Configurações do Executável
NOME_EXE = "HubDeJogos.exe"
ICONE_PATH = "icone.ico"
SCRIPT_PRINCIPAL = "main.py"


def limpar_antigos():
    """Remove o .exe anterior e pastas temporárias se existirem."""
    print("🧹 Limpando compilações anteriores...")

    if os.path.exists(NOME_EXE):
        try:
            os.remove(NOME_EXE)
            print(f"  - Removido {NOME_EXE} antigo da pasta raiz.")
        except Exception as e:
            print(f"  - Erro ao remover {NOME_EXE}: {e}")

    for pasta in ['build', 'dist']:
        if os.path.exists(pasta):
            shutil.rmtree(pasta, ignore_errors=True)
            print(f"  - Pasta '{pasta}' removida.")


def compilar():
    """Executa o PyInstaller usando o interpretador Python atual do ambiente."""
    print("\n🔨 Iniciando compilação com PyInstaller...")

    # sys.executable garante que usamos o ambiente correto (venv) com todas as bibliotecas instaladas
    comando = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        f"--name={NOME_EXE.replace('.exe', '')}",
        "--collect-all=pyfiglet",
        SCRIPT_PRINCIPAL
    ]

    if os.path.exists(ICONE_PATH):
        comando.append(f"--icon={ICONE_PATH}")
        print(f"  - Ícone '{ICONE_PATH}' encontrado e incluído.")
    else:
        print(f"  - ⚠️ AVISO: Ícone '{ICONE_PATH}' não encontrado. Compilando sem ícone.")

    resultado = subprocess.run(comando)

    if resultado.returncode == 0:
        print("\n✅ Compilação concluída com sucesso!")

        exe_gerado = os.path.join("dist", NOME_EXE)
        if os.path.exists(exe_gerado):
            shutil.move(exe_gerado, NOME_EXE)
            print(f"📦 Executável disponível em: {os.path.abspath(NOME_EXE)}")

        for pasta in ['build', 'dist']:
            if os.path.exists(pasta):
                shutil.rmtree(pasta, ignore_errors=True)

        spec_file = f"{NOME_EXE.replace('.exe', '')}.spec"
        if os.path.exists(spec_file):
            os.remove(spec_file)

    else:
        print("\n❌ Erro durante a compilação do projeto.")


if __name__ == "__main__":
    limpar_antigos()
    compilar()