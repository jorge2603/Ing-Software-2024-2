import React, { useEffect, useState } from 'react';
import './Form_Peliculas.css';

const Form = ({ agregaPeliculaHandler,pelicula_seleccionada,actualizar_pelicula }) => {
    const [id, setId] = useState("");
    const [pelicula, setPelicula] = useState("");
    const [genero, setGenero] = useState("");
    const [duracion, setDuracion] = useState("");
    const [inventario, setInventario] = useState("");
    const [contador, setContador] = useState(4);

    useEffect(() => {
        if (pelicula_seleccionada) {
            setId(pelicula_seleccionada.id);
            setPelicula(pelicula_seleccionada.nombre);
            setGenero(pelicula_seleccionada.genero);
            setDuracion(pelicula_seleccionada.duracion);
            setInventario(pelicula_seleccionada.inventario);
        }

    }, [pelicula_seleccionada]);

    const handleSubmit = (e) => {
        e.preventDefault();

        if (!pelicula.trim() || !genero.trim() || !duracion.trim() || !inventario.trim()) {
            return;
        }

        const nuevaPelicula = {
            id: id,
            nombre: pelicula,
            genero: genero,
            duracion: duracion,
            inventario: inventario
        }
       
       
        if (id){    
            actualizar_pelicula(nuevaPelicula);
        }else{
            setContador(contador + 1);
            nuevaPelicula.id = contador;
            agregaPeliculaHandler(nuevaPelicula);
        }

        setId("");
        setPelicula("");
        setGenero("");
        setDuracion("");
        setInventario("");

        
    }
    const cancelar=()=>{
        setId("");
        setPelicula("");
        setGenero("");
        setDuracion("");
        setInventario("");
    }
   
    return (
        <div className="contenedor">
        <form onSubmit={handleSubmit}>
            <div className="form-group">
                <label htmlFor="nombre">Nombre</label>
                <input
                    type="text"
                    className="form-control"
                    id="nombre"
                    value={pelicula}
                    onChange={(event) => setPelicula(event.target.value)}
                />
            </div>
            <div className="form-group">
                <label htmlFor="genero">Genero</label>
                <input
                    type="text"
                    className="form-control"
                    id="genero"
                    value={genero}
                    onChange={(event) => setGenero(event.target.value)}
                /> 
            </div>
            <div className="form-group">
                <label htmlFor="duracion">Duración</label>
                <input
                    type="text"
                    className="form-control"
                    id="duracion"
                    value={duracion}
                    onChange={(event) => setDuracion(event.target.value)}
                />
            </div>
            <div className="form-group">
                <label htmlFor="inventario">Inventario</label>
                <input
                    type="text"
                    className="form-control"
                    id="inventario"
                    value={inventario}
                    onChange={(event) => setInventario(event.target.value)}
                />
            </div>

            <button type="submit" className="btn btn-primary">{pelicula_seleccionada ? "Actualizar" : "Agregar Película"}</button>
            <button className="btn btn-danger" onClick={cancelar}>cancelar</button>
            
        </form>
        </div>
    );
}

export default Form;
