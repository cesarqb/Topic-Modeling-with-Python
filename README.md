# TOPIC MODELING CON PYTHON

Este proyecto implementa un flujo completo de **procesamiento de lenguaje natural (NLP)** para analizar comentarios de redes sociales mediante técnicas de **modelado de tópicos (Topic Modeling)**.

El objetivo es **identificar los principales temas presentes en los comentarios de usuarios** utilizando técnicas de limpieza de texto, análisis exploratorio y modelos probabilísticos como **LDA (Latent Dirichlet Allocation)**.

---

## Objetivos del proyecto

* Analizar comentarios de usuarios provenientes de redes sociales.
* Aplicar técnicas de **preprocesamiento de textos**.
* Generar **análisis exploratorio de textos** mediante visualizaciones.
* Detectar **similitud entre comentarios**.
* Identificar **tópicos latentes** utilizando modelos de **Topic Modeling (LDA)**.

---

## Técnicas utilizadas

Durante el proyecto se aplican diferentes técnicas de **Procesamiento de Lenguaje Natural (NLP)**:

* Limpieza y normalización de texto
* Tokenización
* Eliminación de *stopwords*
* Análisis exploratorio de textos
* Análisis gráfico de textos
* Análisis de **similitud entre comentarios**
* Modelado de tópicos con **Latent Dirichlet Allocation (LDA)**

---

## Tecnologías utilizadas

* Python: NLTK, Gensim, Scikit-learn, Matplotlib, WordCloud

---

## Estructura del proyecto

```
Topic-Modeling-with-Python
│
├── README.md
├── requirements.txt
│
├── data
│   ├── raw
│   │   └── BanamexFace.csv
│   │
│   └── processed
│       └── BanamexFace_clean.csv
│
├── notebooks
│   └── topic_modeling_analysis.ipynb
│
├── src
│   ├── text_preprocessing.py
│   ├── lda_model.py
│   └── similarity_analysis.py
│
├── images
│   └── wordcloud.png
│
└── results
    └── topics_output.csv
```

**Descripción de carpetas**

* `data/` → contiene los datos originales y datos procesados.
* `notebooks/` → análisis exploratorio y desarrollo del modelo.
* `src/` → scripts reutilizables de procesamiento y modelado.
* `images/` → visualizaciones generadas (ej. nube de palabras).
* `results/` → resultados del análisis de tópicos.

---

## Flujo del análisis

El análisis sigue las siguientes etapas:

1. **Carga de datos**
2. **Limpieza y preprocesamiento de texto**
3. **Análisis exploratorio del corpus**
4. **Visualización de palabras frecuentes**
5. **Cálculo de similitud entre comentarios**
6. **Entrenamiento de modelo LDA**
7. **Identificación de tópicos principales**

---

## Ejemplo de resultados

El modelo permite identificar diferentes temas presentes en los comentarios de usuarios, agrupando palabras que suelen aparecer juntas dentro de un mismo tópico.

Ejemplo de salida del modelo LDA:

```
Topic 1: banco, servicio, cliente, atención  
Topic 2: tarjeta, pago, crédito, cuenta  
Topic 3: aplicación, móvil, acceso, problema
```

---

## Posibles mejoras futuras

* Implementar **visualización interactiva de tópicos (pyLDAvis)**
* Evaluación automática del número óptimo de tópicos
* Integración de **embeddings de palabras**
* Implementación de modelos más recientes como **BERTopic**

---

## 👨‍🏫 Autor
César Quezada  
Científico de Datos | Docente Universitario | Mentor

---
