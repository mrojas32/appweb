import { Button } from "@mui/material"
import { Link } from "react-router-dom";

export default function Home() {
    
    return (
        <div className='flex flex-col gap-3 items-start'>
            <Link to='/login'>
                Login
            </Link>
            <Link to='/canchas'>
                Canchas
            </Link>
        </div>
    );
}
