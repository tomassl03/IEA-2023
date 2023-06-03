# IEA 2023
# Exercicio 11 (Programa com adptação) - Aula 2
# 21 Fev 2023
# 107393 - Tomás Leite


from time import gmtime
from time import localtime


FILE_PATH = "Aula2_RegistoAlunosP.txt"
NUM_ALUNOS = 10

# Definir funções
def get_current_time():
    return '{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}'.format(*localtime()[:6])   #formatação da data e hora local (YYYY-MM-DD HH:mm:ss)

def escrever_no_ficheiro(nm, na):        #função para abrir ficheiro e escrever no próprio
    with open(FILE_PATH, "a") as f:
        current_time = get_current_time()
        f.write(f"Registo N : {nm} - {na} {current_time}\n")

def ler_do_ficheiro():
    with open(FILE_PATH, "r") as f:
        return f.read()

# Programa principal
def main():
    print("Criação do ficheiro Ok...")
    for i in range(NUM_ALUNOS):
        nm = input("Número mecanográfico: ")
        na = input("Nome do aluno: ")
        escrever_no_ficheiro(nm, na)    #chamar a função para escrever as variaveis nm e na

    print("Visualização do registo dos alunos...")
    print(ler_do_ficheiro())

if __name__ == "__main__":
    main()

print("Fim programa...")
