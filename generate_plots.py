
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style for premium aesthetics using standard matplotlib/seaborn
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("viridis")

# Configuration
DATA_PATH = r"f:\CURSOS 2025\ONE ALURA\DATA_SCIENCE_ONE\Challenge-TelecomX_ETL\Challenge-TelecomX-Alura-One-DS\TelecomX_Data_Cleaned.csv"
OUTPUT_DIR = "imgs"

# Ensure output directory exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def load_data(path):
    print(f"Loading data from {path}...")
    df = pd.read_csv(path)
    
    # Cleaning specifically for 'Charges.Total' which often has empty strings
    df['Charges.Total'] = pd.to_numeric(df['Charges.Total'], errors='coerce')
    
    # Drop rows with NaN in critical columns for general analysis if widely missing,
    # OR filter per plot. Let's do a general clean for the 'clean data' requirement
    # removing completely empty rows if any
    df.dropna(how='all', inplace=True)
    
    return df

def save_plot(fig, filename):
    path = os.path.join(OUTPUT_DIR, filename)
    print(f"Saving {filename}...")
    fig.savefig(path, dpi=300, bbox_inches='tight')
    plt.close(fig)

def plot_churn_distribution(df):
    """01_distribucion_churn.png"""
    # Clean NaNs in Churn
    data = df.dropna(subset=['Churn'])
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    counts = data['Churn'].value_counts()
    colors = ['#2E86C1', '#E74C3C'] # Blue for No, Red for Yes
    
    ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90, colors=colors,
           explode=(0, 0.1), shadow=True, textprops={'fontsize': 12, 'weight': 'bold'})
    ax.set_title('Distribución de Abandono (Churn)', fontsize=16, fontweight='bold', color='#34495E')
    
    save_plot(fig, '01_distribucion_churn.png')

def plot_demographics(df):
    """02_demograficos.png"""
    cols = ['gender', 'SeniorCitizen', 'Partner', 'Dependents']
    # Clean
    data = df.dropna(subset=cols + ['Churn'])
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    axes = axes.flatten()
    
    for i, col in enumerate(cols):
        # Calculate churn rate
        if col == 'SeniorCitizen':
            data[col] = data[col].replace({0: 'No', 1: 'Yes'})
            
        group_data = data.groupby(col)['Churn'].apply(lambda x: (x == 'Yes').mean() * 100).reset_index()
        
        sns.barplot(x=col, y='Churn', data=group_data, ax=axes[i], palette="viridis", hue=col, legend=False)
        axes[i].set_title(f'Tasa de Churn por {col}', fontsize=12, fontweight='bold')
        axes[i].set_ylabel('Churn Rate (%)')
        axes[i].set_xlabel('')
        axes[i].bar_label(axes[i].containers[0], fmt='%.1f%%')

    plt.suptitle('Análisis Demográfico', fontsize=20, fontweight='bold', y=1.02)
    save_plot(fig, '02_demograficos.png')

def plot_tenure(df):
    """03_analisis_permanencia.png"""
    # Clean
    data = df.dropna(subset=['tenure', 'Churn'])
    
    fig, axes = plt.subplots(1, 3, figsize=(20, 6))
    
    # 1. Boxplot
    sns.boxplot(data=data, x='Churn', y='tenure', palette=['#3498DB', '#E74C3C'], ax=axes[0], hue='Churn', legend=False)
    axes[0].set_title('Distribución de Permanencia por Churn', fontsize=12, fontweight='bold')
    
    # 2. KDE/Hist
    sns.histplot(data=data, x='tenure', hue='Churn', multiple="stack", palette=['#3498DB', '#E74C3C'], ax=axes[1])
    axes[1].set_title('Histograma de Permanencia', fontsize=12, fontweight='bold')
    
    # 3. Churn by Group
    # Create tenure group binning similar to notebook
    bins = [0, 12, 24, 36, 48, 60, 72]
    labels = ['0-12', '12-24', '24-36', '36-48', '48-60', '60+']
    data = data.copy() # Avoid SettingWithCopyWarning
    data['tenure_group'] = pd.cut(data['tenure'], bins=bins, labels=labels)
    
    churn_rate = data.groupby('tenure_group', observed=False)['Churn'].apply(lambda x: (x == 'Yes').mean() * 100).reset_index()
    
    sns.barplot(x='tenure_group', y='Churn', data=churn_rate, ax=axes[2], palette="Reds_d", hue='tenure_group', legend=False)
    axes[2].set_title('Tasa de Churn por Grupo de Permanencia', fontsize=12, fontweight='bold')
    axes[2].bar_label(axes[2].containers[0], fmt='%.1f%%')
    
    save_plot(fig, '03_analisis_permanencia.png')

