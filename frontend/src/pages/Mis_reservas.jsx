import {useState, useEffect} from 'react'
import React from 'react';
import './Table.css'; // Importar el archivo CSS para los estilos

const Table = () => {

    const [reservas, setReservas] = useState(null);

    const loadReservas = () => {
        fetch('http://127.0.0.1:8000/api/reservas', {
            method: 'GET',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
            },
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Success:', data);
            setReservas(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    };

    useEffect( () => {
        loadReservas();
    }, [] );

    if (!reservas) {
        return (
            <div> Loading... </div>
        );
    }
    
    return (
        <table className="styled-table">
            <thead>
                <tr>
                    <th>Tipo de Cancha</th>
                    <th>Fecha</th>
                    <th>Hora</th>
                </tr>
            </thead>
            <tbody>
                {reservas.map(reserva => (
                    //JSON.stringify(reserva)
                <tr>
                    <td>
                        Futbol
                    </td>
                    <td>
                        {reserva.fecha}
                    </td>
                    <td>
                        {reserva.bloq}
                    </td>
                </tr>
                ))}
            </tbody>
        </table>
    );
}

export default Table;
