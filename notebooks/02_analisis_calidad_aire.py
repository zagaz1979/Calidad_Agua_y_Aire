# Importar librerías
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Estilo de visualización
sns.set_theme(style="whitegrid")

# Cargar datos filtrados
df_aire = pd.read_csv('../datos/aire_filtrado_caribe.csv')

# Inspección rápida
print("Columnas disponibles:", df_aire.columns)
print("\n-------------------------------------------------------------------------------")
print(df_aire.head())

df_aire['departamento'].unique()

# Convertir columna de año a entero (si es necesario)
df_aire['anio'] = df_aire['anio'].astype(int)

df_aire['variable'].unique()

# Contaminantes más comunes a analizar (ajusta si tienes otros)
contaminantes = ['PM10', 'O3', 'PST', 'P', 'PM2.5', 'TAire2', 'SO2', 'NO2', 'CO',
       'HAire2', 'DViento', 'RGlobal', 'VViento']

df_aire.isnull().sum()

df_aire.info()

df_aire['representatividad'].unique()

# Ver cuántos y cuáles son
df_aire[df_aire['representatividad'].isna()]

# Cantidad de datos nan en el campo representatividad
df_aire['representatividad'].isna().sum()

# Eliminar los registros con NaN en representatividad
#df_aire = df_aire.dropna(subset=['representatividad'])

# Imputar un valor promedio (si el porcentaje es importante)
#media_rep = df_aire['representatividad'].mean()
#df_aire['representatividad'] = df_aire['representatividad'].fillna(media_rep)

df_aire['variable'].unique()

df_aire['anio'].unique()

df_aire['promedio'].unique()

df_aire['promedio'].isna().sum()

# Evolución temporal de cada contaminante por departamento
for contaminante in contaminantes:
    if contaminante in df_aire['variable'].unique():
        plt.figure(figsize=(10, 5))
        sns.lineplot(
            data=df_aire[df_aire['variable'] == contaminante],
            x='anio',
            y='promedio',
            hue='departamento',
            marker='o'
        )
        plt.title(f'Evolución de {contaminante} (Promedio Anual)')
        plt.xlabel('Año')
        plt.ylabel(f'{contaminante} (µg/m³ o equivalente)')
        plt.legend(title='Departamento')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        print(f"Contaminante '{contaminante}' no encontrado en el dataset.")

# Transforma los datos para que cada contaminante sea una columna
df_pivot = df_aire.pivot_table(
    index=['departamento', 'anio'],
    columns='variable',
    values='promedio',
    aggfunc='mean'  # promedia si hay varias estaciones por depto-año
).reset_index()

# Calcular promedio general por departamento
df_promedios = df_pivot.groupby('departamento').mean(numeric_only=True).reset_index()

df_promedios

df_promedios.columns.name = None  # quita el nombre del índice de columnas

# Elimina 'Año' antes de promediar
df_promedios = df_pivot.drop(columns='anio').groupby('departamento').mean(numeric_only=True).reset_index()

df_promedios

df_barplot = df_promedios.melt(
    id_vars='departamento',
    var_name='Contaminante',
    value_name='Valor promedio'
)

plt.figure(figsize=(12, 6))
sns.barplot(
    data=df_barplot,
    x='Contaminante',
    y='Valor promedio',
    hue='departamento'
)
plt.title('Promedio anual de contaminantes por departamento')
plt.ylabel('µg/m³ o equivalente')
plt.xlabel('Contaminante')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df_barplot = (
    df_aire.groupby(['anio', 'variable', 'departamento'])['promedio']
    .mean()
    .reset_index()
    .rename(columns={'variable': 'Contaminante', 'promedio': 'Valor promedio'})
)

# Crear gráfico múltiple por año
g = sns.catplot(
    data=df_barplot,
    kind="bar",
    x="Contaminante",
    y="Valor promedio",
    hue="departamento",
    col="anio",               # Un gráfico por año
    col_wrap=1,               # Número de gráficos por fila
    height=5,
    aspect=1.5,
    palette="tab10"
)

g.set_titles("Año {col_name}")
g.set_axis_labels("Contaminante", "Promedio (µg/m³)")
g.set_xticklabels(rotation=45)
plt.tight_layout()
plt.show()

df_melt = df_promedios.melt(id_vars=['departamento'], var_name='variable', value_name='valor')
df_melt = df_melt.dropna(subset=['valor'])

df_promedios.columns

print(df_melt.shape)
df_melt.head()

plt.figure(figsize=(14, 6))
sns.barplot(
    data=df_melt,
    x='variable',
    y='valor',
    hue='departamento',
    palette='Set2'
)

plt.title('Promedio anual de contaminantes por departamento')
plt.xlabel('Contaminante')
plt.ylabel('Valor promedio (µg/m³ o equivalente)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

