import React, { useEffect, useState } from 'react';
import './Form_Clientes.css';

const Form = ({ agregaClienteHandler,cliente_seleccionada,actualizar_cliente }) => {
    const [id, setId] = useState("");
    const [cliente, setCliente] = useState("");
    const [apellidopat, setApellidopat] = useState("");
    const [apellidomat, setApellidomat] = useState("");
    const [password, setPassword] = useState("");
    const [email, setEmail] = useState("");
    const [superuser, setSuperuser] = useState("");
    const [contador, setContador] = useState(4);
    useEffect(() => {
        if (cliente_seleccionada) {
            setId(cliente_seleccionada.id);
            setCliente(cliente_seleccionada.cliente);
            setApellidopat(cliente_seleccionada.apellidopat);
            setApellidomat(cliente_seleccionada.apellidomat);
            setPassword(cliente_seleccionada.password);
            setEmail(cliente_seleccionada.email);
            setSuperuser(cliente_seleccionada.superuser);
        }

    }, [cliente_seleccionada]);

    const handleSubmit = (e) => {
        e.preventDefault();

        if (!cliente.trim() || !apellidopat.trim() || !apellidomat.trim() || !password.trim() || !email.trim()){
            return;
        }
        const estado = superuser ? "1" : "0";

        const nuevaCliente = {
            id: id,
            cliente: cliente,
            apellidopat: apellidopat,
            apellidomat: apellidomat,
            password: password,
            email: email,
            superuser: estado

        }
       
       
        if (id){    
            actualizar_cliente(nuevaCliente);
        }else{
            setContador(contador + 1);
            nuevaCliente.id = contador;
            agregaClienteHandler(nuevaCliente);
        }

        setId("");
        setCliente("");
        setApellidopat("");
        setApellidomat("");
        setPassword("");
        setEmail("");
        setSuperuser("");


        
    }
    const cancelar=()=>{
        setId("");
        setCliente("");
        setApellidopat("");
        setApellidomat("");
        setPassword("");
        setEmail("");
        setSuperuser("");
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
                    value={cliente}
                    onChange={(event) => setCliente(event.target.value)}
                />
            </div>
            <div className="form-group">
                <label htmlFor="director">Apellido paterno</label>
                <input
                    type="text"
                    className="form-control"
                    id="director"
                    value={apellidopat}
                    onChange={(event) => setApellidopat(event.target.value)}
                />
            </div> <div className="form-group">
                <label htmlFor="director">Apellido materno</label>
                <input
                    type="text"
                    className="form-control"
                    id="director"
                    value={apellidomat}
                    onChange={(event) => setApellidomat(event.target.value)}
                />
            </div>
            <div className="form-group">
                <label htmlFor="anio">Password</label>
                <input
                    type="text"
                    className="form-control"
                    id="anio"
                    value={password}
                    onChange={(event) => setPassword(event.target.value)}
                />
            </div>
            <div className="form-group">
                <label htmlFor="anio">Email</label>
                <input
                    type="text"
                    className="form-control"
                    id="anio"
                    value={email}
                    onChange={(event) => setEmail(event.target.value)}
                />
            </div>
            <div className="form-group">
                <label htmlFor="anio">Superusuario</label>
                <input
                    type="checkbox"
                    className="form-check-input"
                    id="activo"
                    value={superuser}
                    onChange={(event) => setSuperuser(event.target.checked)}
                />
            </div>
            <button type="submit" className="btn btn-primary">{cliente_seleccionada ? "Actualizar" : "Agregar Usuario"}</button>
            <button className="btn btn-danger" onClick={cancelar}>cancelar</button>
            
        </form>
        </div>
    );
}

export default Form;
