# Challenge TelecomX - ETL y Análisis Exploratorio de Datos

## Descripción del Proyecto

Este proyecto forma parte del Challenge de Data Science de Alura, enfocado en el análisis de datos de clientes de **TelecomX** para identificar patrones de **churn** (evasión de clientes) y proporcionar insights estratégicos para reducir la pérdida de clientes.

## Objetivo

Recopilar, procesar y analizar datos de clientes utilizando Python y sus principales bibliotecas para:

- ✅ Extraer información desde una API JSON
- ✅ Aplicar conceptos de ETL (Extracción, Transformación y Carga)
- ✅ Crear visualizaciones estratégicas
- ✅ Realizar Análisis Exploratorio de Datos (EDA)
- ✅ Generar insights y recomendaciones accionables

## Estructura del Proyecto

```
Challenge-TelecomX-Alura-One-DS/
│
├── /imgs                       # Imágenes del proyecto
├── TelecomX_ETL.ipynb          # Notebook principal con ETL y EDA
├── TelecomX_Data_Cleaned.csv   # Datos limpios (generado tras ejecutar)
└── README.md                   # Descripción del proyecto
```

## Tecnologías Utilizadas

- **Python 3.13+**
- **pandas** - Manipulación de datos
- **numpy** - Operaciones numéricas
- **matplotlib** - Visualizaciones
- **seaborn** - Visualizaciones estadísticas
- **requests** - Consumo de API

## Contenido del Análisis

### 1. **Extracción de Datos (E)**

- Conexión a API JSON de TelecomX
- Obtención de datos de clientes en formato anidado

### 2. **Transformación (T)**

- Desanidación de datos JSON
- Limpieza y preparación de datos
- Conversión de tipos de datos
- Manejo de valores nulos

### 3. **Carga (L)**

- Consolidación en DataFrame estructurado
- Exportación a CSV para uso## 📊 Resultados Clave del Análisis

El análisis exploratorio de datos (EDA) reveló una tasa de rotación (churn) global del **25.72%**. Al profundizar en los segmentos, identificamos factores críticos de riesgo:

- **Demografía:**
  - **Adultos Mayores:** Presentan un riesgo significativamente mayor, con un **40.27%** de churn frente al 22.89% de los no mayores.
  - **Dependientes y Parejas:** Clientes _sin_ pareja (32.01%) o _sin_ dependientes (30.34%) tienen tasas de abandono mucho más altas que aquellos con lazos familiares.

- **Contratos y Facturación:**
  - **Tipo de Contrato:** El contrato **mensual (Month-to-month)** es el predictor más fuerte de abandono, con una tasa alarmante del **41.32%**, comparado con solo el 2.75% en contratos de dos años.
  - **Método de Pago:** El uso de **Cheque Electrónico** está asociado con un churn del **43.80%**, mientras que los métodos automáticos (tarjeta de crédito/transferencia) rondan el 15-16%.
  - **Facturación:** Los usuarios con facturación electrónica (Paperless) abandonan más (32.48%) que los que reciben factura física (15.87%).

- **Antigüedad (Tenure):**
  - Existe una correlación directa entre antigüedad y retención. Los clientes que abandonaron tenían en promedio **18 meses** de antigüedad, mientras que los clientes retenidos promedian **37.5 meses**. El primer año es el periodo más crítico.

![Distribución de Churn](imgs/01_distribucion_churn.png)
_Figura 1: Distribución global de Churn mostrando la tasa de abandono del 25.7% (Imbalanced Dataset)._

![Análisis de Permanencia](imgs/03_analisis_permanencia.png)
_Figura 2: Distribución de permanencia. Se observa que el churn se concentra en los primeros meses de servicio._

![Análisis de Contratos](imgs/05_analisis_contratos.png)
_Figura 3: Impacto del tipo de contrato en la retención. Los contratos a largo plazo reducen drásticamente el riesgo._

![Análisis de Servicios](imgs/04_analisis_servicios.png)
_Figura 4: Relación entre la tenencia de servicios adicionales y la tasa de cancelación._

![Matriz de Correlación](imgs/07_matriz_correlacion.png)
_Figura 5: Matriz de correlación mostrando las relaciones entre variables numéricas._

## 🛠️ Desafíos y Soluciones de Datos

Durante el proceso ETL, se abordaron varios desafíos técnicos para asegurar la calidad del dataset final:

- **Estructura JSON Anidada:** Los datos originales provenían de una API con estructura anidada (e.g., `Customer`, `Account`, `Subscription`). Se implementó una función de normalización para aplanar estas jerarquías en un DataFrame tabular y manejable.
- **Inconsistencias en Cargos:** La columna `Charges.Total` contenía valores vacíos (" ") para clientes nuevos con antigüedad cero. Estos se identificaron y se imputaron correctamente (o se ajustaron a 0 según la lógica de negocio) para permitir operaciones numéricas.
- **Normalización de Texto:** Se estandarizaron valores categóricos (ej. variaciones de "No internet service") para evitar duplicidad de categorías en el análisis.
- **Tipado de Datos:** Conversión explícita de variables numéricas y categóricas para optimizar el uso de memoria y facilitar el modelado posterior.

## 🚀 Recomendaciones Estratégicas

Basado en los hallazgos, se recomiendan las siguientes acciones para mitigar el churn:

### 1. Programa de Retención para Clientes Nuevos

- Onboarding robusto en primeros 3-6 meses
- Seguimiento proactivo mensual
- Descuentos introductorios

### 2. Incentivos para Contratos de Largo Plazo

- Descuentos por contrato anual (10-15%)
- Servicios premium incluidos
- Garantía de precio fijo

### 3. Promoción de Servicios de Valor Agregado

- Bundling de servicios de seguridad y soporte
- Pruebas gratuitas de 30-60 días
- Demostraciones del valor

### 4. Optimización de Métodos de Pago

- Incentivar pagos automáticos (descuento 2-5%)
- Simplificar configuración
- Reducir uso de electronic check

### 5. Segmentación y Personalización

- Ofertas personalizadas por segmento de riesgo
- Intervención proactiva antes del churn
- Foco en adultos mayores y clientes nuevos

## Próximos Pasos

**Modelado Predictivo de Churn**

- Construcción de un modelo de Machine Learning para predecir la probabilidad de cancelación.
- Evaluación con métricas como Accuracy, Precision, Recall y ROC-AUC.
- Identificación de variables más influyentes en la predicción.

**Exportación de Datos**

Al finalizar el proceso de limpieza y transformación, se generan los siguientes archivos listos para su uso:

- **`TelecomX_Data_Cleaned.csv`**: Dataset principal en formato CSV. Contiene los datos limpios, desanidados y estructurados, ideal para análisis rápidos, importación en herramientas de BI o modelado.
- **`TelecomX_Data_Cleaned.json`**: Versión en formato JSON del dataset limpio, preservando la estructura de datos si fuera necesario para otras aplicaciones.

Estos archivos se encuentran en la raíz del proyecto y son el resultado final del pipeline ETL documentado en `TelecomX_ETL.ipynb`.

**Autor**

**Lennin Billey Temoche Gómez**

- GitHub: [@LenninTemoche](https://github.com/LenninTemoche)
- Proyecto: Challenge TelecomX - Data Science - Alura ONE

## Licencia

Este proyecto es parte del programa educativo de Alura LATAM y Oracle Next Education (ONE).
