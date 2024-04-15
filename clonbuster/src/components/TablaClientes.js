import "./TablaClientes.css";

const Tabla = ({clientes,elminaClienteHandler, editarCliente }) => {

   const handleedit = (cliente) => {
      editarCliente(cliente); 
   }
 
   
    return (
       <div className="table">
             <table>
                <thead>
                      <tr>
                           <th>Id</th>
                         <th>Nombres</th>
                         <th>Apellido paterno</th>
                         <th>Apellido materno</th>
                           <th>contrasena</th>
                           <th>Correo</th>
                           <th>superusuario</th>
                           <th>Acciones</th>

                      </tr>
                </thead>
                <tbody>
                  {clientes.map((cliente) => (
                     
                      <tr key={cliente.id}>
                        <td>{cliente.id}</td>
                         <td>{cliente.cliente}</td>
                         <td>{cliente.apellidopat}</td>
                           <td>{cliente.apellidomat}</td>
                           <td>{cliente.password}</td>
                           <td>{cliente.email}</td>
                           <td>{cliente.superuser}</td>
                           <td>
                               <button className="btn btn-secondary"  onClick={() => handleedit(cliente)}>Editar</button>
                              <button className="btn btn-danger" onClick={elminaClienteHandler.bind(this, cliente.id)}>Eliminar</button>
                             
                           </td>
                        </tr> 
                  ))}
                </tbody>
             </table>
         </div>
    );
    }

export default Tabla;
