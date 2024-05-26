CREATE TABLE IF NOT EXISTS Usuario(
    ID_usuario INT AUTO_INCREMENT  primary key,
    nombre VARCHAR(255) NOT NULL,
    passwd VARCHAR(255) NOT NULL,
    estudiante BOOLEAN NOT NULL,
    correo VARCHAR(255) NOT NULL,
    UNIQUE KEY unique_nombre (nombre)
    );


INSERT INTO Usuario (ID_usuario, nombre, passwd, estudiante, correo)
VALUES
    (1, 'Juan Pérez', 'secreto123', TRUE, 'juan.p@usm.cl'),
    (2, 'María López', 'clave456', FALSE, 'maria.l@usm.cl'),
    (3, 'Pedro Rodríguez', 'password789', TRUE, 'pedro.r@usm.cl');
    
CREATE TABLE IF NOT EXISTS Canchas (
    ID_canchas INT AUTO_INCREMENT  PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    tipo VARCHAR(255) NOT NULL,
    ubicacion VARCHAR(255),
    UNIQUE KEY unique_nombre (nombre)
);

INSERT INTO Canchas (ID_canchas, nombre, tipo, ubicacion)
VALUES
    (1, 'Cancha de tenis', 'Tenis', 'Al costado'),
    (2, 'Cancha de fútbol', 'Futbol','Al medio'),
    (3, 'Cancha de baloncesto', 'Basquetball', 'En un lado');

CREATE TABLE IF NOT EXISTS Reserva (
  ID_reserva INT AUTO_INCREMENT  PRIMARY KEY,
  fecha DATE,
  bloq_ini VARCHAR(10),
  bloq_final VARCHAR(10),
  ID_usuario INT,
  ID_canchas INT,
  FOREIGN KEY (ID_usuario) REFERENCES Usuario(ID_usuario),
  FOREIGN KEY (ID_canchas) REFERENCES Canchas(ID_canchas)
);

INSERT INTO Reserva (ID_reserva, fecha, bloq_ini, bloq_final, ID_Usuario, ID_canchas)
VALUES
    (1, '2024-05-25', '09:00', '10:30', 1, 1),
    (2, '2024-05-26', '14:00', '15:30', 2, 2),
    (3, '2024-05-27', '18:00', '19:30', 3, 3);

CREATE TABLE IF NOT EXISTS Administrador (
    ID_admin INT AUTO_INCREMENT  PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    passwd VARCHAR(255) NOT NULL,
    UNIQUE KEY unique_nombre (nombre)
);

INSERT INTO Administrador (ID_admin, nombre, passwd)
VALUES
    (1, 'Ana García', 'admin123'),
    (2, 'Carlos Rodríguez', 'clave456'),
    (3, 'Laura Pérez', 'secreto789');
