
# Sesión 05: Distribuciones muestrales y técnicas de evaluación de modelos

## :dart: Objetivos

- Distinguir la diferencia entre población y muestra.
- Entender el concepto de 'sesgos' y por qué es tan importante estar conscientes de ellos.
- Aprender el concepto de muestreo aleatorio y cómo puede protegernos parcialmente de los sesgos.
- Utilizar la técnica 'bootstrap' como medio para explorar la distribución muestral de una estadística.
- Crear y utilizar histogramas, errores estándar e intervalos de confianza para evaluar la incertidumbre de una medida estadística.
- Utilizar técnicas para evitar sesgos en el entrenamiento de modelos, como la división de datasets y la validación cruzada.

## 📂 Contenido

<ins>Poblaciones y muestras</ins>

En un estudio estadístico la *población* es el grupo completo acerca del cual se pretende obtener cierta información. Una *muestra* es un subconjunto de esa población.

Es muy importante antes de empezar un análisis estadístico tener muy claro cuáles son los parámetros que definen a nuestra población. Esos parámetros pueden ser geográficos, étnicos, de género, profesionales, etc.

Una de las tareas que realizamos como científicos de datos es la de definir poblaciones, obtener muestras de datos de estas poblaciones, y encontrar procedimientos a través de los que podamos encontrar información útil que pueda ser aplicable a una gran parte de la población. Dado que muchas veces tener datos concisos de **toda** la población es muy difícil, costoso o hasta imposible, debemos aprender a trabajar con muestras de manera efectiva.

Platiquemos un poco acerca de:

1. ¿Cómo definir poblaciones?
2. ¿A qué retos nos enfrentamos cuando definimos poblaciones?
3. ¿Cuáles pueden ser las consecuencias de definir incorrectamente a una población?
4. ¿Cómo generalizamos información de una muestra a una población?
5. ¿Qué problemas pueden surgir en este proceso de generalización?
6. ¿Cómo podemos evitar algunos de estos problemas o aunque sea minimizarlos?

---

<ins>Sesgos en nuestros datos</ins>

Una de las dificultades a las que nos enfrentamos cuando trabajamos con muestras de datos es que hay una alta probabilidad de que nuestros datos estén sesgados. Esto quiere decir que tienen una tendencia que no refleja la realidad tal y como es.

Los sesgos son muy peligrosos. Dificultan y hasta imposibilitan la obtención de información útil. Cuando nuestros datos están sesgados, la información que obtengamos no puede ser generalizada  al resto de la población, puesto que no refleja la realidad como es, sólo una perspectiva de ella.

Entrenar modelos predictivos y clasificatorios utilizando datos sesgados puede resultar en enormes e inaceptables injusticias.

Como científicos de datos debemos de pensar y estar atentos a los sesgos de nuestros datos, no solamente porque distorsionan nuestros análisis, sino porque tenemos la responsabilidad de llevar a cabo nuestra profesión éticamente.

Platiquemos un poco acerca de:

1. ¿De dónde surgen los sesgos en nuestros datos? ¿Cómo llegan ahí?
2. ¿A qué problemas podemos enfrentarnos cuando hay sesgos en nuestros datos?
3. ¿Qué podemos hacer para evitar sesgos en nuestros datos?
4. ¿De qué manera dañan a la sociedad estos sesgos?
5. ¿Qué papel juegan los científicos de datos en la eliminación de estos sesgos?

---

<ins>Distribuciones muestrales de estadísticas y Bootstrap</ins>

Para este momento seguramente ya te habrás percatado de que las medidas estadísticas que hemos aprendido a hasta ahora no son infalibles. Cada vez que tomamos una medida estadística, existe cierta incertidumbre alrededor de ella. ¿Qué hubiera pasado si nuestra muestra fuera ligeramente distinta? ¿Nuestra medida se mantendría igual o cambiaría?

