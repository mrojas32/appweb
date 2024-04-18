import DataTable from "react-data-table-component";
import {useState, useEffect} from 'react'
import React from 'react';
import './Table.css'; // Importar el archivo CSS para los estilos

class Table extends React.Component {
  render() {
    return (
    <table className="styled-table">
        <thead>
          <tr>
            <th>Tipo de Cancha</th>
            <th>Fecha</th>
            <th>Hora</th>
            <th>Bloque</th>
            <th>Estado</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Cancha Futbol 1</td>
            <td>18-04-24</td>
            <td>9:35 - 10_45</td>
            <td>3-4</td>
            <td>Activo</td>
          </tr>
          <tr>
            <td>Cancha Tenis</td>
            <td>19-04-24</td>
            <td>12.15 - 13.25</td>
            <td>7-8</td>
            <td>Activo</td>
          </tr>
          <tr>
            <td>Cancha Futbol 2</td>
            <td>24-04-24</td>
            <td>10.55 - 12.05</td>
            <td>5-6</td>
            <td>Activo</td>
          </tr>
        </tbody>
      </table>
    );
  }
}

export default Table;
