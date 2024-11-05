# Proyecto Flask con MongoDB

Este proyecto es una aplicación Flask que utiliza una base de datos MongoDB. A continuación se describen los pasos necesarios para configurar el entorno y ejecutar la aplicación.

## Requisitos previos
- Tener instalado **Docker** y **Docker Compose** en tu sistema.
- Tener **Python 3** instalado.

## Pasos de configuración

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/Efigas-S-A/mongorupture.git
   cd mongorupture
   ```

Asegúrate de tener Docker y Docker Compose instalados para levantar el servicio de MongoDB.

2. Asegúrate de tener una carpeta llamada ./mongo_data en el mismo nivel que el archivo docker-compose.yml. Esta carpeta se usará para la persistencia de los datos de MongoDB.

3. Levanta la base de datos ejecutando:
  ```bash
    docker-compose up -d
   ```

4. Crea un entorno virtual para instalar las dependencias de Python:
  ```bash
     python3 -m venv venv
  ```
5. En Linux/MacOS:

   ```bash
   source venv/bin/activate
   ```

6. En Windows

   ```bash
    .\venv\Scripts\activate
   ```

7. Con el entorno virtual activado, instala las dependencias desde el archivo requirements.txt:

   ```bash
      pip install -r requirements.txt
   ```

8. Antes de iniciar la aplicación, ejecuta los siguientes scripts para preparar los datos de eventos y usuarios en la base de datos:

   ```bash
      python rupture/models/eventos.py
      python rupture/models/users.py
   ```
9. Finalmente, ejecuta la aplicación Flask:
   ```bash
      python rupture/main.py
   ```

Notas adicionales
Asegúrate de que el contenedor de MongoDB esté corriendo correctamente antes de ejecutar los scripts y la aplicación Flask.



Autor
<Juan Sebastian Mendez> ```

