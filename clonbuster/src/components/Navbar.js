import {Link,Outlet} from "react-router-dom";

const Navbar = () => {
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <Link to="/" className="navbar-brand">Clonbuster</Link>
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav">
            <li className="nav-item active">
                <Link to="/" className="nav-link">Home</Link>
            </li>
            <li className="nav-item">
                <Link to="/peliculas" className="nav-link">Peliculas</Link>
            </li>
            <li className="nav-item">
                <Link to="/clientes" className="nav-link">Clientes</Link>
            </li>
            <li className="nav-item">
                <Link to="/rentas" className="nav-link">Rentas</Link>
            </li>
          </ul>
        </div>
      </nav>
    )
}

export default Navbar;