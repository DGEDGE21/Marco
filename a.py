from h import Individuo
from h import Filiacao
from h import Morada

#21MAX.D@
individuo1I=Individuo('Anisio Maximiano','Djedje','1.85','Maputo','Solteiro')
individuo1F=Filiacao('Maximiano Ernesto Dgedge','Rosa Laurinda Manjate')
individuo1M=Morada('Mocambique','Maputo-Magaonine B(Q.25 Casa n78)')

#Marco
individuo2I=Individuo('Marco Maximiano','Dgedge','1,67','Maputo','Solteiro')
individuo2F=Filiacao('Maximiano Ernesto Dgedge','Rosa Laurinda Manjate')
individuo2M=Morada('Mocambique','Maputo-Magaonine B(Q.25 Casa n78)')

#MOTOR
a=str(input('\033[7;36;40mDigite o nome ou Apelido do individuo:\033[m '))
if a=='Anisio Maximiano':
      print('\033[36mNome Proprio:\033[m',individuo1I.nomep)
      print('\033[36mApelido:\033[m',individuo1I.apelido)
      print('\033[36mNaturalidade:\033[m',individuo1I.naturalidade)
      print('\033[36mEstado civil:\033[m',individuo1I.estadocivil)
      print('\033[36Nome do pai:\033[m',individuo1F.pai)
      print('\033[36mNome da mae:\033[m',individuo1F.mae)
      print('\033[36mMorada\Residencia:\033[m',individuo1M.pais, individuo1M.localidade)

#my python was bugging !
if a=='Djedje':
    print('\033[36mNome Proprio:\033[m', individuo1I.nomep)
    print('\033[36mApelido:\033[m', individuo1I.apelido)
    print('\033[36mNaturalidade:\033[m', individuo1I.naturalidade)
    print('\033[36mEstado civil:\033[m', individuo1I.estadocivil)
    print('\033[36Nome do pai:\033[m', individuo1F.pai)
    print('\033[36mNome da mae:\033[m', individuo1F.mae)
    print('\033[36mMorada\Residencia:\033[m', individuo1M.pais, individuo1M.localidade)

if a=='Marco Maximiano':
    print('\033[36mNome Proprio:\033[m',individuo2I.nomep)
    print('\033[36mApelido:\033[m',individuo2I.apelido)
    print('\033[36maltura:\033[m',individuo2I.altura)
    print('\033[36mNaturalidade:\033[m',individuo2I.naturalidade)
    print('\033[36mEstado civil:\033[m',individuo2I.estadocivil)
    print('\033[36mNome do pai:\033[m',individuo2F.pai)
    print('\033[mnome da mae:\033[m',individuo2F.mae)
    print('\033[mMorada\Residencia:\033[m',individuo2M.pais,individuo2M.localidade)

if a=='Dgedge':
    print('\033[36mNome Proprio:\033[m', individuo2I.nomep)
    print('\033[36mApelido:\033[m', individuo2I.apelido)
    print('\033[36maltura:\033[m', individuo2I.altura)
    print('\033[36mNaturalidade:\033[m', individuo2I.naturalidade)
    print('\033[36mEstado civil:\033[m', individuo2I.estadocivil)
    print('\033[36mNome do pai:\033[m', individuo2F.pai)
    print('\033[36mnome da mae:\033[m', individuo2F.mae)
    print('\033[36mMorada\Residencia:\033[m', individuo2M.pais, individuo2M.localidade)

