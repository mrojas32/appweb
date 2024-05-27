import { useEffect, useState } from "react";


function CanchasDesglose({recinto, id, nombre, tipo, ubicacion}){
    return(
        <canchita classname="pon color y diseño que quieras">
            <h3 classname="text-center pon color y diseño que quieras">{recinto}</h3>
            <p>ID_canchas: {id}</p>
            <p>Nombre: {nombre}</p>
            <p>Tipo: {tipo}</p>
            <p>Ubicacion: {ubicacion}</p>
        </canchita>
    )
}

export default function Canchas() {
    const [canchas, setCanchas] = useState([])

    const getCanchas = async () => {
        const allCanchas = await fetch('http://127.0.0.1:8000/api/canchas/')
        const canchasJson = await allCanchas.json()
        setCanchas(canchasJson)
    }
    useEffect(() => {
        getCanchas()
    })
    return (
    <main classname="pon color y diseño que quieras">
        <h1 classname="pon color y diseño que quieras">Canchas</h1>
        <div>
            {
                canchas.lenght == 0 ? "..." : canchas.map(cancha => (
                    <CanchasDesglose
                    sigla={recinto.id}
                    nombre={recinto.nombre}
                    tipo={recinto.tipo}
                    ubicacion={recinto.ubicacion}
                    />
                ))
            }
        </div>
    </main>
    )

}
