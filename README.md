# Práctica de integración continua con GitHub Actions

Proyecto de ejemplo para probar automáticamente una función de Python con `pytest` en cada `push`.

## Integrantes

- Integrante 1: completar nombre
- Integrante 2: completar nombre

## Crear el repositorio en GitHub

1. En GitHub, crea un repositorio público llamado `ci-practica-equipo##`, reemplazando `##` por el número asignado al equipo (por ejemplo, `ci-practica-equipo01`).
2. No inicialices el repositorio con otro README si vas a subir estos archivos.
3. En una terminal, desde esta carpeta, conecta el repositorio y sube el proyecto. Sustituye `USUARIO` por tu nombre de usuario de GitHub:

```bash
git add .
git commit -m "Primer commit"
git branch -M main
git remote add origin https://github.com/USUARIO/ci-practica-equipo##.git
git push -u origin main
```

Si ya existe un remoto llamado `origin`, actualízalo con `git remote set-url origin URL_DEL_REPOSITORIO` en lugar de volver a agregarlo.

## Proyecto y pruebas

`calculadora.py` contiene las funciones `suma`, `resta` y `multiplicacion`. `test_calculadora.py` verifica cada operación. Para ejecutar las pruebas y revisar la cobertura localmente:

```bash
python -m pip install pytest pytest-cov
python -m pytest --cov=. --cov-report=term-missing
```

## Integración continua

El workflow `.github/workflows/ci.yml` se ejecuta en cada `push`. Prepara Python 3.12, instala `pytest` y `pytest-cov`, ejecuta las pruebas y genera `coverage.xml`. Publica el reporte con el nombre `coverage-report`. Si las pruebas fallan, la ejecución se detiene antes de publicar reportes o el artefacto de build.

La fase Build no compila el código Python: reúne el archivo fuente en una carpeta distribuible. El artefacto `build-python` es un ZIP descargable que contiene `artefactos/calculadora.py`. El reporte de cobertura `coverage-report` indica qué porcentaje del código está cubierto y qué líneas faltan por probar.

El workflow genera ambos artefactos en GitHub Actions. Descárgalos desde **Artifacts** en la ejecución correspondiente.

## Evidencias y reflexión

Incluyan en la entrega:

- URL del repositorio.
- Archivo `.github/workflows/ci.yml`.
- Captura de pruebas locales exitosas y del porcentaje de cobertura.
- Captura de una ejecución exitosa en **Actions** y de los artefactos `coverage-report` y `build-python`.
- Captura del reporte automático de cobertura.
- Captura de una ejecución fallida en **Actions**.
- Respuestas a las preguntas de cobertura: porcentaje obtenido, existencia de código sin probar y funciones faltantes. Con pruebas para cada función, se espera 100 % de cobertura de líneas de `calculadora.py`.
- Relación de la falla intencional con **Fail Fast**, **Feedback inmediato** y **Shift Left Testing**.
- Una conclusión personal de cada integrante, con sus propias palabras.

Para generar la ejecución fallida solicitada, cambien temporalmente `return a + b` por `return a - b` en `calculadora.py`, hagan commit y push, y capturen el fallo en **Actions**. Después restauren la suma correcta, hagan otro commit y push, y confirmen que el workflow vuelve a pasar. Así el repositorio termina en estado funcional.

Conclusión individual (integrante 1): completar aquí cómo ayuda encontrar errores antes de liberar el software.

Conclusión individual (integrante 2): completar aquí cómo ayuda encontrar errores antes de liberar el software.
