# Clase 1 – Configurando el ecosistema Python: documentación paso a paso

Este documento detalla lo que se hizo siguiendo la guía
*GUIA_Clase01_Practica_Creando_Entornos_Virtuales_en_Python.pdf*.

- **Carpeta de trabajo (equivale a `Fapd` de la guía):** `C:\Users\jorge\Desktop\Python`
- **Sistema:** Windows 11, PowerShell
- **Python base:** 3.14.4 (instalado con el Python install manager, accesible con el launcher `py`)
- **Nombre del entorno virtual:** `nombre_entorno` (tal como lo pide la guía)

---

## Resumen de resultados

| Paso de la guía | Estado | Evidencia |
|---|---|---|
| 1. Carpeta de trabajo y navegación | Hecho (adaptado) | Se usó `Desktop\Python` en vez de `Documentos\Fapd` |
| 2. Crear el venv | Hecho | Existe `nombre_entorno\` con `Scripts\python.exe` (Python 3.14.4) |
| 3. Activación y permisos | Verificado | Política de ejecución ya es `RemoteSigned`; existe `Activate.ps1` |
| 4. Usar el entorno en VS Code | **Pendiente (lo haces tú)** | Ver sección "Lo que te queda por hacer" |
| 5. pip, numpy y `pip list` | Hecho | pip 26.3, numpy 2.5.5 dentro de `nombre_entorno\Lib\site-packages` |
| Actividad: instalar 8 librerías | Hecho | Las 8 se importan sin errores (tabla más abajo) |
| `.gitignore` | Hecho | Archivo `.gitignore` creado con el contenido de la guía |
| `requirements.txt` | Hecho | Generado con `pip freeze` (30 paquetes con versión fija) |

---

## Paso 1 – Carpeta de trabajo

**Qué dice la guía:** crear una carpeta `Fapd` en Documentos y entrar en ella desde la terminal.

**Qué se hizo:** como el proyecto ya estaba abierto en VS Code en `C:\Users\jorge\Desktop\Python`,
se usó esa carpeta como carpeta de trabajo, en lugar de crear `Documentos\Fapd`. Es equivalente:
lo importante es que el entorno viva dentro de la carpeta del proyecto.

```powershell
cd C:\Users\jorge\Desktop\Python
```

## Paso 2 – Crear el entorno virtual

**Qué dice la guía:** `python -m venv nombre_entorno` en Windows.

**Qué se hizo:** en esta máquina el comando `python` abre un atajo de la Microsoft Store en vez de
tu Python real (alias de ejecución de Windows). Por eso se usó el launcher `py`, que sí apunta a
Python 3.14.4:

```powershell
py -m venv nombre_entorno
```

Se usó el nombre `nombre_entorno`, exactamente como indica la guía. Como ese nombre no está en el `.gitignore` de la guía, se añadió `nombre_entorno/` a mano.

**Checkpoint 1 – OK:** apareció la subcarpeta `nombre_entorno` dentro de `Desktop\Python`.
Comprobación: `nombre_entorno\Scripts\python.exe --version` devuelve `Python 3.14.4`.

## Paso 3 – Activación y permisos

**Qué dice la guía:** si PowerShell bloquea scripts, ejecutar
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`, y luego activar con
`nombre_entorno\Scripts\activate`.

**Qué se hizo:**
1. Se consultó la política actual (solo lectura): `Get-ExecutionPolicy -Scope CurrentUser` → **`RemoteSigned`**.
   Ya está como pide la guía, así que **no hizo falta cambiar nada**.
2. Se comprobó que existe `nombre_entorno\Scripts\Activate.ps1`.
3. Para instalar y verificar, se llamó directamente al Python del entorno
   (`nombre_entorno\Scripts\python.exe`). Esto equivale a tener el entorno activado, sin depender del prompt.

Para activarlo tú en la terminal:

```powershell
nombre_entorno\Scripts\activate
```

**Checkpoint 2 – lo verificas tú:** el prompt debe empezar con `(nombre_entorno)`:
`(nombre_entorno) PS C:\Users\jorge\Desktop\Python>`

Para salir del entorno (buena práctica de la guía):

```powershell
deactivate
```

**Checkpoint 3:** el prompt vuelve al formato original, sin el prefijo.

## Paso 4 – Usar el entorno en VS Code (pendiente, manual)

Esto requiere hacer clic en la interfaz de VS Code, por lo que queda para ti:

- **Scripts `.py`:** abre un archivo `.py`, haz clic en la versión de Python en la barra de estado
  (abajo a la derecha, ahora aparece `Python 3.14.4`) y elige el intérprete
  `nombre_entorno` (`.\nombre_entorno\Scripts\python.exe`). Si ves el menú "Select an environment manager" que
  salió antes, elige **venv** y selecciona el entorno existente en lugar de crear uno nuevo.
- **Cuadernos Jupyter `.ipynb`:** crea el cuaderno, pulsa **Seleccionar Kernel → Entornos de Python →
  `nombre_entorno`**. Para esto VS Code puede pedir instalar `ipykernel` en el entorno, acepta.

