# 📊 Challenge TelecomX - ETL y Análisis Exploratorio de Datos

## 🎯 Descripción del Proyecto

Este proyecto forma parte del Challenge de Data Science de Alura, enfocado en el análisis de datos de clientes de **TelecomX** para identificar patrones de **churn** (evasión de clientes) y proporcionar insights estratégicos para reducir la pérdida de clientes.

## 🚀 Objetivo

Recopilar, procesar y analizar datos de clientes utilizando Python y sus principales bibliotecas para:

- ✅ Extraer información desde una API JSON
- ✅ Aplicar conceptos de ETL (Extracción, Transformación y Carga)
- ✅ Crear visualizaciones estratégicas
- ✅ Realizar Análisis Exploratorio de Datos (EDA)
- ✅ Generar insights y recomendaciones accionables

## 📁 Estructura del Proyecto

```
Challenge-TelecomX-Alura-One-DS/
│
├── TelecomX_ETL.ipynb          # Notebook principal con ETL y EDA
├── TelecomX_Data_Cleaned.csv   # Datos limpios (generado tras ejecutar)
└── README.md                    # Este archivo
```

## 🛠️ Tecnologías Utilizadas

- **Python 3.13+**
- **pandas** - Manipulación de datos
- **numpy** - Operaciones numéricas
- **matplotlib** - Visualizaciones
- **seaborn** - Visualizaciones estadísticas
- **requests** - Consumo de API

## 📦 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/LenninTemoche/Challenge-TelecomX-Alura-One-DS.git
cd Challenge-TelecomX-Alura-One-DS
```

### 2. Instalar dependencias

```bash
pip install pandas numpy matplotlib seaborn requests
```

### 3. Abrir el notebook

```bash
jupyter notebook TelecomX_ETL.ipynb
```

## 📊 Contenido del Análisis

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
- Exportación a CSV para uso futuro

### 4. **Análisis Exploratorio (EDA)**

- Análisis de churn general
- Análisis demográfico
- Análisis de permanencia (tenure)
- Análisis de servicios
- Análisis de contratos y facturación
- Análisis de cargos
- Matriz de correlación

### 5. **Insights y Recomendaciones**

- Identificación de factores de riesgo
- Estrategias de retención
- Recomendaciones accionables

## 🔍 Principales Hallazgos

### 🎯 Factores Clave de Churn

1. **Permanencia (Tenure)**
   - Clientes nuevos (0-12 meses): **MAYOR RIESGO**
   - Clientes de largo plazo (>24 meses): Significativamente más leales

2. **Tipo de Contrato**
   - Month-to-month: **ALTÍSIMA tasa de churn**
   - Contratos de 1-2 años: Tasas significativamente menores

3. **Servicios Adicionales**
   - OnlineSecurity, OnlineBackup, TechSupport: **Protegen contra churn**
   - Clientes sin estos servicios: Mayor probabilidad de abandono

4. **Método de Pago**
   - Electronic check: Mayor churn
   - Pagos automáticos: **Mejor retención**

## 💡 Recomendaciones Estratégicas

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

## 📈 Próximos Pasos

- [ ] Desarrollar modelo predictivo de churn (Machine Learning)
- [ ] Implementar sistema de alertas en tiempo real
- [ ] Crear dashboard de monitoreo de KPIs
- [ ] Realizar A/B testing de estrategias de retención
- [ ] Análisis de cohortes por periodo de adquisición

## 👨‍💻 Autor

**Lennin Temoche**

- GitHub: [@LenninTemoche](https://github.com/LenninTemoche)
- Proyecto: Challenge Alura ONE - Data Science

## 📄 Licencia

Este proyecto es parte del programa educativo de Alura LATAM y Oracle Next Education (ONE).

---

⭐ **Si este proyecto te fue útil, no olvides darle una estrella en GitHub!**
