import React from "react";
import Form from "./Form_Peliculas";
import Tabla from "./TablaPeliculas";
import { useState } from "react";
import "./Peliculas.css";


const Peliculas = () => {
    const [peliculas, setPeliculas] = useState([
        {
           id: 1,
           nombre: "El padrino",
           genero: "Drama",
           duracion: "175 minutos",
           inventario: "5",
        },
        {
           id: 2,
           nombre: "El padrino II",
             genero: "Drama",
             duracion: "202 minutos",
               inventario: "10",

           
        },
        {
           id: 3,
           nombre: "El padrino III",
             genero: "Drama",
               duracion: "162 minutos",
                  inventario: "2",

           
        },
     ]);

     const [pelicula_seleccionada, setPeliculaSeleccionada] = useState(null);
  
     const agregaPeliculaHandler = (pelicula) => {
        setPeliculas((prevPeliculas) => {
           return [...prevPeliculas, { ...pelicula }];
        });
     };

     const elminaPeliculaHandler = (peliculaId) => {
        console.log(peliculaId);
        const peliculasFiltradas = peliculas.filter(pelicula => pelicula.id !== peliculaId);
        setPeliculas(peliculasFiltradas);
        console.log(peliculas);
     }

     const editarPelicula = (peliculaEditada) => {
        const peliculasActualizadas = peliculas.map(pelicula => (pelicula.id === peliculaEditada.id ? peliculaEditada : pelicula));
        setPeliculas(peliculasActualizadas);
        setPeliculaSeleccionada(null);
     }
  

    return (
        <div className="App">
            <h2>Peliculas</h2>
            <Form 
            agregaPeliculaHandler={agregaPeliculaHandler}
            pelicula_seleccionada={pelicula_seleccionada}
            actualizar_pelicula={editarPelicula}/>
            <div className="tablacontainer">
            <Tabla peliculas={peliculas} elminaPeliculaHandler={elminaPeliculaHandler} 
            editarPelicula={(pelicula)=>setPeliculaSeleccionada(pelicula)}/>
            </div>
        </div>
    );
}

export default Peliculas;
