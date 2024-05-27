import React from 'react';
import {Link,Outlet,} from 'react-router-dom';

const Navbar = () => {

	return (
		<>
			<header style={{height:'.5em'}}>
				<h1>
					<Link to='/'>HOME   </Link>
				</h1>

					<div>
						<span>     juanito     </span>
                        <Link to='/'>   Cerrar Sesión</Link>
					</div>

			</header>
		</>
	);
};

export default Navbar;
