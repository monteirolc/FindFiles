import encontra
print("A entrada deve ser conforme a seguir")
print("/home/algo/minhapasta/(para linux)")
find_path = input('Digite a pasta onde deseja escanear: ')
find_expression = input('Digite a expressão procurada: ')

encontra.find_files(find_path=find_path,
                    find_expression=find_expression, count=0)
