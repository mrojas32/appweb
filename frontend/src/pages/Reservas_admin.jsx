import DataTable from "react-data-table-component";
import {useState, useEffect} from 'react'
import React from 'react';
import './Table.css'; // Importar el archivo CSS para los estilos

class Table extends React.Component {
  render() {

    const deleteRow = event => {
      const row = event.target.closest('tr');
      row.remove();
    };

    return (
    <table className="styled-table">
        <thead>
          <tr>
            <th>Usuario</th>
            <th>ID_reserva</th>
            <th>Fecha</th>
            <th>Hora</th>
            <th>Acción</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Usuario 1</td>
            <td>1</td>
            <td>18-04-24</td>
            <td>9:35 - 10_45</td>
            <td><button onClick={deleteRow}>Cancelar Reserva</button></td>
          </tr>
          <tr>
            <td>Usuario 2</td>
            <td>2</td>
            <td>19-04-24</td>
            <td>12.15 - 13.25</td>
            <td><button onClick={deleteRow}>Cancelar Reserva</button></td>
          </tr>
          <tr>
            <td>Usuario 3</td>
            <td>3</td>
            <td>24-04-24</td>
            <td>10.55 - 12.05</td>
            <td><button onClick={deleteRow}>Cancelar Reserva</button></td>
          </tr>
        </tbody>
      </table>
    );
  }
}

export default Table;
