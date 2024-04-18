import React from 'react';
import {Link,Outlet,} from 'react-router-dom';

export const Navbar = () => {

	return (
		<>
			<header>
				<h1>
					<Link to='/'>HOME   </Link>
				</h1>

					<div className='user'>
						<span className='username'>     juanito     </span>
                        <Link to='/'>   Cerrar Sesión</Link>
					</div>

			</header>

			<Outlet />
		</>
	);
};