import { useEffect, useState } from "react";


function CanchasDesglose({id, nombre, tipo, ubicacion}){
    return(
        <tr>
            <td> {id} </td>
            <td> {nombre} </td>
            <td> {tipo} </td>
            <td> {ubicacion} </td>
        </tr>
    )
}

export default function Canchas() {
    const [canchas, setCanchas] = useState([])

    const getCanchas = async () => {
        const allCanchas = await fetch('http://127.0.0.1:8000/api/canchas/')
        const canchasJson = await allCanchas.json()
        console.log(canchasJson);
        setCanchas(canchasJson)
    }
    useEffect(() => {
        getCanchas()
    }, []);
    return (
    <main classname="pon color y diseño que quieras">
        <h1 classname="pon color y diseño que quieras">Canchas</h1>
        <table>
            <thead>
                <tr>
                    <th> id </th>
                    <th> nombre </th>
                    <th> tipo </th>
                    <th> ubicacion </th>
                </tr>
            </thead>
            <tbody>
                {
                    canchas.lenght === 0 ? "..." : canchas.map(cancha => (
                        <CanchasDesglose
                        id={cancha.ID_canchas}
                        nombre={cancha.nombre}
                        tipo={cancha.tipo}
                        ubicacion={cancha.ubicacion}
                        />
                    ))
                }
            </tbody>
        </table>
    </main>
    )

}
