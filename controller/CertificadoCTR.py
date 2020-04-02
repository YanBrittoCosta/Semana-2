import sqlite3
import pandas as pd
import os


class CertificadoCTR:


    def __init__(self,PATH_NAME,banco_cert):

        self.PATH_NAME = PATH_NAME
        self.banco_cert = banco_cert

    def dicio(self):
        #varrendo todos os arquivos com extensao xlsxda pasta de registro
        todos_arquivos = list(filter(lambda x:'.xlsx' in x,os.listdir(self.PATH_NAME)))
        todos_dataset = []
        #varrendo os arquivos e inserindo no dicionario
        for arquivos in todos_arquivos:
            data = pd.read_excel(self.PATH_NAME + arquivos,sheet_name = None)
            todos_dataset.append(data)
            #todos_dataset = pd.Series(data).to_frame()
            #todos_dataset = pd.DataFrame([data])

        
        #print(todos_dataset.head())
        #conectando com o banco de dados
        con = sqlite3.connect(self.banco_cert +'.sqlite')

        #obtendo nome das tabelas xlsx
        nome_tabela = [os.path.splitext(i)[0] for i in todos_arquivos]
        print(nome_tabela)

        # pega a primeira linha de cada aba da tabela
        campos_tabela = []
        #print (todos_dataset.head(0))
        
        for i in range (0,len(nome_tabela)):
            nome_das_colunas = pd.DataFrame([todos_dataset[i]]).head(0)
            campos_tabela.append(nome_das_colunas)

        #criando as tabelas no banco de dados
        print('campos das tabelas')
        print(campos_tabela)
        print("nome das colunas\n")
        print(nome_das_colunas)
        '''
        cur = con.cursor()
        for b in range(0,len(nome_tabela)):
            cur.execute('DROP TABLE IF EXISTS '+nome_tabela[b])

        for j in range(0,len(nome_tabela)):
            cur.execute("""CREATE TABLE IF NOT EXISTS """+nome_tabela[j]+"""("""+','.join(campos_tabela[j])+""")""")

        
        #todos_dataset2.to_csv('controller/teste1.csv', encoding='utf-8', index=False)
        #varrendo todas as tabelas e para cada é realizado a inserção dos dados
        for index in range(0,len(nome_tabela)):
            query = """INSERT INTO """+str(nome_tabela[index])+"""("""+','.join(campos_tabela[index])+""")VALUES("""+','.join(map(str,'?'*len(pd.DataFrame([todos_dataset[index]]).columns)))+""")"""
            todos_dataset[index] = pd.DataFrame([todos_dataset[index]]).astype(str)

            #print(todos_dataset)
            #
            for k in range(0,len(todos_dataset[index])):
                
                inserir_registro = tuple(todos_dataset[index].iloc[k])
                cur.execute(query,inserir_registro)
                con.commit()
        '''