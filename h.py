import pickle


class Individuo:
    def __init__(self,nomep ,apelido ,altura ,naturalidade,estadocivil,pai,mae,pais,localidade):
        self.nomep=nomep
        self.apelido=apelido
        self.altura=altura
        self.naturalidade=naturalidade
        self.estadocivil=estadocivil
        self.pai = pai
        self.mae = mae
        self.pais = pais
        self.localidade = localidade





class Persistencia:
    def save(pessoa,dados):
        try:
            with open(pessoa +'.XML','wb') as seusdados:
                pickle.dump(dados,seusdados)
        except pickle.PickleError as err:
            print(str(err))

    def load(pessoa):
        try:
            with open(pessoa + '.XML', 'rb')as lerdados:
                return pickle.load(lerdados)
        except pickle.PickleError as err2:
            print(str(err2))

