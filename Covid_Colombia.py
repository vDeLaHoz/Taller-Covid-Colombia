import pandas as pd
import matplotlib.pyplot as plt


# Obtener la data

url = 'Casos_positivos_de_COVID-19_en_Colombia.csv'
data = pd.read_csv(url)[:10000]

# Tratamiento de la data

data.drop('Código ISO del país', axis = 1, inplace=True)
data.drop('Fecha de muerte', axis = 1, inplace=True)
data.drop('Nombre del país', axis = 1, inplace=True)
data.drop('Pertenencia étnica', axis = 1, inplace=True)
data.drop('Nombre del grupo étnico', axis = 1, inplace=True)
data.drop('Fecha de inicio de síntomas', axis = 1, inplace=True)
data.drop('Unidad de medida de edad', axis = 1, inplace=True)
data.drop('Código DIVIPOLA departamento', axis = 1, inplace=True)
data.drop('Código DIVIPOLA municipio', axis = 1, inplace=True)
data.drop('ID de caso', axis = 1, inplace=True)


# 1.Número de casos de Contagiados en el País

casosContagiados = data.shape[0]
print(f'Número de casos de contagiados en el pais es: {casosContagiados}')


# 2.Número de Municipios Afectados

municipiosAfectados = data['Nombre municipio'].value_counts().count()
print(f'El número de municipios afectados es: {municipiosAfectados}')


# 3.Liste los municipios afectados (sin repetirlos)

municipiosAfectados_noRep = data['Nombre municipio'].value_counts()
print(f'Municipios afectados: {municipiosAfectados_noRep}')


# 4.Número de personas que se encuentran en atención en casa

data.loc[data['Ubicación del caso'] == 'casa'] = 'Leve'
data.loc[data['Ubicación del caso'] == 'CASA'] = 'Leve'
atencionEnCasa = data[data['Ubicación del caso'] == 'Casa'].shape[0]
print(f'El numero de personas con atención en casa es de: {atencionEnCasa}')


# 5.Número de personas que se encuentran recuperados

recuperados = data[data['Recuperado'] == 'Recuperado'].shape[0]
print(f'Personas recuperadas: {recuperados}')


# 6. Número de personas que ha fallecido

fallecidos = data[data['Estado'] == 'Fallecido'].shape[0]
print(f'El numero de fallecidos es: {fallecidos}')


# 7.Ordenar de Mayor a menor por tipo de caso (Importado, en estudio, Relacionado)

caso = data['Tipo de contagio' ].value_counts().head()
print(f'Tipo de caso:\n{caso}')


# 8.Número de departamentos afectados

departamentosAfectados = data['Nombre departamento'].value_counts().count()
print(f'Departamentos afectados: {departamentosAfectados}')


# 9.Liste los departamentos afectados(sin repetirlos)

departamentosAfectados_noRep = data['Nombre departamento'].value_counts()
print(f'Departamentos afectados: {departamentosAfectados_noRep}')


# 10.Ordene de mayor a menor por tipo de atención

atencion = data['Tipo de recuperación'].value_counts().head()
print('*'*50)
print(f'Tipo de atencion:\n{atencion}')