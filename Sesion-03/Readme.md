
# Sesión 03: Exploración de Variables Categóricas y Análisis Multivariable

## :dart: Objetivos

- Identificar distintas técnicas para explorar y visualizar variables categóricas.
- Añadir anotaciones a nuestras gráficas para hacerlas más comprensibles.
- Utilizar gráficas de barras.
- Graficar un conjunto de datos agrupado de acuerdo a dos variables categóricas.
- Producir más de una gráfica al mismo tiempo para compararlas.
- Graficar un conjunto de datos numéricos agrupados de acuerdo a una variable categórica.

## 📂 Contenido

<ins>Variables Categóricas</ins>

En la sesión pasada aprendimos a explorar la distribución de variables numéricas. ¿Qué hay de las categóricas? Hay muchas técnicas más que han sido desarrolladas para analizar variables categóricas, como las gráficas de barras y las tablas de contigencia. En esta sesión aprenderemos a utilizar estas técnicas.

También aprenderemos a darle un poco más de claridad a nuestras gráficas añadiendo títulos y leyendas. Además, aprenderemos a producir más de una gráfica al mismo tiempo para poder comparar entre múltiples categorías.

>

---

<ins>Anotando nuestras gráficas</ins>

En la sesión anterior aprendimos a realizar gráficas de distribuciones de datos, pero no vimos cómo añadir anotaciones para darle más claridad a nuestras visualizaciones.

Un científico de datos es un comunicador, y como tal es muy importante que podamos generar gráficas comprensibles y fáciles de interpretar para que la información que encontremos pueda ser transmitida.

> 

[**`Ejemplo 1`**](Ejemplo-01/anotando_graficas.ipynb)
[**`Reto 1`**](Reto-01/anotando_graficas.ipynb)

---

<ins>Gráficas de barras y la Moda</ins>

Así como los histogramas nos sirven para visualizar las distribuciones de variables numéricas, las gráficas de barras son una herramienta muy común para visualizar los conteos de frecuencias de variables categóricas.

En una gráfica de barras, el eje y puede indicar tanto conteo de frecuencias como el porcentaje de la frecuencia. Veamos cómo realizar ambas.

> 

[**`Ejemplo 2`**](Ejemplo-02/graficas_de_barras.ipynb)
[**`Reto 2`**](Reto-02/graficas_de_barras.ipynb)

---

<ins>Gráficas de pie</ins>

Un pequeño comentario acerca de las gráficas de pie:

Las gráficas de pie, aunque son muy utilizadas en la media popular, son gráficas en realidad bastante inefectivas. Para el cerebro humano es muy difícil comparar los distintos tamaños de los pedazos del pie, lo cual se presta a muchas malinterpretaciones.

Es recomendable usar gráficas de barras en vez de gráficas de pie. Si quieres saber más acerca de las razones por las que hay que evitar las gráficas de pie, puedes ir a este link: https://www.perceptualedge.com/articles/visual_business_intelligence/save_the_pies_for_dessert.pdf

> 

---

<ins>Tablas de contigencia e indexación en múltiples niveles</ins>

Es común que tengamos más de una variable categórica en nuestros conjuntos. Si queremos realizar un conteo de frecuencias usando dos o más variables categóricas para agrupar a nuestros datos podemos usar lo que se llama "tablas de contigencia".

`pandas` ofrece un método llamado `crosstab` que nos permite realizar estas tablas en un santiamén.

¡También aprovecharemos los resultados de nuestro método `crosstab` para aprender a indexar `DataFrames` con múltiples niveles de columnas!

> 

[**`Ejemplo 3`**](Ejemplo-03/tablas_de_contingencia.ipynb)
[**`Reto 3`**](Reto-03/tablas_de_contingencia.ipynb)

---

<ins>Graficando en múltiples axis</ins>

Cuando tenemos tablas de contigencia, la única manera de poder visualizarlas en una gráfica es generando varias gráficas al mismo tiempo. Afortunadamente `matplotlib` hace de este proceso algo muy sencillo.

> 

[**`Ejemplo 4`**](Ejemplo-04/graficando_multiples_axis.ipynb)
[**`Reto 4`**](Reto-04/graficando_multiples_axis.ipynb)

---

<ins>Boxplots y Violinplots</ins>

Las tablas de contingencia son muy útiles cuando queremos hacer conteo de frecuencias utilizando dos o más categorías para agrupar nuestros datos. En cambio los boxplots y violinplots resultan ser muy útiles cuando queremos analizar la distribución de una variable numérica después de haber sido agrupada utilizando una variable categórica.

> 

[**`Ejemplo 5`**](Ejemplo-05/boxplots_y_violinplots.ipynb)
[**`Reto 5`**](Reto-05/boxplots_y_violinplots.ipynb)

---

## Postwork

[**`Postwork Sesión 3`**](Postwork/Readme.md)
