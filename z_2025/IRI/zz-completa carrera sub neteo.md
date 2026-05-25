## Guía de Ejercicios de Subneteo VLSM (Máscara de Subred de Longitud Variable)

A continuación se presentan dos enunciados para la práctica de direccionamiento IP dinámico, utilizando una red base de Clase B. Para la resolución de ambos, se requiere el cálculo preciso del espacio de direcciones para optimizar el uso de los recursos.

---

### Ejercicio 1

Se ha asignado el bloque de red **172.18.0.0/16**. Se requiere realizar la segmentación necesaria para satisfacer los requerimientos de seis departamentos con las siguientes capacidades de hosts, presentadas de forma aleatoria:

* **Red A:** 1,200 hosts
* **Red B:** 100 hosts
* **Red C:** 4,500 hosts
* **Red D:** 25 hosts
* **Red E:** 8,000 hosts
* **Red F:** 500 hosts

### Ejercicio 2

Se dispone de la dirección de red **192.168.0.0/16**. Se solicita diseñar el esquema de direccionamiento para seis subredes con las siguientes necesidades de hosts, listadas sin un orden específico:

* **Red 1:** 2,500 hosts
* **Red 2:** 150 hosts
* **Red 3:** 6,000 hosts
* **Red 4:** 12,000 hosts
* **Red 5:** 60 hosts
* **Red 6:** 800 hosts

---

### Requerimientos de resolución para cada ejercicio

Para cada una de las subredes solicitadas, se debe determinar y presentar la siguiente información técnica:

* **a)** Prefijo de red (`/N`) y máscara de subred en formato decimal punteado.
* **b)** Dirección IP de red y el rango completo de direcciones IP utilizables (primer y último host).
* **c)** Dirección IP de broadcast.
* **d)** Cantidad de direcciones totales de la subred (incluyendo red y broadcast).
* **e)** Cantidad de bits de host utilizados.

<div style="page-break-after: always;"></div>

## Resultados de los Ejercicios (Solucionario)

Para la correcta resolución, se han ordenado las subredes de mayor a menor cantidad de hosts requeridos a fin de optimizar el direccionamiento.

### Resolución Ejercicio 1 (Red Base: 172.18.0.0/16)

| Subred | Hosts Req. | Bits Host | Prefijo | Máscara | Dir. de Red | Rango Utilizable | Broadcast | Dir. Totales |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Red E** | 8,000 | 13 | /19 | 255.255.224.0 | 172.18.0.0 | 172.18.0.1 - 172.18.31.254 | 172.18.31.255 | 8,192 |
| **Red C** | 4,500 | 13 | /19 | 255.255.224.0 | 172.18.32.0 | 172.18.32.1 - 172.18.63.254 | 172.18.63.255 | 8,192 |
| **Red A** | 1,200 | 11 | /21 | 255.255.248.0 | 172.18.64.0 | 172.18.64.1 - 172.18.71.254 | 172.18.71.255 | 2,048 |
| **Red F** | 500 | 9 | /23 | 255.255.254.0 | 172.18.72.0 | 172.18.72.1 - 172.18.73.254 | 172.18.73.255 | 512 |
| **Red B** | 100 | 7 | /25 | 255.255.255.128 | 172.18.74.0 | 172.18.74.1 - 172.18.74.126 | 172.18.74.127 | 128 |
| **Red D** | 25 | 5 | /27 | 255.255.255.224 | 172.18.74.128 | 172.18.74.129 - 172.18.74.158 | 172.18.74.159 | 32 |

---

### Resolución Ejercicio 2 (Red Base: 192.168.0.0/16)

| Subred | Hosts Req. | Bits Host | Prefijo | Máscara | Dir. de Red | Rango Utilizable | Broadcast | Dir. Totales |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Red 4** | 12,000 | 14 | /18 | 255.255.192.0 | 192.168.0.0 | 192.168.0.1 - 192.168.63.254 | 192.168.63.255 | 16,384 |
| **Red 3** | 6,000 | 13 | /19 | 255.255.224.0 | 192.168.64.0 | 192.168.64.1 - 192.168.95.254 | 192.168.95.255 | 8,192 |
| **Red 1** | 2,500 | 12 | /20 | 255.255.240.0 | 192.168.96.0 | 192.168.96.1 - 192.168.111.254 | 192.168.111.255 | 4,096 |
| **Red 6** | 800 | 10 | /22 | 255.255.252.0 | 192.168.112.0 | 192.168.112.1 - 192.168.115.254 | 192.168.115.255 | 1,024 |
| **Red 2** | 150 | 8 | /24 | 255.255.255.0 | 192.168.116.0 | 192.168.116.1 - 192.168.116.254 | 192.168.116.255 | 256 |
| **Red 5** | 60 | 6 | /26 | 255.255.255.192 | 192.168.117.0 | 192.168.117.1 - 192.168.117.62 | 192.168.117.63 | 64 |