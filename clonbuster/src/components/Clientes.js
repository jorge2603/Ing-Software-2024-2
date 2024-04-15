import React from "react";
import Form from "./Form_Clientes";
import Tabla from "./TablaClientes";
import { useState } from "react";


const Clientes = () => {
    const [clientes, setClientes] = useState([
        {
            id: 1,
            cliente: "Arthur",
            apellidopat: "Gomez",
            apellidomat: "Paredes",
            password: "123",
            email:"arthur@gmail.com",
            superuser: "1"
        },
        {
            id: 2,
            cliente: "Lucas",
            apellidopat: "Martinez",
            apellidomat: "Rosas",
            password: "321",
            email:"Lucas264@hotmaul.com",
            Usuario:"LucMart",
            superuser: "0"
          },
          {
            id: 3,
            cliente: "Sofia",
            apellidopat: "Gonzalez",
            apellidomat: "Gomez",
            password: "contrasena",
            email:"sofia536@gmail.com",
            superuser: "0"
            
          }

     ]);

     const [cliente_seleccionada, setClienteSeleccionada] = useState(null);
  
     const agregaClienteHandler = (cliente) => {
        setClientes((prevClientes) => {
           return [...prevClientes, { ...cliente }];
        });
     };

     const elminaClienteHandler = (clienteId) => {
        console.log(clienteId);
        const clientesFiltradas = clientes.filter(cliente => cliente.id !== clienteId);
        setClientes(clientesFiltradas);
        console.log(clientes);
     }

     const editarCliente = (clienteEditada) => {
        const clientesActualizadas = clientes.map(cliente => (cliente.id === clienteEditada.id ? clienteEditada : cliente));
        setClientes(clientesActualizadas);
        setClienteSeleccionada(null);
     }
  

    return (
        <div className="App">
            <h2>Clientes</h2>
            <Form 
            agregaClienteHandler={agregaClienteHandler}
            cliente_seleccionada={cliente_seleccionada}
            actualizar_cliente={editarCliente}/>
            <Tabla clientes={clientes} elminaClienteHandler={elminaClienteHandler} 
            editarCliente={(cliente)=>setClienteSeleccionada(cliente)}/>
        </div>
    );
}

export default Clientes;
