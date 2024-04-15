import React, { useEffect, useState } from 'react';
import './Form_Rentas.css';

const Form = ({ agregaRentaHandler,renta_seleccionada,actualizar_renta }) => {
    const [id, setId] = useState("");
    const [id_cliente, setId_cliente] = useState("");
    const [id_pelicula, setId_pelicula] = useState("");
    const [dias, setDias] = useState("");
    const [contador, setContador] = useState(4);
    useEffect(() => {
        if (renta_seleccionada) {
            setId(renta_seleccionada.id);
            setId_cliente(renta_seleccionada.id_cliente);
            setId_pelicula(renta_seleccionada.id_pelicula);
            setDias(renta_seleccionada.dias);
        }

    }, [renta_seleccionada]);

    const handleSubmit = (e) => {
        e.preventDefault();

        if (!id_cliente.trim() || !id_pelicula.trim()){
            return;
        }

        const nuevaRenta = {
            id: id,
            id_cliente: id_cliente,
            id_pelicula: id_pelicula,
            dias: 5

        }
       
       
        if (id){    
            actualizar_renta(nuevaRenta);
        }else{
            setContador(contador + 1);
            nuevaRenta.id = contador;
            agregaRentaHandler(nuevaRenta);
        }

        setId("");
        setId_cliente("");
        setId_pelicula("");
        setDias("");



        
    }
    const cancelar=()=>{
        setId("");
        setId_cliente("");
        setId_pelicula("");
        setDias("");

    }
   
    return (
        <div className="contenedor">
        <form onSubmit={handleSubmit}>
            <div className="form-group">
                <label htmlFor="nombre">Id del cliente</label>
                <input
                    type="text"
                    className="form-control"
                    id="nombre"
                    value={id_cliente}
                    onChange={(event) => setId_cliente(event.target.value)}
                    disabled={renta_seleccionada ? true : false}
                />
            </div>
            <div className="form-group">
                <label htmlFor="genero">Id de la pelicula</label>
                <input
                    type="text"
                    className="form-control"
                    id="genero"
                    value={id_pelicula}
                    onChange={(event) => setId_pelicula(event.target.value)}
                    disabled={renta_seleccionada ? true : false}
                />
            </div>
            <div className="form-group">
                <label htmlFor="dias">Dias</label>
                <input
                    type="text"
                    className="form-control"
                    id="dias"
                    value={dias}
                    onChange={(event) => setDias(event.target.value)}
                    disabled={renta_seleccionada ? false : true}
                />
            </div>
            <button type="submit" className="btn btn-primary">{renta_seleccionada ? "Actualizar" : "Agregar Usuario"}</button>
            <button className="btn btn-danger" onClick={cancelar}>cancelar</button>
            
        </form>
        </div>
    );
}

export default Form;
