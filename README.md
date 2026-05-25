# 📊 Análisis del Proyecto Educativo "Aulico"

## 🎯 Visión General

El proyecto **Aulico** es un repositorio de materiales educativos para enseñanza técnica a nivel secundario/técnico. Se organiza como un sistema de gestión de contenidos docentes con múltiples cursos/materias, cada uno con sus propios materiales para alumnos y profesores.

## 📁 Estructura del Proyecto

### Organización por Cursos

El proyecto contiene **7 cursos principales** y directorios de archivo temporal:

| Código | Curso/Materia | Área Temática | Estudiantes |
|--------|---------------|---------------|-------------|
| **C3Z1** | Computación 3er Año 1er Bimestre | Informática básica | - |
| **CYA** | Control y Automatización | PLC, lógica cableada, sistemas de control | 62 |
| **EIN** | Electrónica Industrial | Electrónica, sistemas de control, circuitos lógicos | 75 |
| **IRI** | Infraestructura de Redes e Internet | Redes LAN, OSI, TCP/IP, cableado estructurado | 72 |
| **LPR** | Lógica de Programación | Python, programación estructurada | 62 |
| **LSO** | - | - | 62 |
| **PWD** | - | - | 71 |

### Directorios de Archivo

- **z_2025/**: Materiales del año 2025 (Adultos Fines, Física, Cens464)
- **z_2026/**: Materiales del año 2026 (EAU - Electrónica y Automatización)
- **z_Material en General/**: Recursos compartidos

## 🏗️ Estructura Interna de Cada Curso

Cada curso sigue un patrón de organización consistente:

```
[CODIGO]/
├── [CODIGO]-Para_Alumnos/          # Materiales para estudiantes
│   ├── 00-Contrato Didactico.pdf
│   ├── 00-Uso de Celulares.pdf     # Política de uso de dispositivos
│   ├── [NUM]-Actividad-[Tema].pdf  # Actividades prácticas
│   └── [NUM]-Material-[Tema].pdf   # Material de lectura/teórico
│
└── [CODIGO]-Para_Profesor/         # Materiales para docentes
    ├── 00-ListaAlumnos.gsheet      # Lista de estudiantes
    ├── [CODIGO]-[NUM]-Planificacion_Aulica-[Tema].pdf
    ├── [CODIGO]-[NUM]-Sintesis+Resolucion-[Tema].pdf
    ├── [CODIGO]-[NUM]-Evaluacion.md/pdf
    └── pdt-[CODIGO].md             # Notas/pendientes
```

## 📋 Patrones de Nomenclatura

### Numeración de Actividades
- **E0C1**: Evaluación 0, Clase 1 (Repaso/saberes previos)
- **E1C1**: Evaluación 1, Clase 1 (Primer módulo)
- **E1C2**: Evaluación 1, Clase 2
- **01, 11, 12, 21**: Secuencia de actividades dentro de un módulo

### Tipos de Archivos
- **Actividad**: Ejercicios prácticos para estudiantes
- **Material**: Contenido teórico y guías de lectura
- **Planificación_Aulica**: Plan de clase para el profesor
- **Sintesis+Resolucion**: Resumen y soluciones de actividades
- **Evaluación**: Exámenes y cuestionarios

## 🔍 Análisis Detallado por Curso

### 1. **CYA - Control y Automatización**
**Contenido:**
- Lógica cableada y componentes eléctricos industriales
- Hardware del PLC (Controlador Lógico Programable)
- Señales digitales y analógicas
- Sistema de direccionamiento
- Entorno de programación y comunicación
- Lenguaje Ladder

**Recursos:**
- Videos de YouTube (enlace en `CYA/CYA-Para_Profesor/pdt-CYA.md`)
- Evaluaciones con respuestas

### 2. **IRI - Infraestructura de Redes e Internet**
**Contenido:**
- Redes LAN y topologías
- Modelo OSI (análisis detallado de capas)
- Cableado estructurado y conectorización
- Enlace físico y conectorización cruzada
- Fundamentos de TCP/IP
- Sistema binario y direccionamiento de red
- Máscaras de red y cálculo de direccionamiento
- Configuración de direcciones IP estáticas
- Diagnóstico de conectividad (ipconfig, ping)

**Recursos:**
- Comunicaciones a estudiantes (`IRI/IRI-Profesor/IRI-141-Comunicacion.md`)
- Evaluaciones programadas
- Materiales adicionales sobre cableado estructurado

### 3. **EIN - Electrónica Industrial**
**Contenido:**
- Fundamentos de electrónica industrial
- Sistemas de control
- Circuitos lógicos fundamentales
- Electrónica digital para control

### 4. **LPR - Lógica de Programación**
**Contenido:**
- Python para programadores con experiencia en C++
- Temas básicos: indentación, tipado dinámico, estructuras de control, tipos de datos, funciones

**Recursos:**
- `Guía Temática de Python` (LPR/LPR-Profesor/Guía Temática de Python para Programadores con Experiencia en C++.md)
- `temas_basicos_python.md` con progreso de capacitación
- Cuestionarios de fundamentos primordiales

### 5. **C3Z1 - Computación Básica**
**Contenido:**
- Introducción al hardware y software
- Gestión de archivos y carpetas
- Uso de procesador de textos
- Elaboración de CV (modelo Harvard)
- Historia de la computadora

### 6. **z_2026/EAU - Electrónica y Automatización (2026)**
**Contenido:**
- Seguridad y EPP (Equipos de Protección Personal)
- Cargas y campo eléctrico

## 📊 Características del Proyecto

### ✅ Fortalezas
1. **Organización sistemática**: Estructura clara y consistente entre cursos
2. **Separación de roles**: Materiales diferenciados para alumnos y profesores
3. **Documentación completa**: Planificaciones, síntesis, resoluciones y evaluaciones
4. **Uso de múltiples formatos**: PDF, Markdown, Google Sheets, Google Docs
5. **Políticas institucionales**: Contratos didácticos y normativas de uso de celulares
6. **Seguimiento de estudiantes**: Listas de alumnos en Google Sheets
7. **Versionado temporal**: Archivos organizados por año académico

### 🔧 Tecnologías y Herramientas
- **Google Workspace**: Sheets (listas), Docs (contratos)
- **PDF**: Materiales educativos y planificaciones
- **Markdown**: Notas y documentación técnica
- **Excel**: Planificaciones de módulos
- **YouTube**: Recursos multimedia

### 📈 Metodología Educativa
- **Enfoque práctico**: Actividades y ejercicios integrados
- **Evaluación continua**: Múltiples evaluaciones por módulo
- **Scaffolding**: Materiales progresivos desde saberes previos hasta temas avanzados
- **Retroalimentación**: Síntesis y resoluciones disponibles para profesores

## 🎯 Conclusiones

Este es un **sistema de gestión de contenidos educativos** bien estructurado para enseñanza técnica en áreas de:
- Informática y computación
- Redes y comunicaciones
- Electrónica y automatización
- Programación

El proyecto demuestra una planificación docente rigurosa con materiales completos, seguimiento de estudiantes y documentación exhaustiva de cada clase y evaluación. La estructura modular permite fácil mantenimiento y actualización de contenidos.

---

**Fecha de análisis:** 2026-05-25