**Checkpoint 4:** al abrir la carpeta, VS Code detecta `nombre_entorno` y lo recomienda como entorno preferido.

## Paso 5 – Actualizar pip e instalar numpy

**Qué dice la guía:** `python.exe -m pip install --upgrade pip`, luego `pip install numpy` y `pip list`.

**Qué se hizo** (usando el Python del venv):

```powershell
nombre_entorno\Scripts\python.exe -m pip install --upgrade pip      # pip 26.3 dentro del venv
nombre_entorno\Scripts\python.exe -m pip install numpy               # numpy 2.5.5
nombre_entorno\Scripts\python.exe -m pip list
```

**Checkpoint 5 – OK:** `numpy` aparece en `pip list` y su carpeta existe en
`nombre_entorno\Lib\site-packages\numpy`, es decir, quedó instalado **dentro del entorno** y no en el
Python global.

## Actividad – Instalar las 8 librerías

```powershell
nombre_entorno\Scripts\python.exe -m pip install numpy pandas seaborn plotly scikit-learn statsmodels beautifulsoup4 category_encoders
```

Resultado: instalación correcta. Se verificó importando cada una dentro del entorno:

| Librería (nombre de import) | Versión | Estado |
|---|---|---|
| numpy | 2.5.5 | OK |
| pandas | 3.1.1 | OK |
| seaborn | 0.13.2 | OK |
| plotly | 7.1.0 | OK |
| scikit-learn (`sklearn`) | 1.9.1 | OK |
| statsmodels | 0.15.0 | OK |
| beautifulsoup4 (`bs4`) | 4.15.0 | OK |
| category_encoders | 2.11.2 | OK |

pip instaló además sus dependencias (scipy, matplotlib, joblib, patsy, etc.).

## Buena práctica – `.gitignore`

Se creó `C:\Users\jorge\Desktop\Python\.gitignore` con el contenido de la guía: ignora
`.venv/`, `venv/`, `env/`, `ENV/` (más `nombre_entorno/`, añadido a mano), `__pycache__/`, `*.pyc` y `.vscode/`. Así, si más adelante subes el
proyecto a GitHub, no se sube la carpeta del entorno (miles de archivos binarios).

> Nota: `.vscode/` está ignorado (es opcional según la guía). Si quieres compartir la configuración
> de VS Code con tu equipo, quita esa línea.

## Buena práctica – `requirements.txt`

```powershell
nombre_entorno\Scripts\python.exe -m pip freeze > requirements.txt
```

Se generó `requirements.txt` con los 30 paquetes y sus versiones exactas (codificación ASCII, que es
la que pip espera). Este archivo **sí** se sube a GitHub. Quien clone el proyecto solo hace:

```powershell
py -m venv nombre_entorno
nombre_entorno\Scripts\activate
pip install -r requirements.txt
```

**Checkpoint 6:** el archivo existe en la raíz de la carpeta. Hay que regenerarlo cada vez que
instales una librería nueva.

---

## Diferencias respecto a la guía (y por qué)

1. **Carpeta:** `Desktop\Python` en lugar de `Documentos\Fapd`, porque es tu proyecto abierto en VS Code.
2. **`py` en lugar de `python`:** en tu PC `python` abre la Microsoft Store (alias de Windows).
3. **`.gitignore`:** se añadió `nombre_entorno/`, porque el de la guía solo ignora `.venv/`, `venv/`, `env/` y `ENV/`.
4. **Sin `Set-ExecutionPolicy`:** ya estaba en `RemoteSigned`; además es una configuración de
   Windows que prefiero no modificar sin necesidad.
5. **Sin activar el prompt:** se llamó al Python del entorno por su ruta completa para
   no depender de la terminal activada.

## Lo que te queda por hacer

1. En VS Code, selecciona el intérprete `nombre_entorno` (Paso 4) y abre una terminal nueva
   (Terminal → New Terminal). Debe mostrar `(nombre_entorno)` al inicio.
2. Si trabajas con cuadernos `.ipynb`, instala la extensión **Jupyter** (`ms-toolsai.jupyter`) y
   acepta instalar `ipykernel` cuando VS Code lo pida.
3. Si no quieres ver más la advertencia de PATH de pip, añade
   `C:\Users\jorge\AppData\Local\Python\pythoncore-3.14-64\Scripts` a tu PATH de usuario
   (ver las instrucciones que te di antes). No afecta al venv.

## Archivos creados o modificados

| Archivo | Acción |
|---|---|
| `nombre_entorno\` | Creado (entorno virtual con las 8 librerías) |
| `.gitignore` | Creado |
| `requirements.txt` | Creado |
| `Documentacion_Clase01_Entorno_Python.md` | Este documento |

Además, en la sesión anterior se editó `%APPDATA%\Code\User\settings.json` para dejar Black Formatter
como formateador por defecto de Python con formateo al guardar.
