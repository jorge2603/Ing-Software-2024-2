import './App.css';
import Peliculas from "./components/Peliculas";
import {BrowserRouter as Router, Route, Routes,Outlet} from "react-router-dom";
import Navbar from './components/Navbar';
import Clientes from './components/Clientes';
import Rentas from './components/Rentas';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar/>
        <Routes>
          <Route path="/" element={<Outlet/>}/>
          <Route path="peliculas" element={<Peliculas/>}/>
          <Route path="clientes" element={<Clientes/>}/>
          <Route path="rentas" element={<Rentas/>}/>

        </Routes>
      </div>
    </Router>

    // <div className="App">
    //   <h1>Clonbuster</h1>
    //   <Peliculas/>
    // </div>
  );
}

export default App;
