import "./TablaRentas.css";

const Tabla = ({rentas, editarRenta }) => {

   const handleedit = (renta) => {
      editarRenta(renta); 
   }
 
   
    return (
       <div className="table">
             <table>
                <thead>
                      <tr>
                           <th>Id </th>
                            <th>Id Cliente</th>
                            <th>Id Pelicula</th>
                            <th>Dias</th>
                            <th>Acciones</th>

                        

                      </tr>
                </thead>
                <tbody>
                  {rentas.map((renta) => (
                     
                      <tr key={renta.id}>
                        <td>{renta.id}</td>

                            <td>{renta.id_cliente}</td>
                            <td>{renta.id_pelicula}</td>
                            <td style={{ color: renta.dias < 0 ? 'red' : 'inherit' }}>{renta.dias}</td>

                           <td>
                               <button className="btn btn-secondary"  onClick={() => handleedit(renta)}>Editar</button>
                            
                             
                           </td>
                        </tr> 
                  ))}
                </tbody>
             </table>
         </div>
    );
    }

export default Tabla;
