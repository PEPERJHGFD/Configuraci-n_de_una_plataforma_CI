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

`calculadora.py` contiene la función `suma`. `test_calculadora.py` comprueba que sumar 2 y 3 devuelve 5. Para ejecutar la prueba localmente:

```bash
python -m pip install pytest
python -m pytest
```

## Integración continua

El workflow `.github/workflows/ci.yml` se ejecuta en cada `push`. Prepara Python 3.12, instala `pytest`, ejecuta las pruebas y genera `artefactos/calculadora.py`. Después comprime esa carpeta en `artefacto.zip` y publica el ZIP con el nombre `build-python` mediante GitHub Actions.

Esta fase Build no compila el código Python: reúne el archivo fuente en una carpeta distribuible. El artefacto es el ZIP descargable que contiene `artefactos/calculadora.py`. Si las pruebas fallan, los pasos siguientes no se ejecutan y no se publica el artefacto.

Para comprobarlo localmente, ejecuta `python -m pytest`. El workflow crea el artefacto en GitHub Actions. Descarga `build-python` desde **Artifacts**: GitHub empaqueta el archivo `artefacto.zip` en el ZIP descargado; al extraerlo y abrir `artefacto.zip`, encontrarás `artefactos/calculadora.py`.

## Evidencias y reflexión

Incluyan en la entrega:

- URL del repositorio.
- Archivo `.github/workflows/ci.yml`.
- Captura de una ejecución exitosa en **Actions**, con los pasos Build, ZIP y subida exitosos.
- Captura del artefacto `build-python` y de `calculadora.py` dentro de `artefacto.zip` después de descargarlo.
- Captura de una ejecución fallida en **Actions**.
- Respuestas a las preguntas de la actividad:
  - Generar artefactos automáticamente evita repetir manualmente el empaquetado y permite descargar el mismo resultado de cada ejecución.
  - Si las pruebas o el build fallan, el workflow se detiene y no publica un artefacto incorrecto.
  - Obtener el mismo artefacto reduce diferencias entre lo probado y lo distribuido.
- Una conclusión personal de cada integrante, con sus propias palabras.

Para generar la ejecución fallida solicitada, cambien temporalmente `return a + b` por `return a - b` en `calculadora.py`, hagan commit y push, y capturen el fallo en **Actions**. Después restauren la suma correcta, hagan otro commit y push, y confirmen que el workflow vuelve a pasar. Así el repositorio termina en estado funcional.

Conclusión individual (integrante 1): completar aquí cómo ayuda encontrar errores antes de liberar el software.

Conclusión individual (integrante 2): completar aquí cómo ayuda encontrar errores antes de liberar el software.