Dado que normalmente no es posible regresar al origen de los datos para adquirir más muestras, existen ciertos procedimientos que podemos realizar para determinar el nivel de incertidumbre que existe en nuestras medidas estadísticas.

Una de estas técnicas es el bootstrapping. Veamos cómo funciona.

>

[**`Ejemplo 1`**](Ejemplo-01/bootstrap.ipynb)
[**`Reto 1`**](Reto-01/bootstrap.ipynb)

---

<ins>Error estándar e intervalos de confianza</ins>

Ya que hemos tenemos una Serie con las medidas estadísticas tomadas de cada remuestra, además de revisar la distribución podemos hacer un par de cosas más.

El error estándar nos dice qué tan dispersas están nuestras medidas estadísticas. Esta es una de las maneras de cuantificar incertidumbre.

Los intervalos de confianza son una manera de mostrar la incertidumbre de una manera muy fácil de comprender, suelen utilizarse en ciencia de datos para establecer qué tan precisa es nuestra medida estadística.

>

[**`Ejemplo 2`**](Ejemplo-02/error_estandar_e_intervalos_de_confianza.ipynb)
[**`Reto 2`**](Reto-02/error_estandar_e_intervalos_de_confianza.ipynb)

---

<ins>Técnicas de evaluación de modelos</ins>

Así como podemos tener sesgos e incertidumbre en nuestras medidas estadísticas, también nos puede pasar lo mismo con los modelos predictivos que entrenamos.

Hay varias formas en las que podemos encontrar este tipo de problemas al entrenar modelos predictivos o clasificatorios. Aquí vamos a hablar de dos de ellas:

1. A veces puede suceder que los datos que tenemos ya tienen de por sí un sesgo incluido. Este sesgo puede provenir de la forma en la que fueron recabados los datos, de los sesgos de las personas que los recabaron, de un error de metodología, etc. Esto puede ocasionar que nuestros modelos entrenados no puedan realizar predicciones racionales. Platiquemos un poco acerca de esto:

  a) ¿De dónde pueden provenir estos sesgos? ¿Cómo llegan a nuestros datos?
  
  b) ¿Qué problemas pueden ocasionar? ¿Qué ejemplos tenemos de esto?
  
  c) ¿Cómo podemos protegernos de este tipo de errores? ¿Es posible eliminar por completo los sesgos en nuestros datos?

2. Existe la posibilidad de que un modelo que entrenemos resulte muy bueno para predecir los datos con los que fue entrenado, pero que no pueda generalizar su capacidad predictiva a datos que no ha visto anteriormente. Como normalmente tampoco es una opción regresar a la fuente de los datos para colectar nuestras muestras, necesitamos entonces algunas técnicas que nos permitan tener un poco más de confianza en nuestros modelos. A continuación vamos a ver en la práctica dos maneras de evitar este problema.

---

<ins>Dataset de entrenamiento y dataset de prueba</ins>

Un primer acercamiento puede ser tomar nuestro dataset y dividirlo en dos: un dataset para entrenamiento y otro para pruebas. El modelo se entrena utilizando el dataset de entrenamiento y luego su precisión se evalúa utilizando el dataset de prueba. De esta manera se 'simula' la capacidad predictiva del modelo en el mundo real: probando su precisión con datos que nunca antes ha visto.

>

[**`Ejemplo 3`**](Ejemplo-03/entrenamiento_y_prueba.ipynb)
[**`Reto 3`**](Reto-03/entrenamiento_y_prueba.ipynb)

---

<ins>Validación cruzada</ins>

La validación cruzada lleva el método anterior aún más lejos, puesto que realiza múltiples divisiones, entrena el modelo múltiples veces usando combinaciones distintas de divisiones y evalúa al modelo usando el promedio de todos los entrenamientos.

>

[**`Ejemplo 4`**](Ejemplo-04/validacion_cruzada.ipynb)
[**`Reto 4`**](Reto-04/validacion_cruzada.ipynb)

---

## Postwork

[**`Postwork Sesión 5`**](Postwork/Readme.md)
