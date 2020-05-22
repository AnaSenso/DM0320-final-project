# Proyecto final - Ana Senso

## SHIVA: Sistema de validación y análisis de test de personalidad
![Image](https://github.com/AnaSenso/DM0320-final-project/blob/master/output/Image.png)

## Descripción del proyecto:
### Personalidad:
    - Que es
    - Test de personalidad
    - Validación de de test de personalidad

### Decripción del código:
**PERFORMING FACTORIAL ANALYSIS ...**
    - PHASE 1. Validate if factorial analysis can be performed ...
    - PHASE 2. Getting best number of factors ...
    - PHASE 3. Performing factorial analysis: to get item correlation with Dimensions..
    - PHASE 3.1. Creating item factorial dataframe  ...
    - PHASE 3.2. Adding information to info df dataframe...
    - PHASE 4. Analize dimensions: To get item correlation with all the Facets ...
    - PHASE 4.1. Get item correlation with all the Facets ....
        - Create a dataframe for each dimension ....
        - Perform factor analysis for each Dimension to get item correlation witn Factors ...
    - PHASE 4.2. Adding information to info df dataframe ...
    - PHASE 5. Exporting info dataframe as csv ...
**ANALYZING DATA ...**
    - Analyzing DIMENSION data ...
    - Analyzing ITEM data ...

## Recursos:
### Módulos de python, librerias y otras tecnologías:
- Limpieza y análisis básico de datos
    - [Pandas](https://pandas.pydata.org/pandas-docs/stable/index.html)
    - [Numpy](https://numpy.org/)
- Análisis de datos estadísticos
    - [SciPy stats](https://docs.scipy.org/doc/scipy/reference/stats.html)
    - [Statsmodels](https://www.statsmodels.org/stable/index.html)
    - [Pingouin](https://pingouin-stats.org/index.html)
    - [FactorAnalyzer](https://factor-analyzer.readthedocs.io/en/latest/factor_analyzer.html)
- Visualización de datos:
    - [Matplotlib](https://matplotlib.org/)
    - [Seaborn](https://seaborn.pydata.org/index.html)

### Base de datos:
- [Johnson's IPIP-NEO data repository](https://osf.io/wxvth/): Base de datos que almacena 300K respuestas al cuestionario NEO-PI. Este cuestionario de personalidad, que sigue el modelo de los cinco grandes (Big Five), es el más validado en la actualidad.

### Links de referencia:
- Howo to perform Factor analisis (Big Five): [link](https://www.datacamp.com/community/tutorials/introduction-factor-analysis)
[video](https://www.youtube.com/watch?v=ttBs_wfw_6U)

- Proyecto parecido [link](https://github.com/automoto/big-five-data)
- Caso de estudio: data analitics aplicado al modelo Big Five [link](https://www.sngular.com/es/data-analytics-big-five/)
- Baremación española del NEO-PI [link](http://scielo.isciii.es/scielo.php?script=sci_arttext&pid=S1130-52742009000200003)
- Estudio de validez convergente y estructural del NEO-PI [link](https://www.uv.es/seoane/boletin/previos/N92-1.pdf)
- Introducción a la psicología - Teoría clasica de respuest al item [link](http://aprendeenlinea.udea.edu.co/lms/investigacion/file.php/39/ARCHIVOS_2010/PDF/IntPsicometria_aristidesvara_1_.pdf)
