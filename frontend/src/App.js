import Login from "./pages/Login";
import Canchas from "./pages/Canchas";
import Reserva from "./pages/Reserva";
import Home from "./pages/Home";
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
        </Routes>
    </BrowserRouter>
    </div>
  );
}

export default App;
