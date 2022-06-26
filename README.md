# Tuhabi challenge
Propuesta de solución a la prueba técnica backend de Tuhabi.

## _Información general_
Stack de tecnologías a implementar en esta solución basada en la arquitectura de microservicios.
- python 3.8.10+ 
- Libreía pymysql para conexiones MySQL
- Librería FastApi
- Librería uvicorn

## _Desarrollo_
Las consultas a la base de datos serán directamente en lenguaje SQL, esto, por los requerimientos de este desarrollo en particular.
Se evita el uso de un framework y un ORM.
Se realizará el desarrollo implementando Test-Driven Development, por lo cual, se escriben los casos de prueba para validar los criterios de aceptación de la HU: consulta de inmuebles.

También, se tendrá la HU: Habilitador de me gusta en inmuebles. Esta solo en propuesta junto con un diagrama de la base de datos o documentación correspondiente mejorados.

## _Observaciones_
El criterio de búsqueda de inmuebles por estado, no está disponible, esto debido a que en la base de datos no se cuenta con esta información.
