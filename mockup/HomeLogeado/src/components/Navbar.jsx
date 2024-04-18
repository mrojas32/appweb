import { NavLink } from "react-router-dom";

const Navbar = () => { 
    return (
        <nav className="navbar navbar-dark bg-dark">
            <div className="container">
                <NavLink to="/" className="btn btn-outline-primary">NombreUsuarioLoggeado</NavLink>
                <NavLink to="/Reservar" className="btn btn-outline-primary">Reservas</NavLink>
            </div>
        </nav>
    );
};

export default Navbar;