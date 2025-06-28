# Cargar librerías necesarias
import pandas as pd

# Cargar datasets
ruta_aire = '../datos/calidad_aire_colombia.csv'
ruta_agua = '../datos/calidad_agua_colombia.csv'

# Asiganr variables a cada dataset
df_aire = pd.read_csv(ruta_aire)
df_agua = pd.read_csv(ruta_agua)

# Información de los campos
df_aire.info()

# Información de los campos
df_agua.info()

print("Se han renombrado las columnas del dataframe aire")
df_aire.rename(columns={
    'ID Estacion': 'id_estacion',
    'Autoridad Ambiental': 'autoridad_ambiental',
    'Estación': 'estacion',
    'Latitud': 'latitud',
    'Longitud': 'longitud',
    'Variable': 'variable',
    'Unidades': 'unidades',
    'Tiempo de exposición (horas)': 'tiempo_exposicion',
    'Año': 'anio',
    'Promedio': 'promedio',
    'Suma': 'suma',
    'No. de datos': 'n_datos',
    'Representatividad Temporal': 'representatividad',
    'Excedencias limite actual': 'excedencias',
    'Porcentaje excedencias limite actual': 'porcentaje_excedencias',
    'Mediana': 'mediana',
    'Percentil 98': 'percentil_98',
    'Máximo': 'maximo',
    'Fechas/horas del máximo': 'fecha_maximo',
    'Mínimo': 'minimo',
    'Fechas/horas del mínimo': 'fecha_minimo',
    'Días de excedencias': 'dias_excedencias',
    'Código del Departamento': 'cod_departamento',
    'Nombre del Departamento': 'departamento',
    'Código del Municipio': 'cod_municipio',
    'Nombre del Municipio': 'municipio',
    'Tipo de Estación': 'tipo_estacion',
    'Ubicacion': 'ubicacion'
}, inplace=True)

print("Nombre de las columnas del df_aire")
df_aire.columns

print("Se han renombrado las columnas del dataframe agua")
df_agua.rename(columns={
    'DepartamentoCodigo': 'cod_departamento',
    'Departamento': 'departamento',
    'MunicipioCodigo': 'cod_municipio',
    'Municipio': 'municipio',
    'Año': 'anio',
    'IRCA': 'irca',
    'Nivel de riesgo': 'nivel_riesgo',
    'IRCAurbano': 'irc_urbano',
    'Nivel de riesgo urbano': 'nivel_riesgo_urbano',
    'IRCArural': 'irc_rural',
    'Nivel de riesgo rural': 'nivel_riesgo_rural'    
}, inplace=True)

print("Nombre de las columnas del df_agua")
df_agua.columns

print("Valores únicos de los años del df_aire")
df_aire['anio'].unique()

print("Valores únicos de los años del df_agua")
df_agua['anio'].unique()

print("Valores únicos de los departamentos del df_aire")
df_aire['departamento'].unique()

print("Diccionario de normalización del df_aire")
departamentos_normalizados = {
    'BOYACA': 'BOYACÁ',
    'QUINDIO': 'QUINDÍO',
    'ATLANTICO': 'ATLÁNTICO',
    'CORDOBA': 'CÓRDOBA',
    'VALLE DEL CAUCA': 'VALLE DEL CAUCA',
    'SANTANDER': 'SANTANDER',
    'NORTE DE SANTANDER': 'NORTE DE SANTANDER',
    'BOGOTA, D.C.': 'BOGOTÁ, D.C.',
    'BOGOTÁ, D.C.': 'BOGOTÁ, D.C.',
    'BOGOTÁ, D.C.': 'BOGOTÁ, D.C.',
    'RISARALDA': 'RISARALDA',
    'LA GUAJIRA': 'LA GUAJIRA',
    'CUNDINAMARCA': 'CUNDINAMARCA',
    'CAUCA': 'CAUCA',
    'MAGDALENA': 'MAGDALENA',
    'CALDAS': 'CALDAS',
    'CESAR': 'CESAR',
    'HUILA': 'HUILA',
    'TOLIMA': 'TOLIMA',
    'META': 'META',
    'ANTIOQUIA': 'ANTIOQUIA',
    'NARIÑO': 'NARIÑO',
    'CHOCÓ': 'CHOCÓ',
    'CHOCÓ': 'CHOCÓ',
    'BOLÍVAR': 'BOLÍVAR',
    'ARAUCA': 'ARAUCA',
    'CASANARE': 'CASANARE',
    'QUINDÍO': 'QUINDÍO',
    'BOYACÁ': 'BOYACÁ',
    'CÓRDOBA': 'CÓRDOBA',
    'ATLÁNTICO': 'ATLÁNTICO',
    'SANTANDER': 'SANTANDER',
    'LA GUAJIRA': 'LA GUAJIRA'
    # Las demás ya están bien o se corregirán automáticamente
}

