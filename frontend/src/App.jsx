import React, { useState, useEffect } from 'react'

import Login from "./pages/Login";
import Canchas from "./pages/Canchas";
import Reserva from "./pages/Reserva";
import Home from "./pages/Home";
import Mis_reservas from "./pages/Mis_reservas";
import Reservas_admin from "./pages/Reservas_admin";
import Usuario from "./pages/Usuario";
import Registro from "./pages/Registro"
import Navbar from './Navbar';
import './index.css';
import { BrowserRouter, Route, Routes, Redirect } from "react-router-dom";
import { getToken } from './dataModel/Session';


function App() {
    const [sessionToken, setSessionToken] = useState( getToken() );

    useEffect( () => {
        const handleSessionToken = (e) => {
            const token = e.detail.token;
            if (token) setSessionToken(token)
            else setSessionToken(null)
        }
        
        document.addEventListener('session-token-update', handleSessionToken);
        return () => {
            document.removeEventListener('session-token-update', handleSessionToken);
        }
    }, [] );

    if (!sessionToken){
        return (
            <div className='flex flex-col w-full h-screen items-center'>
                <BrowserRouter>
                    <Routes>
                        <Route path='' element={<Login/>}/>
                        <Route path='/registro' element={<Registro/>}/>
                    </Routes>
                </BrowserRouter>
            </div>
        );
    }

    return (
        <div className='flex flex-col w-full h-screen items-center'>
            <BrowserRouter>
                <Navbar/>
                <Routes>
                    <Route path='' element={<Home/>}/>
                    <Route path='/canchas' element={<Canchas/>}/>
                    <Route path='/reserva' element={<Reserva/>}/>
                    <Route path='/login' element={<Login/>}/>
                    <Route path='/mis_reservas' element={<Mis_reservas/>}/>
                    <Route path='/reservas_admin' element={<Reservas_admin/>}/>
                    <Route path='/usuario' element={<Usuario/>}/>
                    <Route path='/registro' element={<Registro/>}/>
                </Routes>
            </BrowserRouter>
        </div>
    );
}

export default App;
