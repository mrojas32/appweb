import { NavLink } from "react-router-dom";

const Navbar = () => { 
    return (
        <nav className="navbar navbar-dark bg-dark">
            <div className="container">
                <NavLink to="/" className="btn btn-outline-primary">HomeAdmin</NavLink>
                <NavLink to="/Reportes" className="btn btn-outline-primary">Reportes y Estadísticas</NavLink>
                <NavLink to="/Gestion" className="btn btn-outline-primary">Gestión Reservas</NavLink>
            </div>
        </nav>
    );
};

export default Navbar;