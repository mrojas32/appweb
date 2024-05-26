import { Button } from "@mui/material"
import { Link } from "react-router-dom";

export default function Home() {
    
    return (
        <div className='flex flex-col gap-3 items-start'>
            <Link to='/login'>
                Login
            </Link>
            <Link to='/registro'>
                Registro
            </Link>
            <Link to='/usuario'>
                Usuario
            </Link>
            <Link to='/canchas'>
                Canchas
            </Link>
            <Link to='/reserva'>
                Reserva
            </Link>
            <Link to='/mis_reservas'>
                Mis Reservas
            </Link>
            <Link to='/reservas_admin'>
                Administrador de reservas
            </Link>
        </div>
    );
}
