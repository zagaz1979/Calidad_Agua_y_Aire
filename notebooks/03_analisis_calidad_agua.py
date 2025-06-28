# Importar librerías
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar estilo visual
sns.set_theme(style="whitegrid")

# Cargar dataset filtrado de calidad del agua
df_agua = pd.read_csv('../datos/agua_filtrada_caribe.csv')

df_agua.info()

df_agua.isnull().sum()

df_agua.nunique()

# Verificar columnas
print("Columnas disponibles:", df_agua.columns)
print("\n-------------------------------------------------------------------------------")
print(df_agua.head())

# Asegurarse de que IRCA esté presente
if 'irca' not in df_agua.columns:
    raise ValueError("La columna 'IRCA' no está en el dataset. Revisa el nombre exacto.")
else:
    print("La columna IRCA se encuentra en el dataset")
    
df_agua['irca'].unique()

df_agua['nivel_riesgo_rural'].unique()

df_agua['nivel_riesgo_urbano'].unique()

# Ver distribución de IRCA por año y departamento
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_agua, x='anio', y='irca', hue='departamento')
plt.title('Distribución del IRCA por Año y Departamento')
plt.ylabel('IRCA (%)')
plt.xticks(rotation=45)
plt.legend(title='Departamento')
plt.tight_layout()
plt.show()

# Evolución del IRCA promedio por departamento
df_irca_anual = df_agua.groupby(['anio', 'departamento'])['irca'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(data=df_irca_anual, x='anio', y='irca', hue='departamento', marker='o')
plt.title('Evolución Promedio del IRCA por Departamento (2007–2023)')
plt.ylabel('IRCA Promedio (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Clasificación de riesgo según IRCA
def clasificar_irca(valor):
    if valor <= 5:
        return 'Sin Riesgo'
    elif valor <= 14:
        return 'Riesgo Bajo'
    elif valor <= 35:
        return 'Riesgo Medio'
    elif valor <= 80:
        return 'Riesgo Alto'
    else:
        return 'Riesgo Invial'

df_agua['CLASIFICACION_IRCA'] = df_agua['irca'].apply(clasificar_irca)
df_agua.head()

# Conteo por clasificación
plt.figure(figsize=(10, 5))
sns.countplot(data=df_agua, x='CLASIFICACION_IRCA', order=['Sin Riesgo', 'Riesgo Bajo', 'Riesgo Medio', 'Riesgo Alto', 'Riesgo Invial'], hue='departamento')
plt.title('Clasificación del IRCA por Departamento')
plt.ylabel('Número de registros')
plt.tight_layout()
plt.show()

# IRCA promedio por municipio (top 10 peores)
df_municipios_irca = df_agua.groupby('municipio')['irca'].mean().reset_index()
df_municipios_irca = df_municipios_irca.sort_values(by='irca', ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(data=df_municipios_irca, x='irca', y='municipio', palette='Reds_r')
plt.title('Top 10 Municipios con Peor Calidad de Agua (IRCA Promedio)')
plt.xlabel('IRCA Promedio (%)')
plt.tight_layout()
plt.show()