print("Se ha Limpiado los espacios y pasamos a mayúsculas primero")
df_aire['departamento'] = df_aire['departamento'].str.strip().str.upper()

print("Se ha aplicado el diccionario de normalización")
df_aire['departamento'] = df_aire['departamento'].replace(departamentos_normalizados)

print("Valores únicos ordenados de los departamentos del df_aire")
print(sorted(df_aire['departamento'].unique()))

print("Valores únicos de los departamentos del df_aire")
df_agua['departamento'].unique()

print("Diccionario de normalización del df_agua")
departamentos_normalizados_df_agua = {
    'SUCRE': 'SUCRE',
    'TOLIMA': 'TOLIMA',
    'ANTIOQUIA': 'ANTIOQUIA',
    'ATLANTICO': 'ATLÁNTICO',
    'ATLÁNTICO': 'ATLÁNTICO',
    'BOGOTA, D.C.': 'BOGOTÁ, D.C.',
    'BOGOTÁ, D.C.': 'BOGOTÁ, D.C.',
    'BOLIVAR': 'BOLÍVAR',
    'BOLÍVAR': 'BOLÍVAR',
    'BOYACA': 'BOYACÁ',
    'BOYACÁ': 'BOYACÁ',
    'CUNDINAMARCA': 'CUNDINAMARCA',
    'CALDAS': 'CALDAS',
    'CAQUETA': 'CAQUETÁ',
    'CAQUETÁ': 'CAQUETÁ',
    'CAUCA': 'CAUCA',
    'CESAR': 'CESAR',
    'CORDOBA': 'CÓRDOBA',
    'CÓRDOBA': 'CÓRDOBA',
    'CHOCO': 'CHOCÓ',
    'CHOCÓ': 'CHOCÓ',
    'HUILA': 'HUILA',
    'LA GUAJIRA': 'LA GUAJIRA',
    'MAGDALENA': 'MAGDALENA',
    'META': 'META',
    'NARIÑO': 'NARIÑO',
    'NORTE DE SANTANDER': 'NORTE DE SANTANDER',
    'QUINDIO': 'QUINDÍO',
    'QUINDÍO': 'QUINDÍO',
    'RISARALDA': 'RISARALDA',
    'SANTANDER': 'SANTANDER',
    'VALLE DEL CAUCA': 'VALLE DEL CAUCA',
    'ARAUCA': 'ARAUCA',
    'CASANARE': 'CASANARE',
    'PUTUMAYO': 'PUTUMAYO',
    'ARCHIPIELAGO DE SAN ANDRES, PROVIDENCIA Y SANTA CATALINA': 'ARCHIPIÉLAGO DE SAN ANDRÉS, PROVIDENCIA Y SANTA CATALINA',
    'ARCHIPIÉLAGO DE SAN ANDRÉS, PROVIDENCIA Y SANTA CATALINA': 'ARCHIPIÉLAGO DE SAN ANDRÉS, PROVIDENCIA Y SANTA CATALINA',
    'AMAZONAS': 'AMAZONAS',
    'GUAINIA': 'GUAINÍA',
    'GUAINÍA': 'GUAINÍA',
    'GUAVIARE': 'GUAVIARE',
    'VAUPES': 'VAUPÉS',
    'VAUPÉS': 'VAUPÉS',
    'VICHADA': 'VICHADA'
}

print("Se ha Limpiado los espacios y pasamos a mayúsculas primero")
df_agua['departamento'] = df_agua['departamento'].str.strip().str.upper()

print("Se ha aplicado el diccionario de normalización")
df_agua['departamento'] = df_agua['departamento'].replace(departamentos_normalizados_df_agua)

print("Valores únicos ordenados de los departamentos del df_agua")
print(sorted(df_agua['departamento'].unique()))

print("Automatización para saber los valores únicos de cada columna en el df_agua\n")
for col in df_agua.columns:
    print(f"Columna: {col}")
    print(df_agua[col].unique())
    print("-" * 40)

df_agua['municipio'].unique()

print("Automatización para saber los valores únicos de cada columna en el df_aire\n")
for col in df_aire.columns:
    print(f"Columna: {col}")
    print(df_aire[col].unique())
    print("-" * 40)

#df_agua['municipio'].unique()

# cuántas veces aparece cada municipio
#df_agua['municipio'].value_counts()

# contar cuántos municipios hay
#df_agua['municipio'].nunique()

# Ver los municipios ordenadamente (como una lista legible)
# sorted(df_agua['municipio'].dropna().unique())

