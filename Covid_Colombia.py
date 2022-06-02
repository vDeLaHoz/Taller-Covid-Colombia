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


# 11.Liste de mayor a menor los 10 departamentos con mas casos de contagiados

mas_casos_dpto = data['Nombre departamento' ].value_counts().head(10)
print(f'Los 10 departamentos con mas casos de contagiados son:\n{mas_casos_dpto}')


# 12.Liste de mayor a menor los 10 departamentos con mas casos de fallecidos

aux = data[data['Estado'] == 'Fallecido'].groupby('Nombre departamento')
fallecidos_dpto = aux.size().sort_values(ascending=False).head(10)
print(f'Los 10 departamentos con más casos de fallecidos son:\n{fallecidos_dpto}')


# 13.Liste de mayor a menor los 10 departamentos con mas casos de recuperados

aux = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento')
recuperados_dpto = aux.size().sort_values(ascending=False).head(10)
print(f'Los 10 departamentos con más casos de recuperados son:\n{recuperados_dpto}')


# 14.Liste de mayor a menor los 10 municipios con mas casos de contagiados

casos_municipios = data['Nombre municipio' ].value_counts().head(10)
print(f'Los 10 municipios con mas casos de contagiados son:\n{casos_municipios}')


# 15.Liste de mayor a menor los 10 municipios con mas casos de fallecidos

aux = data[data['Estado'] == 'Fallecido'].groupby('Nombre municipio')
fallecidos_municipios = aux.size().sort_values(ascending=False).head(10)
print(f'Los 10 municipios con más casos de fallecidos son:\n{fallecidos_municipios}')


# 16.Liste de mayor a menor los 10 municipios con mas casos de recuperados

aux = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio')
recuperados_municipios = aux.size().sort_values(ascending=False).head(10)
print(f'Los 10 municipios con más casos de recuperados son:\n{recuperados_municipios}')


# 17.Liste agrupado por departamento y en orden de Mayor a menor las ciudades con mas casos de contagiados

contagios_ciudad_dpto = data.groupby(['Nombre departamento', 'Nombre municipio']).size().sort_values(ascending=False)
print(f'Departamentos y sus ciudades con mas casos de contagios:\n{contagios_ciudad_dpto}')

# 18.Número de Mujeres y hombres contagiados por ciudad por departamento

hombres_mujeres_contagiados = data.groupby(['Sexo', 'Nombre municipio', 'Nombre departamento']).size().sort_values(ascending=False)
print(f'Número de Mujeres y hombres contagiados por ciudad por departamento:\n{hombres_mujeres_contagiados}')


# 19.Liste el promedio de edad de contagiados por hombre y mujeres por ciudad por departamento

promedio = data.groupby( ['Sexo', 'Nombre municipio', 'Nombre departamento']).Edad.mean()
print(f'Promedio de edad de contagiados por hombre y mujeres por ciudad por departamento: \n{promedio}')


# 20.Liste de mayor a menor el número de contagiados por departamento de procedencia

procedencia_dpto = data['Nombre departamento'].value_counts()
print(f'Número de contagiados por departamento de procedencia: \n{procedencia_dpto}')


# 21.Liste de mayor a menor las fechas donde se presentaron mas contagios

fechas_contagios = data['Fecha de diagnóstico' ].value_counts().sort_values(ascending=False)
print(f'Fechas donde se presentaron mas contagios:\n{fechas_contagios}')


# 22.Diga cual es la tasa de mortalidad y recuperación que tiene toda Colombia

muertes = data[data['Estado'] == 'Fallecido'].shape[0]
recuperados = data[data['Recuperado'] == 'Recuperado'].shape[0]

mortalidad = muertes / casosContagiados * 100
tasa_recuperacion = recuperados / casosContagiados * 100

print(f'Tasa de mortalidad en Colombia: {mortalidad}')
print(f'Tasa de recuperacion en Colombia: {tasa_recuperacion}')


# 23. Liste la tasa de mortalidad y recuperación que tiene cada departamento

muertes_depto = data[data['Estado'] == 'Fallecido'].groupby('Nombre departamento').size()
mortalidad_dpto = muertes_depto /  casosContagiados * 100
print(f'Tasa de mortalidad de cada departamento:\n{mortalidad_dpto}')

recuperacion_depto = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size()
tasa_recuperacion_dpto = recuperacion_depto /  casosContagiados * 100
print(f'Tasa de recuperacion de cada departamento:\n{tasa_recuperacion_dpto}')


# 24.Liste la tasa de mortalidad y recuperación que tiene cada ciudad

muertes_municipio = data[data['Estado'] == 'Fallecido'].groupby('Nombre municipio').size()
mortalidad_municipio = muertes_municipio /  casosContagiados * 100
print(f'Tasa de mortalidad de cada municipio:\n{mortalidad_municipio}')

recuperacion_municipio = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size()
tasa_recuperacion_munic = recuperacion_municipio /  casosContagiados * 100
print(f'Tasa de recuperacion de cada municipio:\n{tasa_recuperacion_munic}')


