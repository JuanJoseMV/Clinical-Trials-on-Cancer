# Clinical-Trials-on-Cancer

Este repositorio representa el trabajo hecho en el semillero de investigación Machine Learning de la Universidad de Antioquia, sobre el proyecto Clinical Trials on Cancer donde se crean modelos de Machine Learning para predecir si un ensayo clínico puede ser considerado un criterio de inclusión o exclusión a un tratamiento para pacientes con cáncer.

## Archivos y gráficas
El proyecto cuenta con el Dataset principal (que puede ser descargado en https://www.kaggle.com/auriml/eligibilityforcancerclinicaltrials). Algunos archivos que sobrepasaron el límite de peso de Github están almacenados en la careta compartida de Google Drive del proyecto y se agregan al .gitignore para evitar problemas a la hora de hacer cambios. Además, se tienen los datasets creados para los diferentes experimetos que se realizaron. También cuenta con gráficas de cada experimento realizado. Se tiene un registro de los modelos más importantes usados durante el experimento, las diferentes tablas que se requirieron para la práctica y algunos textos que almacenan información de los diferentes procesos hechos.

## Notebooks
En la carpeta de Notebooks se encuentran todos los notebooks usados para los experimentos. Estos notebooks están separadoos por categorías y en cada notebook se pueden encontrar los experimentos realizados para cada tema específico, ya sea para la limpieza de datos o correr modelos con digferentes parámetros. 

En los notebooks de preprocesamiento se hace una limpieza de la base de datos original, se toma una porción de esta y se guarda para usarla en los demás modelos. Luego, en los notebooks de los modelos se crearon funciones para cargar los datos preprocesados y almacenarlos en las variables globales X y Y. Cada modelo básico cuenta con funciones para correr un modlo con parámetros específicos, realizar un GridSearch, dibujar la curva de aprendizaje, la curva ROC y algunas funciones auxiliares.

## Trabajo en proceso
En la sección de Sequential Forward Selection se está trabajando en la elaboración de un algortimo de búsqueda secuencial de características con criterios tipo filtro que funcione en paralelo. Las funciones tipo filtro se pueden observar en el archivo AtomicFunctions.py. Esta sección todavía está en construcción ya que presentó algunos errores en su implementación.

Además, la sección de Voting también se encuentra en proceso.