def plot_services(df):
    """04_analisis_servicios.png"""
    services = ['PhoneService', 'MultipleLines', 'InternetService', 
                'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 
                'TechSupport', 'StreamingTV', 'StreamingMovies']
    
    # Clean NaNs in these columns
    data = df.dropna(subset=services + ['Churn'])
    
    fig, axes = plt.subplots(3, 3, figsize=(20, 18))
    axes = axes.flatten()
    
    for i, col in enumerate(services):
        churn_rate = data.groupby(col)['Churn'].apply(lambda x: (x == 'Yes').mean() * 100).reset_index()
        sns.barplot(x=col, y='Churn', data=churn_rate, ax=axes[i], palette="viridis", hue=col, legend=False)
        axes[i].set_title(f'Churn por {col}', fontsize=12, fontweight='bold')
        axes[i].set_ylim(0, 60) # Standardize scale
        axes[i].bar_label(axes[i].containers[0], fmt='%.1f%%')
        axes[i].set_xlabel('')
        axes[i].set_ylabel('Churn Rate (%)')

    plt.suptitle('Impacto de Servicios en el Churn', fontsize=22, fontweight='bold', y=1.02)
    save_plot(fig, '04_analisis_servicios.png')

def plot_contract_billing(df):
    """05_analisis_contratos.png"""
    cols = ['Contract', 'PaperlessBilling', 'PaymentMethod']
    data = df.dropna(subset=cols + ['Churn'])
    
    fig, axes = plt.subplots(1, 3, figsize=(22, 6))
    
    for i, col in enumerate(cols):
        churn_rate = data.groupby(col)['Churn'].apply(lambda x: (x == 'Yes').mean() * 100).reset_index()
        
        # Sort values for better visualization if needed, but categorical order is usually fine
        if col == 'Contract':
            order = ['Month-to-month', 'One year', 'Two year']
            sns.barplot(x=col, y='Churn', data=churn_rate, order=order, ax=axes[i], palette="magma", hue=col, legend=False)
        else:
            sns.barplot(x=col, y='Churn', data=churn_rate, ax=axes[i], palette="magma", hue=col, legend=False)
            if col == 'PaymentMethod':
                axes[i].tick_params(axis='x', rotation=45)
        
        axes[i].set_title(f'Churn por {col}', fontsize=12, fontweight='bold')
        axes[i].bar_label(axes[i].containers[0], fmt='%.1f%%')
    
    save_plot(fig, '05_analisis_contratos.png')

def plot_charges(df):
    """06_distribucion_cargos.png"""
    # Clean Charges
    data = df.dropna(subset=['Charges.Monthly', 'Charges.Total', 'Churn'])
    
    fig, axes = plt.subplots(1, 2, figsize=(18, 6))
    
    # Monthly Charges
    sns.kdeplot(data=data, x='Charges.Monthly', hue='Churn', fill=True, palette=['#3498DB', '#E74C3C'], ax=axes[0])
    axes[0].set_title('Distribución de Cargos Mensuales', fontsize=12, fontweight='bold')
    
    # Total Charges
    sns.kdeplot(data=data, x='Charges.Total', hue='Churn', fill=True, palette=['#3498DB', '#E74C3C'], ax=axes[1])
    axes[1].set_title('Distribución de Cargos Totales', fontsize=12, fontweight='bold')
    
    save_plot(fig, '06_distribucion_cargos.png')

def plot_correlation_matrix(df):
    """07_matriz_correlacion.png"""
    # Select numerical columns
    numerical_cols = ['SeniorCitizen', 'tenure', 'Charges.Monthly', 'Charges.Total']
    
    # Clean
    data = df.dropna(subset=numerical_cols).copy()
    
    # Ensure numeric types
    for col in numerical_cols:
        data[col] = pd.to_numeric(data[col], errors='coerce')
    
    # Drop rows that became NaN after coercion (e.g. if SeniorCitizen was 'Yes'/'No')
    data.dropna(subset=numerical_cols, inplace=True)

    # Compute correlation
    corr = data[numerical_cols].corr()
    
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, ax=ax)
    ax.set_title('Matriz de Correlación', fontsize=16, fontweight='bold')
    
    save_plot(fig, '07_matriz_correlacion.png')

if __name__ == "__main__":
    df = load_data(DATA_PATH)
    
    print("Generating 01_distribucion_churn.png...")
    plot_churn_distribution(df)
    
    print("Generating 02_demograficos.png...")
    plot_demographics(df)
    
    print("Generating 03_analisis_permanencia.png...")
    plot_tenure(df)
    
    print("Generating 04_analisis_servicios.png...")
    plot_services(df)
    
    print("Generating 05_analisis_contratos.png...")
    plot_contract_billing(df)
    
    print("Generating 06_distribucion_cargos.png...")
    plot_charges(df)

    print("Generating 07_matriz_correlacion.png...")
    plot_correlation_matrix(df)
    
    print("Visualization generation complete.")
