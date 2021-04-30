
# Sesión 02: Introducción a la visualización de datos: Distribuciones

## :dart: Objetivos

- Comprender el cocncepto de distribución e identificar la distribución de nuestros datos junto con su importancia.
- Utilizar la librería Seaborn.
- Conocer los boxplots y aprender a generarlos.
- Conocer las tablas de frecuencias y los histogramas como maneras de visualizar distribuciones.
- Clasificar algunas de las formas que generan los histogramas.
- Conocer las gráficas de densidad como una alternativa a los histogramas clásicos.

## 📂 Contenido

<ins>Distribuciones de Datos</ins>

Si tomamos el valor mínimo y el valor máximo de nuestro conjunto de datos tenemos el rango dentro del cual están contenidos todos nuestros datos. Pero dentro de ese rango los valores pueden estar distribuidos de muchas maneras distintas. A veces están muy cerca del valor mínimo, a veces están muy cerca del valor máximo; a veces se amontonan casi todos alrededor de la mediana y sólo unos pocos toman los valores extremos; a veces generan incluso dos "montículos" alrededor de los cuales se concentran la mayoría de los datos. Hay muchísimas posibilidades.

Usando valores individuales es imposible tener una idea general de nuestro conjunto y es por eso que solemos utilizar algunas técnicas que toman en cuenta todo el conjunto de datos al mismo tiempo. Hoy vamos a aprender cómo a través de la visualización de datos podemos darnos una idea mucho más precisa de cómo están organizados los datos en nuestro conjunto.

>

---

<ins>Boxplots</ins>

Los Boxplots (o diagramas de caja) son una manera de visualizar nuestros datos de forma que la organización de los percentiles se haga muy evidente.

Los Boxplots nos ayudan a discernir si nuestros datos están sesgados (si tienen una tendencia), si están dispersos o agrupados y si existen valores atípicos con valores extremos.

> 

[**`Ejemplo 1`**](Ejemplo-01/boxplots.ipynb)
[**`Reto 1`**](Reto-01/boxplots.ipynb)

---

<ins>Tabla de frecuencias</ins>

Los percentiles segmentan nuestros datos en segmentos de distinto tamaño en los que tenemos el mismo número de muestras. En cambio, las tablas de frecuencias segmentan nuestros datos en segmentos que miden lo mismo pero que contienen una cantidad distinta de muestras.

Esto puede darnos otra perspectiva de nuestros datos que también resulta muy útil. Vamos a aprender a generar una tabla de frecuencias usando pandas.

> 

[**`Ejemplo 2`**](Ejemplo-02/tabla_de_frecuencias.ipynb)
[**`Reto 2`**](Reto-02/tabla_de_frecuencias.ipynb)

---

<ins>Histogramas</ins>

Los histogramas son una manera de visualizar nuestras tablas de frecuencias.

El eje x es el rango de nuestros datos y se divide por segmentos (como los que generamos en el Ejemplo pasado).

El eje y indica el conteo de muestras en cada segmento.

> 

[**`Ejemplo 3`**](Ejemplo-04/histogramas.ipynb)

---

<ins>Describiendo histogramas</ins>

Ya que sabemos cómo generar histogramas con nuestros datos, necesitamos ahora algo de vocabulario para describir lo que vemos en ellos.

Describir nuestras distribuciones nos ayuda a comunicar nuestros hallazgos, así como también a encontrar técnicas específicas que podamos utilizar para analizar a más profundidad nuestros datos.

Aprendamos algunos de los términos más comunes.

> 

[**`Ejemplo 4`**](Ejemplo-04/describiendo_histogramas.ipynb)
[**`Reto 3`**](Reto-03/describiendo_histogramas.ipynb)

---

<ins>Gráficas de densidad</ins>

Las gráficas de densidad son una manera de obtener la densidad de probabilidad de un conjunto de datos. Saber cómo obtener una densidad de probabilidad y cómo se genera una gráfica de densidad está fuera del alcance de este curso. Pero lo que nos interesa a nosotros es que utilizando gráficas de densidad se vuelven mucho más evidentes las distribuciones de nuestros datos.

De igual manera, las gráficas de densidad son una gran herramienta para comparar distribuciones en una misma gráfica.

> 

[**`Ejemplo 5`**](Ejemplo-05/graficas_de_densidad.ipynb)
[**`Reto 4`**](Reto-04/graficas_de_densidad.ipynb)

---

## Postwork

[**`Postwork Sesión 2`**](Postwork/Readme.md)
