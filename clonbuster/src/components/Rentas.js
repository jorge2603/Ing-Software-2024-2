import React from "react";
import Form from "./Form_Rentas";
import Tabla from "./TablaRentas";
import { useState } from "react";
import "./Rentas.css";


const Rentas = () => {
    const [rentas, setRentas] = useState([
        {
           id: 1,
           id_cliente: "1",
           id_pelicula: "1",
            
            dias: "5",
        },
        {
           id: 2,
           id_cliente: "2",
              id_pelicula: "4",
                
                dias: "3",
           
        },
        {
           id: 3,
              id_cliente: "7",
                  id_pelicula: "18",
                 
                    dias: "-1",

           
        },
     ]);

     const [renta_seleccionada, setRentaSeleccionada] = useState(null);
  
     const agregaRentaHandler = (renta) => {
        setRentas((prevRentas) => {
           return [...prevRentas, { ...renta }];
        });
     };

     const editarRenta = (rentaEditada) => {
        const rentasActualizadas = rentas.map(renta => (renta.id === rentaEditada.id ? rentaEditada : renta));
        setRentas(rentasActualizadas);
        setRentaSeleccionada(null);
     }
  

    return (
        <div className="App">
            <h2>Rentas</h2>
            <Form 
            agregaRentaHandler={agregaRentaHandler}
            renta_seleccionada={renta_seleccionada}
            actualizar_renta={editarRenta}/>
            <div className="tablacontainer">
            <Tabla rentas={rentas}
            editarRenta={(renta)=>setRentaSeleccionada(renta)}/>
            </div>
        </div>
    );
}

export default Rentas;
