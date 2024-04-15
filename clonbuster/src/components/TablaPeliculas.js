

import "./TablaPeliculas.css";

const Tabla = ({peliculas,elminaPeliculaHandler, editarPelicula }) => {

   const handleedit = (pelicula) => {
      editarPelicula(pelicula); 
   }
 
   
    return (
       <div className="table">
             <table>
                <thead>
                      <tr>
                           <th>Id</th>
                         <th>Nombre</th>
                         <th>Genero</th>
                           <th>Duracion</th>
                           <th>Inventario</th>
                           <th>Acciones</th>
                      </tr>
                </thead>
                <tbody>
                  {peliculas.map((pelicula) => (
                     
                      <tr key={pelicula.id}>
                        <td>{pelicula.id}</td>
                         <td>{pelicula.nombre}</td>
                         <td>{pelicula.genero}</td>
                           <td>{pelicula.duracion}</td>
                           <td>{pelicula.inventario}</td>
                           <td>
                               <button className="btn btn-secondary"  onClick={() => handleedit(pelicula)}>Editar</button>
                              <button className="btn btn-danger" onClick={elminaPeliculaHandler.bind(this, pelicula.id)}>Eliminar</button>
                             
                           </td>
                        </tr> 
                  ))}
                </tbody>
             </table>
         </div>
    );
    }

export default Tabla;