# 25.Liste por cada ciudad la cantidad de personas por atención

atencion = data.groupby(['Nombre municipio', 'Ubicación del caso']).size()
print(f'Cantidad de personas por atención:\n{atencion}')


# 26.Liste el promedio de edad por sexo por cada ciudad de contagiados

promedio_edad = data.groupby(['Sexo', 'Nombre municipio']).Edad.mean()
print(f'Promedio de edad por sexo por cada ciudad de contagiados:\n{promedio_edad}')


# 27. Grafique las curvas de contagio, muerte y recuperación de toda Colombia acumulados

data.loc[data['Sexo'] == 'm'] = 'M'
data.loc[data['Sexo'] == 'f'] = 'F'
data.loc[data['Estado'] == 'leve'] = 'Leve'
data.loc[data['Estado'] == 'LEVE'] = 'Leve'

contagios = data.groupby('Fecha de diagnóstico').size().sort_values().plot(figsize=(15, 4))
plt.show(contagios)
print('\n Curva de Contagios')


fallecidos = data[data['Estado'] == 'Fallecido'].groupby('Fecha de diagnóstico').size().sort_values().plot(figsize=(15, 4))
plt.show(fallecidos)
print('\n Curva de Fallecidos')

recuperados = data[data['Recuperado'] == 'Recuperado'].groupby('Fecha de diagnóstico').size().sort_values().plot(figsize=(15, 4))
plt.show(recuperados)
print('\n Curva de Recuperados')


# 28.Grafique las curvas de contagio, muerte y recuperación de los 10 departamentos con mas casos de contagiados acumulados

contagios_dpto = data.groupby('Nombre departamento').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
plt.show(contagios_dpto)
print('\n Curva de los 10 departamentos con mas casos de contagiados')


fallecidos_dpto = data[data['Estado'] == 'Fallecido'].groupby('Nombre departamento').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
plt.show(fallecidos_dpto)
print('\n Curva de los 10 departamentos con mas casos de fallecidos')


recuperados_dpto = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
plt.show(recuperados_dpto)
print('\n Curva de los 10 departamentos con mas casos de recuperados')


# 29.Grafique las curvas de contagio, muerte y recuperación de las 10 ciudades con mas casos de contagiados acumulados

contagios_municipio = data.groupby('Nombre municipio').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
plt.show(contagios_municipio)
print('\n Curva de los 10 municipios con mas casos de contagiados')


fallecidos_municipio = data[data['Estado'] == 'Fallecido'].groupby('Nombre municipio').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
plt.show(fallecidos_municipio)
print('\n Curva de los 10 municipios con mas casos de fallecidos')


recuperados_municipio = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
plt.show(recuperados_municipio)
print('\n Curva de los 10 municipios con mas casos de recuperados')


# 30.Liste de mayor a menor la cantidad de fallecidos por edad en toda Colombia.

fallecidos = data[data['Estado'] == 'Fallecido'].groupby('Edad').size().sort_values(ascending = False)
print(f'Cantidad de fallecidos por edad en toda Colombia:\n{fallecidos}')


# 31.Liste el porcentaje de personas por atención de toda Colombia

porcentaje= ((data.groupby('Ubicación del caso').size().sort_values(ascending = False)) / ((data.groupby('Ubicación del caso').size().sort_values(ascending = False)).sum())) * 100
print(f'Porcentaje de personas por atención de toda Colombia\n {porcentaje}')


# 32.Haga un gráfico de barras por atención de toda Colombia

data.groupby(['Ubicación del caso']).size().sort_values(ascending = False).plot(kind='bar')
plt.ylabel('Cantidad de personas')
print('\n Gráfico de barras por atención de toda Colombia')


# 33.Haga un gráfico de barras por Sexo de toda Colombia

data.groupby(['Sexo']).size().sort_values(ascending = False).plot(kind='bar')
print('\n Grafico de barras por sexo de toda Colombia')


# 34.Haga un gráfico de barras por tipo de toda Colombia

data.groupby(['Tipo de contagio']).size().sort_values(ascending = False).plot(kind='bar')
print('\n Grafico de barras por tipo de contagio de toda Colombia')


# 35. Haga un gráfico de barras del número de contagiados, recuperados y fallecidos por fecha de toda Colombia

data.groupby('Fecha de diagnóstico').size().plot(kind = 'bar')
Fallecidos = data[data['Ubicación del caso'] == 'Fallecido']
Fallecidos.groupby('Fecha de diagnóstico').size().plot(kind = 'bar')
Recuperado = data[data['Recuperado'] == 'Recuperado']
Recuperado.groupby('Fecha de diagnóstico').size().plot(kind = 'bar')
plt.legend(["Recuperados", "Fallecidos", "Contagiados"])
print('\n Grafico de barras del número de contagiados, recuperados y fallecidos por fecha de toda Colombia')