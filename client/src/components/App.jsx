import React, { useState } from "react";

function App() {
  // Estados para manejar los datos del formulario, la operación seleccionada y los resultados de la API
  const [primaryKey, setPrimaryKey] = useState("");
  const [secKey, setSecKey] = useState("");
  const [terKey, setTerKey] = useState("");
  const [fechaPrestamo, setFechaPrestamo] = useState("");
  const [fechaDevolucion, setFechaDevolucion] = useState("");
  const [año, setAño] = useState("");
  const [idioma, setIdioma] = useState("");
  const [numeroCopia, setNumeroCopia] = useState("");
  const [titulo, setTitulo] = useState("");
  const [operacion, setOperacion] = useState("insertar"); // Valor por defecto: insertar
  const [resultado, setResultado] = useState("");
  const [tabla, setTabla] = useState("Autor"); // Valor por defecto: usuarios
  // Función para enviar los datos del formulario y realizar operaciones CRUD en la API
  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      let method;
      let endpoint;
      let bodyData;

      switch (tabla) {
        case "Libro":
          endpoint = "libros";
          bodyData = { titulo: primaryKey };
          break;
        case "Autor":
          endpoint = "autores";
          bodyData = { nombre: primaryKey };
          break;
        case "Edicion":
          endpoint = "ediciones";
          bodyData = { isbn: primaryKey, año, idioma, numeroCopia, titulo };
          break;
        case "Autorea":
          endpoint = "autoreas";
          bodyData = { titulo: primaryKey, nombre: secKey };
          break;
        case "Copia":
          endpoint = "copias";
          bodyData = { isbn: primaryKey, numero: secKey };
          break;
        case "Usuario":
          endpoint = "usuarios";
          bodyData = { rut: primaryKey };
          break;
      }
      switch (operacion) {
        case "insertar":
          method = "POST";

          break;
        case "actualizar":
          method = "PUT";

          break;
        case "borrar":
          method = "DELETE";
          break;
        default:
          throw new Error("Operación no válida");
      }

      const response = await fetch(
        `https://tricky-saraann-cristhianac.koyeb.app/${endpoint}`,
        {
          method: method,
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(bodyData),
        }
      );

      if (!response.ok) {
        throw new Error(`Error al ${operacion} usuario`);
      }
    } catch (error) {
      setResultado(`Error: ${error.message}`);
    }
  };

  return (
    <div>
      <h1>Gestión de Biblioteca</h1>
      <form onSubmit={handleSubmit}>
        <label>Tabla:</label>
        <select value={tabla} onChange={(e) => setTabla(e.target.value)}>
          <option value="Libro">Libro</option>
          <option value="Autor">Autor</option>
          <option value="Edicion">Edicion</option>
          <option value="Autorea">Autorea</option>
          <option value="Copia">Copia</option>
          <option value="Usuario">Usuario</option>
          <option value="Prestamo">Prestamo</option>
        </select>
        <label>Operación:</label>
        <select
          value={operacion}
          onChange={(e) => setOperacion(e.target.value)}
        >
          <option value="insertar">Insertar</option>
          <option value="actualizar">Actualizar</option>
          <option value="borrar">Borrar</option>
        </select>

        {tabla === "Libro" && (
          <div>
            <label>Titulo</label>
            <input
              type="text"
              value={primaryKey}
              onChange={(e) => setPrimaryKey(e.target.value)}
              required
            />
          </div>
        )}
        {tabla === "Autor" && (
          <div>
            <label>Nombre</label>
            <input
              type="text"
              value={primaryKey}
              onChange={(e) => setPrimaryKey(e.target.value)}
              required
            />
          </div>
        )}

        {tabla === "Autorea" && (
          <div>
            <label>Titulo del libro</label>
            <input
              type="text"
              value={primaryKey}
              onChange={(e) => setPrimaryKey(e.target.value)}
              required
            />
            <label>Nombre del autor</label>
            <input
              type="text"
              value={secKey}
              onChange={(e) => setSecKey(e.target.value)}
              required
            />
          </div>
        )}

        {tabla === "Edicion" && operacion === "insertar" && (
          <div>
            <label>ISBN:</label>
            <input
              type="text"
              value={primaryKey}
              onChange={(e) => setPrimaryKey(e.target.value)}
              required
            />
            <label>Año:</label>
            <input
              type="text"
              value={año}
              onChange={(e) => setAño(e.target.value)}
              required
            />
            <label>Idioma:</label>
            <input
              type="text"
              value={idioma}
              onChange={(e) => setIdioma(e.target.value)}
              required
            />
            <label>Numero de copia:</label>
            <input
              type="text"
              value={numeroCopia}
              onChange={(e) => setNumeroCopia(e.target.value)}
              required
            />
            <label>Titulo:</label>
            <input
              type="text"
              value={titulo}
              onChange={(e) => setTitulo(e.target.value)}
              required
            />
          </div>
        )}

        {tabla === "Edicion" && operacion != "insertar" && (
          <div>
            <label>ISBN:</label>
            <input
              type="text"
              value={primaryKey}
              onChange={(e) => setPrimaryKey(e.target.value)}
              required
            />
          </div>
        )}

        {tabla === "Copia" && (
          <div>
            <label>ISBN: </label>
            <input
              type="text"
              value={primaryKey}
              onChange={(e) => setPrimaryKey(e.target.value)}
              required
            />
            <label>Numero: </label>
            <input
              type="text"
              value={secKey}
              onChange={(e) => setPrimaryKey(e.target.value)}
              required
            />
          </div>
        )}
        {tabla === "Prestamo" && operacion === "insertar" && (
          <div>
            <label>ISBN: </label>
            <input
              type="text"
              value={primaryKey}
              onChange={(e) => setPrimaryKey(e.target.value)}
              required
            />
            <label>Numero: </label>
            <input
              type="text"
              value={secKey}
              onChange={(e) => setPrimaryKey(e.target.value)}
              required
            />
            <label>Rut: </label>
            <input
              type="text"
              value={terKey}
              onChange={(e) => setTerKey(e.target.value)}
              required
            />
            <label>Fecha de prestamo: </label>
            <input
              type="text"
              value={fechaPrestamo}
              onChange={(e) => setFechaPrestamo(e.target.value)}
              required
            />
            <label>Fecha de devolucion: </label>
            <input
              type="text"
              value={fechaDevolucion}
              onChange={(e) => setFechaDevolucion(e.target.value)}
              required
            />
          </div>
        )}
        {tabla === "Prestamo" && operacion !== "insertar" && (
          <div>
            <label>ISBN: </label>
            <input
              type="text"
              value={primaryKey}
              onChange={(e) => setPrimaryKey(e.target.value)}
              required
            />
            <label>Numero: </label>
            <input
              type="text"
              value={secKey}
              onChange={(e) => setPrimaryKey(e.target.value)}
              required
            />
            <label>Rut: </label>
            <input
              type="text"
              value={terKey}
              onChange={(e) => setTerKey(e.target.value)}
              required
            />
          </div>
        )}
        {tabla === "Usuario" && operacion !== "insertar" && (
          <div>
            <label>Rut: </label>
            <input
              type="text"
              value={primaryKeyKey}
              onChange={(e) => setPrimaryKey(e.target.value)}
              required
            />
          </div>
        )}

        <button type="submit">
          {operacion === "insertar"
            ? "Insertar"
            : operacion === "actualizar"
            ? "Actualizar"
            : "Borrar"}{" "}
          {tabla}
        </button>
      </form>
      <div>{resultado}</div>
    </div>
  );
}

export default App;
