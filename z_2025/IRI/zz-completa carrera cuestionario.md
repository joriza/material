## Completa carrera 2026 (Mayo)

### Cuestionario de Análisis Técnico

1. **Pregunta:** ¿Cuál es el límite dimensional exacto, expresado en bytes, que rige la transmisión de tramas Ethernet para evitar la ineficiencia de la fragmentación de datos?
**Respuesta esperada:** 1500 bytes.
**Cita:** "Para Ethernet... la MTU estándar es de 1500 bytes." (Pág. 1, MTU y Dispositivos de Red).

2. **Pregunta:** En la arquitectura de red contemporánea, ¿qué dispositivo ha desplazado al hub al operar en la Capa 2 y segmentar los dominios de colisión de manera inteligente?
**Respuesta esperada:** El Switch.
**Cita:** "Los Switches (Capa 2) son el corazón de las LAN modernas... eliminan los dominios de colisión." (Pág. 5, MTU y Dispositivos de Red).

3. **Pregunta:** ¿Qué identificador físico inmutable, compuesto por 48 bits, se requiere para el direccionamiento de dispositivos en la Capa de Enlace de Datos?
**Respuesta esperada:** Dirección MAC.
**Cita:** "La Dirección MAC... es un identificador único y físico asignado a cada Placa de Red (NIC) por su fabricante." (Pág. 1, Dirección MAC y Encapsulación).

4. **Pregunta:** ¿Bajo qué estándar de la IEEE se rige la tecnología LAN dominante que ha evolucionado de métodos de acceso compartidos a entornos *full-duplex*?
**Respuesta esperada:** IEEE 802.3 (Ethernet).
**Cita:** "Ethernet (IEEE 802.3) es el estándar LAN dominante, evolucionando de CSMA/CD... a full-duplex." (Pág. 5, Estándares de Red y Componentes Básicos).

5. **Pregunta:** ¿Qué entidad lógica de red es responsable de interconectar redes IP disímiles y actuar como frontera infranqueable para los mensajes de *broadcast*?
**Respuesta esperada:** El Router.
**Cita:** "Un Dominio de Broadcast es un segmento donde los mensajes de broadcast se propagan, y los Routers los segmentan (no reenvían broadcasts)." (Pág. 5, Routers y Dominios de Red).

6. **Pregunta:** En el contexto de la conectorización de medios guiados, ¿cuál es la norma específica que dicta la secuencia cromática de los hilos para garantizar la interoperabilidad en cables RJ45?
**Respuesta esperada:** Norma EIA/TIA 568B.
**Cita:** "La Norma EIA/TIA 568B es el estándar para el orden de los hilos en el conector RJ45." (Pág. 5, Cableado Estructurado Básico).

7. **Pregunta:** ¿Cómo se denomina el proceso técnico mediante el cual cada capa del modelo OSI añade información de control a los datos procedentes de las capas superiores?
**Respuesta esperada:** Encapsulación.
**Cita:** "La encapsulación es el proceso de añadir encabezados... a los datos en cada capa del Modelo OSI." (Pág. 5, Dirección MAC y Encapsulación).

8. **Pregunta:** ¿Qué protocolo de la capa de transporte se debe seleccionar cuando la prioridad absoluta es la velocidad y la baja latencia, aceptando la posible pérdida de datagramas?
**Respuesta esperada:** UDP (User Datagram Protocol).
**Cita:** "Se utiliza cuando la velocidad y la baja latencia son primordiales, y la aplicación puede manejar la pérdida de paquetes." (Pág. 5, Protocolos Complementarios de TCP/IP).

9. **Pregunta:** ¿Cuál es la topología física que, a pesar de su alta redundancia y resiliencia, presenta una complejidad y costo de implementación prohibitivos para entornos LAN convencionales?
**Respuesta esperada:** Topología de Malla.
**Cita:** "La topología de Malla (física) ofrece alta redundancia pero es muy costosa y compleja." (Pág. 7, Topologías de Red).

10. **Pregunta:** ¿Cómo se denomina técnicamente a la PDU (Unidad de Datos de Protocolo) una vez que ha sido procesada y etiquetada por la Capa de Red (Capa 3)?
**Respuesta esperada:** Paquete (o Datagrama).
**Cita:** "Las PDUs cambian de nombre en cada capa: ... Paquete (Red)." (Pág. 5, Dirección MAC y Encapsulación).

---

### Listado de Preguntas para Alumnos

1. ¿Cuál es el límite dimensional exacto, expresado en bytes, que rige la transmisión de tramas Ethernet para evitar la ineficiencia de la fragmentación de datos?
2. En la arquitectura de red contemporánea, ¿qué dispositivo ha desplazado al hub al operar en la Capa 2 y segmentar los dominios de colisión de manera inteligente?
3. ¿Qué identificador físico inmutable, compuesto por 48 bits, se requiere para el direccionamiento de dispositivos en la Capa de Enlace de Datos?
4. ¿Bajo qué estándar de la IEEE se rige la tecnología LAN dominante que ha evolucionado de métodos de acceso compartidos a entornos *full-duplex*?
5. ¿Qué entidad lógica de red es responsable de interconectar redes IP disímiles y actuar como frontera infranqueable para los mensajes de *broadcast*?
6. En el contexto de la conectorización de medios guiados, ¿cuál es la norma específica que dicta la secuencia cromática de los hilos para garantizar la interoperabilidad en cables RJ45?
7. ¿Cómo se denomina el proceso técnico mediante el cual cada capa del modelo OSI añade información de control a los datos procedentes de las capas superiores?
8. ¿Qué protocolo de la capa de transporte se debe seleccionar cuando la prioridad absoluta es la velocidad y la baja latencia, aceptando la posible pérdida de datagramas?
9. ¿Cuál es la topología física que, a pesar de su alta redundancia y resiliencia, presenta una complejidad y costo de implementación prohibitivos para entornos LAN convencionales?
10. ¿Cómo se denomina técnicamente a la PDU (Unidad de Datos de Protocolo) una vez que ha sido procesada y etiquetada por la Capa de Red (Capa 3)?

---

### Ejercicio de Refuerzo de Conceptos

**Actividad: Análisis de Diagnóstico y Diseño de Red**

Se plantea el siguiente escenario para su resolución técnica:
Una institución educativa reporta que su red, basada en una topología de bus física con hubs antiguos, presenta una lentitud extrema y constantes errores de colisión. Además, al enviar un archivo pesado desde una estación de trabajo, la red se bloquea momentáneamente.

**Tareas a realizar:**
1. Identificar el problema estructural relacionado con los dominios de colisión.
2. Proponer el cambio de hardware necesario especificando la capa del modelo OSI en la que opera el nuevo dispositivo.
3. Determinar qué protocolo de transporte (TCP o UDP) sería el adecuado para garantizar que los archivos de los alumnos lleguen sin errores ni desorden.
4. Explicar brevemente qué sucedería si el tamaño de los paquetes generados supera los 1500 bytes de la red Ethernet.

**Respuestas del Ejercicio:**
1. **Problema:** Al usar un bus físico con hubs, todos los dispositivos comparten un único dominio de colisión, lo que genera congestión masiva.
2. **Propuesta:** Reemplazar los hubs por switches, los cuales operan en la Capa 2 (Enlace de Datos) y segmentan la red en múltiples dominios de colisión.
3. **Protocolo:** TCP, ya que garantiza la integridad, el orden de los datos y el reenvío en caso de pérdida.
4. **Consecuencia:** Se produciría la fragmentación de los datos, lo que degradaría el rendimiento de la red y aumentaría la carga de procesamiento en los dispositivos.