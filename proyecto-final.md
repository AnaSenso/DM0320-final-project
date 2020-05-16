# Proyecto final - Ana Senso

## Titulo: Sistema de validación y análisis de test de personalidad

## Descripción del proyecto:
La personalidad es un constructo que da unidad a todas las manifestaciones psicológicas del ser humano. La evaluación de personalidad perimte evaluar rasgos definitorios de un sujeto y, en cierta manera, predecir el comprtamiento del mismo en diferentes situaciones. 

Los test de personalidad son una de las herramientas más utilizadas en recursos humanos. La creación de dicho test debe ser realizada por un experto en personalidad, mientras que la validación del mismo es llevada a cabo por un analista de datos. 

- **Nivel 1** : Crear una herramienta de vlaidación de test de personalidad y evaluar la validez y relevacia de los items del cuestionario. Asigna un peso relativo a cada item y devuelve un análisis de parsonalidad básico (centiles por cada faceta y dimensión).

- **Nivel 2**: La herramienta debe reevaluar la validez de los items a medida que aumenta la muestra de sujetos. Avisa al creador del test cada vez que la validez de un item cambia o se vuelve irrelevante.

- **Nivel 3**: Proporciona informes de análisis de personalidad por grupos o sujetos a través de una api.

- **Nivel 4**: Hace recomendaciones de ofertas de empleo al sujeto en base a su personalidad.

## Recursos:
### Módulos de python, librerias y otras tecnologías:
- Limpieza y análisis básico de datos
    - [Pandas](https://pandas.pydata.org/pandas-docs/stable/index.html)
    - [Numpy](https://numpy.org/)
- Análisis de datos estadísticos
    - [SciPy stats](https://docs.scipy.org/doc/scipy/reference/stats.html)
    - [Statsmodels](https://www.statsmodels.org/stable/index.html)
    - [Pingouin](https://pingouin-stats.org/index.html)
- Visualización de datos:
    - [Matplotlib](https://matplotlib.org/)
    - [Seaborn](https://seaborn.pydata.org/index.html)

### Base de datos:
- [Johnson's IPIP-NEO data repository](https://osf.io/wxvth/): Base de datos que almacena 300K respuestas al cuestionario NEO-PI. Este cuestionario de personalidad, que sigue el modelo de los cinco grandes (Big Five), es el más validado en la actualidad.

### Links de referencia:
- Proyecto parecido [link](https://github.com/automoto/big-five-data)
- Caso de estudio: data analitics aplicado al modelo Big Five [link](https://www.sngular.com/es/data-analytics-big-five/)
- Baremación española del NEO-PI [link](http://scielo.isciii.es/scielo.php?script=sci_arttext&pid=S1130-52742009000200003)
- Estudio de validez convergente y estructural del NEO-PI [link](https://www.uv.es/seoane/boletin/previos/N92-1.pdf)
- Introducción a la psicología - Teoría clasica de respuest al item [link](http://aprendeenlinea.udea.edu.co/lms/investigacion/file.php/39/ARCHIVOS_2010/PDF/IntPsicometria_aristidesvara_1_.pdf)
