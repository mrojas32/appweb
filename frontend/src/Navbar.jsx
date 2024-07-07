import React from 'react';
import {Link,Outlet,} from 'react-router-dom';
import { resetSession } from './dataModel/Session';


const Navbar = () => {

	return (
    <>
        <div className='flex px-5 py-2 bg-white text-black mb-2 w-full justify-between'>
            <h1>
                <Link to='/'>HOME   </Link>
            </h1>

            <div className='flex gap-5'>
                <span>     juanito     </span>
                <Link onClick={resetSession} to='/'>   Cerrar Sesión</Link>
            </div>

        </div>
    </>
	);
};

export default Navbar;