# Ver los municipios como un DataFrame para exportar o analizar
df_agua[['municipio']].drop_duplicates().sort_values('municipio')


print("Normalización básica (mayúsculas + strip)")
df_agua['municipio'] = df_agua['municipio'].str.strip().str.upper()

print("Detectar inconsistencias comunes")
municipios_unicos = sorted(df_agua['municipio'].unique())
for municipio in municipios_unicos:
    print(municipio)

# Función reutilizable para normalizar municipios
def normalizar_municipios(df, columna='municipio', correcciones=None):
    df[columna] = df[columna].str.strip().str.upper()
    if correcciones:
        df[columna] = df[columna].replace(correcciones)
    return df

correcciones_municipios_df_aire = {
    'AGUSTIN CODAZZI': 'AGUSTÍN CODAZZI',
    'AMAGA': 'AMAGÁ',
    'CHIRIGUANA': 'CHIRIGUANÁ',
    'ITAGUI': 'ITAGÜÍ',
    'JARDIN': 'JARDÍN',
    'IBAGUE': 'IBAGUÉ',
    'MEDELLIN': 'MEDELLÍN',
    'MONTELIBANO': 'MONTELÍBANO',
    'MONTERIA': 'MONTERÍA',  
    'NEMOCON': 'NEMOCÓN',
    'POPAYAN': 'POPAYÁN',
    'CARTAGENA DE INDIAS': 'CARTAGENA',
    'PUERTO BERRIO': 'PUERTO BERRÍO',
    'PUERTO LIBERTADOR': 'PUERTO LIBERTADOR',
    'SAN JOSE DE URE': 'SAN JOSÉ DE URÉ',
    'SAN JOSE DE LA MONTAÑA': 'SAN JOSÉ DE LA MONTAÑA',
    'SIBATE': 'SIBATÉ',
    'SONSON': 'SONSÓN',
    'SOPETRAN': 'SOPETRÁN',
    'SOPO': 'SOPÓ',
    'TOCANCIPA': 'TOCANCIPÁ',
    'TULUA': 'TULUÁ',
    'YONDO': 'YONDÓ',
    'ZIPAQUIRA': 'ZIPAQUIRÁ',
    'BOGOTA, D.C.': 'BOGOTÁ, D.C.',
    'CARTAGENA DE INDIAS': 'CARTAGENA',
    # Agrega más según encuentres
}

# Reutilizando función para normalizar municipio
df_aire = normalizar_municipios(df_aire, correcciones=correcciones_municipios_df_aire)

#df_aire['municipio'].unique()

# cuántas veces aparece cada municipio
#df_aire['municipio'].value_counts()

# contar cuántos municipios hay
#df_aire['municipio'].nunique()

# Ver los municipios ordenadamente (como una lista legible)
sorted(df_aire['municipio'].dropna().unique())

# Ver los municipios como un DataFrame para exportar o analizar
#df_aire[['municipio']].drop_duplicates().sort_values('municipio')


print("Valores únicos de los municipios del df_aire")
df_aire['municipio'].unique()

print("Mostrando las primeras filas del dataset df_aire:\n")
print(df_aire.head())

# Mostrar primeras filas del dataset df_agua
print("Mostrando las primeras filas del dataset df_agua:\n")
print(df_agua.head())

# Filtrar por departamentos deseados
print("Se han filtrado por departamentos deseados")
departamentos_interes = ['CÓRDOBA', 'CESAR', 'BOLÍVAR']

df_aire_filtrado = df_aire[df_aire['departamento'].isin(departamentos_interes)]
df_agua_filtrado = df_agua[df_agua['departamento'].isin(departamentos_interes)]

print("Verificación rápida")
print(f"Registros de aire filtrados: {df_aire_filtrado.shape[0]}")
print(f"Registros de agua filtrados: {df_agua_filtrado.shape[0]}")

print("Eliminando la palabra '#TODOS' del df_aire_filtrado")
df_aire_filtrado = df_aire_filtrado[~df_aire_filtrado.isin(['#TODOS']).any(axis=1)]

print("Eliminando la palabra '#TODOS' del df_agua_filtrado")
df_agua_filtrado = df_agua_filtrado[~df_agua_filtrado.isin(['#TODOS']).any(axis=1)]

print("Verificación rápida")
print(f"Registros de aire filtrados: {df_aire_filtrado.shape[0]}")
print(f"Registros de agua filtrados: {df_agua_filtrado.shape[0]}")

print("Archivos filtrados y guardados correctamente.")
df_aire_filtrado.to_csv('../datos/aire_filtrado_caribe.csv', index=False)
df_agua_filtrado.to_csv('../datos/agua_filtrada_caribe.csv', index=False)


