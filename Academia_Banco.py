import sqlite3

bank = sqlite3.connect('data_base/Academy_data_base.db')

cursor = bank.cursor()


cursor.execute("CREATE TABLE alunos (Nome text,"
               "Idade integer,"
               "Email text,"
               "Telefone integer,"
               "Sexo text,"
               "CPF integer," 
               "Nascimento integer,"
               "Altura integer,"
               "Peso integer,"
               "Endereco text,"
               "Num_Casa integer,"
               "Tele_Extra integer,"
               "Mensalidade integer)")




cursor.execute("CREATE TABLE pagamentos (CPF integer,"
               "Valor integer,"
               "Data_Hora integer)")

#al = '08441655570'

#cursor.execute(f"SELECT * FROM  alunos WHERE cpf = {al}")

#print(cursor.fetchone())

bank.commit()