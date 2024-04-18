import Login from "./pages/Login";
import Canchas from "./pages/Canchas";
import Reserva from "./pages/Reserva";
import Home from "./pages/Home";
import Mis_reservas from "./pages/Mis_reservas";
import Reservas_admin from "./pages/Reservas_admin";
import { BrowserRouter, Route, Routes } from "react-router-dom";


function App() {
  return (
    <div className='flex flex-col w-full h-screen items-center p-3'>
    <BrowserRouter>
        <Routes>
            <Route path='' element={<Home/>}/>
            <Route path='/canchas' element={<Canchas/>}/>
            <Route path='/reserva' element={<Reserva/>}/>
            <Route path='/login' element={<Login/>}/>
            <Route path='/mis_reservas' element={<Mis_reservas/>}/>
		        <Route path='/reservas_admin' element={<Reservas_admin/>}/>
        </Routes>
    </BrowserRouter>
    </div>
  );
}

export default App;
