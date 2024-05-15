import React, { useEffect, useState } from "react";
import { Button } from "@fluentui/react";

function App() {
  // Estados para manejar los datos del formulario, la operación seleccionada y los resultados de la API
  const [primaryKey, setPrimaryKey] = useState("");
  const [objetivo, setObjetivo] = useState("");
  const [objetivo2, setObjetivo2] = useState("");
  const [secKey, setSecKey] = useState("");
  const [terKey, setTerKey] = useState("");
  const [fechaPrestamo, setFechaPrestamo] = useState("");
  const [fechaDevolucion, setFechaDevolucion] = useState("");
  const [query, setQuery] = useState("Query1");
  const [año, setAño] = useState("");
  const [idioma, setIdioma] = useState("");
  const [numeroCopia, setNumeroCopia] = useState("");
  const [titulo, setTitulo] = useState("");
  const [operacion, setOperacion] = useState("insertar"); // Valor por defecto: insertar
  const [resultado, setResultado] = useState("");
  const [tabla, setTabla] = useState("Autor"); // Valor por defecto: usuarios
  const [RUTQ, setRUTQ] = useState("");
  const [response2R, setResponse2R] = useState("");
  // Función para enviar los datos del formulario y realizar operaciones CRUD en la API
  useEffect(() => {
    setResponse2R("");
    setRUTQ("");
  }, [query]);
  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      let method;
      let endpoint;
      let bodyData;

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
      switch (tabla) {
        case "Libro":
          bodyData = { titulo: primaryKey };
          if (operacion === "insertar") {
            endpoint = "libros";
          } else {
            endpoint = "libros/" + objetivo;
          }
          break;
        case "Autor":
          bodyData = { nombre: primaryKey };
          if (operacion === "insertar") {
            endpoint = "autores";
          } else {
            endpoint = "autores/" + objetivo;
          }
          break;
        case "Edicion":
          bodyData = { ISBN: primaryKey, año, idioma, numeroCopia, titulo };
          if (operacion === "insertar") {
            endpoint = "ediciones";
          } else {
            endpoint = "ediciones/" + objetivo;
          }

          break;
        case "Autorea":
          bodyData = { tituloLibro: primaryKey, autorNombre: secKey };
          if (operacion === "insertar") {
            endpoint = "autoreas";
          } else {
            endpoint = "autoreas" + objetivo + "/" + objetivo2;
          }

          break;
        case "Copia":
          bodyData = { ISBN: primaryKey, numero: secKey };
          if (operacion === "insertar") {
            endpoint = "copias";
          } else {
            endpoint = "copias/" + objetivo2 + "/" + objetivo;
          }
          break;
        case "Usuario":
          bodyData = { RUT: primaryKey, nombre: secKey };
          if (operacion === "insertar") {
            endpoint = "usuarios";
          } else {
            endpoint = "usuarios/" + objetivo;
          }

          break;
        case "Prestamo":
          bodyData = {
            ISBN: primaryKey,
            numeroCopia: secKey,
            RUT: terKey,
            fechaPrestamo: fechaPrestamo,
            fechaDevolucion: fechaDevolucion,
          };
          if (operacion === "insertar") {
            endpoint = "prestamos";
          } else {
            endpoint = "prestamos/" + objetivo + "/" + objetivo2;
          }

          break;
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
      setResultado(`Operación ${operacion} realizada con éxito`);
      if (!response.ok) {
        throw new Error(`Error al ${operacion}`);
      }
    } catch (error) {
      setResultado(`Error: ${error.message}`);
    }
  };
  const handleSubmitQuerys = async (event) => {
    event.preventDefault();
    let endpoint2;
    if (query === "Query1") {
      endpoint2 = "Query1";
    } else if (query === "Query2") {
      endpoint2 = "Query2/" + RUTQ;
    }
    try {
      const response2 = await fetch(
        `https://tricky-saraann-cristhianac.koyeb.app/${endpoint2}`,
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      if (!response2.ok) {
        throw new Error(`Error ${response2.status} al realizar la petición.`);
      }

      const responseData = await response2.json();
      setResponse2R(responseData);
      console.log(responseData);
    } catch (error) {
      console.error("Error al procesar la solicitud:", error);
    }
  };
  return (
    <div className=" flex flex-col justify-center gap-10 bg-slate-400 p-9 rounded-2xl shadow-2xl  shadow-black/50 animate-blurred-fade-in ">
      <h1 className="w-full text-center">Gestión de Biblioteca</h1>
      <form
        onSubmit={handleSubmit}
        className="flex flex-col justify-between content-between gap-2"
      >
        <div className="gap-2 flex">
          <label>Tabla:</label>
          <select
            value={tabla}
            onChange={(e) => setTabla(e.target.value)}
            className=" rounded-lg"
          >
            <option value="Libro">Libro</option>
            <option value="Autor">Autor</option>
            <option value="Edicion">Edicion</option>
            <option value="Autorea">Autorea</option>
            <option value="Copia">Copia</option>
            <option value="Usuario">Usuario</option>
            <option value="Prestamo">Prestamo</option>
          </select>
        </div>
        <div className="gap-2 flex">
          <label>Operación:</label>
          <select
            value={operacion}
            onChange={(e) => setOperacion(e.target.value)}
            className=" rounded-lg"
          >
            <option value="insertar">Insertar</option>
            <option value="actualizar">Actualizar</option>
            <option value="borrar">Borrar</option>
          </select>
        </div>
        {tabla === "Libro" && (
          <div className=" flex flex-row content-between gap-6 justify-between">
            {operacion !== "insertar" && (
              <input
                className=" border border-gray-400 rounded p-1"
                type="text"
                placeholder="Titulo del libro objetivo"
                value={objetivo}
                onChange={(e) => setObjetivo(e.target.value)}
                required
              ></input>
            )}
            {operacion !== "borrar" && (
              <div className=" gap-3 flex flex-row">
                <label className="mr-5">Titulo:</label>
                <input
                  className=" border border-gray-400 rounded p-1"
                  type="text"
                  value={primaryKey}
                  onChange={(e) => setPrimaryKey(e.target.value)}
                  required
                />
              </div>
            )}
          </div>
        )}
        {tabla === "Autor" && (
          <div className=" flex flex-row content-between gap-6 justify-between">
            {operacion !== "insertar" && (
              <input
                className=" border border-gray-400 rounded p-1"
                type="text"
                placeholder="Nombre del Autor objetivo"
                value={objetivo}
                onChange={(e) => setObjetivo(e.target.value)}
                required
              ></input>
            )}
            {operacion !== "borrar" && (
              <div className=" gap-3 flex flex-row">
                <label className="mr-5">nombre del Autor:</label>
                <input
                  className=" border border-gray-400 rounded p-1"
                  type="text"
                  value={primaryKey}
                  onChange={(e) => setPrimaryKey(e.target.value)}
                  required
                />
              </div>
            )}
          </div>
        )}

        {tabla === "Autorea" && (
          <div className=" flex flex-col gap-2">
            {operacion !== "insertar" && (
              <input
                type="text"
                placeholder="titulo del libro objetivo"
                value={objetivo}
                onChange={(e) => setObjetivo(e.target.value)}
                required
                className=" border border-gray-400 rounded p-1"
              ></input>
            )}

            {operacion !== "insertar" && (
              <input
                type="text"
                placeholder="Nombre del autor objetivo"
                value={objetivo2}
                onChange={(e) => setObjetivo2(e.target.value)}
                required
                className=" border border-gray-400 rounded p-1"
              ></input>
            )}
            {operacion !== "borrar" && (
              <div>
                <div className=" flex gap-4">
                  <label>Titulo del libro:</label>
                  <input
                    type="text"
                    value={primaryKey}
                    onChange={(e) => setPrimaryKey(e.target.value)}
                    required
                    className=" border border-gray-400 rounded p-1"
                  />
                </div>
                <div className=" flex gap-4">
                  <label>Nombre del autor:</label>
                  <input
                    type="text"
                    value={secKey}
                    onChange={(e) => setSecKey(e.target.value)}
                    required
                    className=" border border-gray-400 rounded p-1"
                  />
                </div>
              </div>
            )}
          </div>
        )}

        {tabla === "Edicion" && (
          <div className=" flex flex-col gap-2">
            {operacion !== "insertar" && (
              <input
                type="text"
                placeholder="ISBN del objetivo"
                value={objetivo}
                onChange={(e) => setObjetivo(e.target.value)}
                required
                className=" border border-gray-400 rounded p-1"
              ></input>
            )}
            {operacion !== "borrar" && (
              <div>
                <div className=" flex gap-2">
                  <label>ISBN:</label>
                  <input
                    type="text"
                    value={primaryKey}
                    onChange={(e) => setPrimaryKey(e.target.value)}
                    required
                    className=" border border-gray-400 rounded p-1"
                  />
                </div>
                <div className=" flex gap-2">
                  <label>Año:</label>
                  <input
                    type="text"
                    value={año}
                    onChange={(e) => setAño(e.target.value)}
                    required
                    className=" border border-gray-400 rounded p-1"
                  />
                </div>
                <div className=" flex gap-2">
                  <label>Idioma:</label>
                  <input
                    type="text"
                    value={idioma}
                    onChange={(e) => setIdioma(e.target.value)}
                    required
                    className=" border border-gray-400 rounded p-1"
                  />
                </div>
                <div className=" flex gap-2">
                  <label>Numero de copia:</label>
                  <input
                    type="text"
                    value={numeroCopia}
                    onChange={(e) => setNumeroCopia(e.target.value)}
                    required
                    className=" border border-gray-400 rounded p-1"
                  />
                </div>
                <div className=" flex gap-2">
                  <label>Titulo:</label>
                  <input
                    type="text"
                    value={titulo}
                    onChange={(e) => setTitulo(e.target.value)}
                    required
                    className=" border border-gray-400 rounded p-1"
                  />
                </div>
              </div>
            )}
          </div>
        )}

        {tabla === "Copia" && (
          <div className="flex flex-col gap-2">
            {operacion !== "insertar" && (
              <input
                type="text"
                placeholder="ISBN del objetivo"
                value={objetivo}
                onChange={(e) => setObjetivo(e.target.value)}
                required
                className=" border border-gray-400 rounded p-1"
              ></input>
            )}

            {operacion !== "insertar" && (
              <input
                type="text"
                placeholder="Numero del objetivo"
                value={objetivo2}
                onChange={(e) => setObjetivo2(e.target.value)}
                required
                className=" border border-gray-400 rounded p-1"
              ></input>
            )}
            {operacion !== "borrar" && (
              <div>
                <div className=" flex gap-2">
                  <label>ISBN: </label>
                  <input
                    type="text"
                    value={primaryKey}
                    onChange={(e) => setPrimaryKey(e.target.value)}
                    required
                    className=" border border-gray-400 rounded p-1"
                  />
                </div>
                <div className=" flex gap-2">
                  <label>Numero: </label>
                  <input
                    type="text"
                    value={secKey}
                    onChange={(e) => setSecKey(e.target.value)}
                    required
                    className=" border border-gray-400 rounded p-1"
                  />
                </div>
              </div>
            )}
          </div>
        )}

        {tabla === "Prestamo" && (
          <div className=" flex gap-2 flex-col">
            {operacion !== "insertar" && (
              <div>
                <input
                  type="text"
                  placeholder="ISBN del objetivo"
                  value={objetivo}
                  onChange={(e) => setObjetivo(e.target.value)}
                  required
                  className=" border border-gray-400 rounded p-1"
                ></input>
                <input
                  type="text"
                  placeholder="Numero del objetivo"
                  value={objetivo2}
                  onChange={(e) => setObjetivo2(e.target.value)}
                  required
                  className=" border border-gray-400 rounded p-1"
                />
              </div>
            )}
            {operacion !== "borrar" && (
              <div>
                <div>
                  <label>ISBN: </label>
                  <input
                    type="text"
                    value={primaryKey}
                    onChange={(e) => setPrimaryKey(e.target.value)}
                    required
                    className=" border border-gray-400 rounded p-1"
                  />
                </div>
                <div>
                  <label>Numero: </label>
                  <input
                    type="text"
                    value={secKey}
                    onChange={(e) => setSecKey(e.target.value)}
                    required
                    className=" border border-gray-400 rounded p-1"
                  />
                </div>
                <div>
                  <label>Rut: </label>
                  <input
                    type="text"
                    value={terKey}
                    onChange={(e) => setTerKey(e.target.value)}
                    required
                    className=" border border-gray-400 rounded p-1"
                  />
                </div>
                <div>
                  <label>Fecha de prestamo: </label>
                  <input
                    type="text"
                    value={fechaPrestamo}
                    onChange={(e) => setFechaPrestamo(e.target.value)}
                    required
                    className=" border border-gray-400 rounded p-1"
                  />
                </div>
                <div>
                  <label>Fecha de devolucion: </label>
                  <input
                    type="text"
                    value={fechaDevolucion}
                    onChange={(e) => setFechaDevolucion(e.target.value)}
                    required
                    className=" border border-gray-400 rounded p-1"
                  />
                </div>
              </div>
            )}
          </div>
        )}

        {tabla === "Usuario" && (
          <div className=" flex gap-2 ">
            {operacion !== "insertar" && (
              <input
                type="text"
                placeholder="Llave Primaria del objetivo"
                value={objetivo}
                onChange={(e) => setObjetivo(e.target.value)}
                required
                className=" border border-gray-400 rounded p-1"
              ></input>
            )}
            {operacion !== "borrar" && (
              <div>
                <label>Rut: </label>
                <input
                  type="text"
                  value={primaryKey}
                  onChange={(e) => setPrimaryKey(e.target.value)}
                  required
                  className=" border border-gray-400 rounded p-1"
                />
                <label>Nombre: </label>
                <input
                  type="text"
                  value={secKey}
                  onChange={(e) => setSecKey(e.target.value)}
                  required
                  className=" border border-gray-400 rounded p-1"
                ></input>
              </div>
            )}
          </div>
        )}

        <Button type="submit">
          {operacion === "insertar"
            ? "Insertar"
            : operacion === "actualizar"
            ? "Actualizar"
            : "Borrar"}{" "}
          {tabla}
        </Button>
        <div>{resultado}</div>
      </form>
      <div></div>
      <form
        onSubmit={handleSubmitQuerys}
        className="flex flex-col justify-between content-between gap-2"
      >
        <div className="gap-2 flex flex-col">
          <label className=" w-full text-center">Solicitud:</label>
          <select
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            className=" rounded-lg"
          >
            <option value="Query1">Ver Copias de Libros</option>
            <option value="Query2">Ver Prestamos de un Usuario</option>
          </select>
          {query === "Query2" && (
            <div
              className=" flex gap-2
              "
            >
              <label>Rut: </label>
              <input
                type="text"
                value={RUTQ}
                onChange={(e) => setRUTQ(e.target.value)}
                required
                className=" border border-gray-400 rounded p-1"
              />
            </div>
          )}
          <Button type="submit">Realizar Solicitud</Button>
        </div>

        <div>
          {response2R &&
            query === "Query1" &&
            response2R.map((item) => (
              <div key={item.titulo}>
                <h2>{item.titulo}</h2>

                <p>Numero: {item.copia.numero}</p>
                <p>ISBN: {item.edicion.ISBN}</p>
                <p>año: {item.edicion.año}</p>
                <p>idioma: {item.edicion.idioma}</p>
              </div>
            ))}
        </div>

        {response2R && query === "Query2" && (
          <h2>Los libros prestados por el usario con el RUT {RUTQ} son: </h2>
        )}
        {response2R &&
          query === "Query2" &&
          response2R.map((item) => (
            <div key={item.titulo}>
              <h2>{item.titulo}</h2>
            </div>
          ))}
      </form>
    </div>
  );
}

export default App;
