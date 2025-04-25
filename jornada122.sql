-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-04-2025 a las 01:58:14
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `jornada122`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `extra`
--

CREATE TABLE `extra` (
  `id` int(11) NOT NULL,
  `nombre` varchar(64) NOT NULL,
  `valor` varchar(64) NOT NULL,
  `staff_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `staff`
--

CREATE TABLE `staff` (
  `id` int(11) NOT NULL,
  `nombre` varchar(64) NOT NULL,
  `gap` varchar(64) DEFAULT NULL,
  `estiramiento` varchar(64) DEFAULT NULL,
  `contrato` varchar(64) DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  `foto` text DEFAULT NULL,
  `telefono` varchar(10) DEFAULT NULL,
  `ocupacion` varchar(32) DEFAULT NULL,
  `residencia` varchar(10) DEFAULT NULL,
  `prioridad` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `staff`
--

INSERT INTO `staff` (`id`, `nombre`, `gap`, `estiramiento`, `contrato`, `edad`, `foto`, `telefono`, `ocupacion`, `residencia`, `prioridad`) VALUES
(1, 'Angel Mares', '77 Cigarras', 'De Kamikaze a Gladiador', 'Yo soy un hombre poderoso, auténtico, leal', 23, '/static/AngelMares.jpg', '5578138451', 'ING. Telemático/ Programador ', 'Texcoco', 0),
(2, 'Selene Guzmán', '77 Cigarras', 'De Perra a Madre Naturaleza', 'Yo soy una mujer libre, valiente, poderosa', 40, '/static/SeleneGuzman.jpg', '5539262309', 'ING. Agrónomo ', 'Texcoco', 2),
(3, 'Reyes Cruz', 'P.E. 73 Axolotl Itzamna', 'De Muerto a Vivo', 'Yo soy un hombre amoroso, honesto, comprometido', 59, '/static/ReyesCruz.jpg', '5536991608', 'Plomería, gas, electricidad', 'Coyoacán', 0),
(4, 'Jennifer Rivera', '105 Mariposas Ikigai', NULL, NULL, 22, '/static/JenniferRivera.jpg', '5542192650', 'Psicóloga', 'Iztacalco', 0),
(5, 'Miriam Gonzalez', '104', 'De Perra a Madre Naturaleza', 'Yo soy una mujer amorosa, poderosa, comprometida', 42, '/static/MiriamGonzalez.jpg', '5530383920', 'Ingeniero Industrial / Comercian', 'Chimalhuac', 0),
(6, 'Lorena Lomelí', '76', 'De Kamikaze a Amazona', 'Yo soy una mujer honesta, valiente, amorosa', 36, '/static/LorenaLomeli.jpg', '5537944091', 'Estilista', NULL, 0),
(7, 'Itzani Márquez', '105 Mariposas Ikigai', 'De Baby bitch a Flash dance', 'Yo soy una mujer amorosa, valiente, auténtica', 27, '\\static\\ItzaniMarzquez.jpg', '5526622385', NULL, NULL, 0),
(8, 'Mónica Lugo', '77 Cigarras', 'De Víctima a Gloria Trevi', 'Yo soy una mujer responsable, amorosa, honesta', 49, '/static/MonicaLugo.jpg', '5526580892', NULL, NULL, 0),
(9, 'Armando García', '72 Yavhé Yolotl', 'De Zombie a Romeo Santos', 'Yo soy un hombre honesto, amoroso, poderoso', 54, '/static/ArmandoGarcia.jpg', '5574582464', 'Coductor de Uber / Emprendedor d', NULL, 0),
(10, 'Victor Ríos', '105 Mariposas Ikigai', NULL, 'Yo soy un hombre amoroso, poderoso, valiente', NULL, '/static/VictorRios.jpg', '5635761750', 'Agencia de viajes', NULL, 0),
(11, 'Carlos Tejeda', '105 Mariposas Ikigai', 'De Boy Scout a Backstreet Boy', 'Yo soy un hombre valiente, responsable, libre', 24, '/static/CarlosTejeda.jpg', '5522028937', 'Preventa comercial', 'Ixtapaluca', 0),
(12, 'Mónica León', '100 Samadhi', 'De Perra a Madre Naturaleza', 'Yo soy una mujer amorosa, comprometida, valiente', 50, '/static/MonicaLeon.jpg', '5542935510', 'Tejedora a crochet', 'Texcoco', 0),
(13, 'Angy', '105 Mariposas Ikigai', NULL, 'Yo soy una mujer libre, valiente, poderosa', NULL, '/static/Angeles.jpg', '5534563377', NULL, NULL, 0),
(14, 'Kevin García', '107 Ópalos de Fuego', 'De Superhéroe Fracasado a Gaviota', 'Yo soy un hombre amoroso, apasionado, responsable', 24, '/static/KevinGarcia.jpg', '5610706772', 'Abogado / Gerente de bar', NULL, 0),
(15, 'Keila Guzmán', '104', 'De Perra a Madre Naturaleza', 'Yo soy una mujer poderosa, valiente, libre', NULL, '/static/KeilaGuzman.jpg', '5959525916', 'ING. Agrónomo', 'Texcoco', 0),
(16, 'Patricia Moran', NULL, 'De Monja a Gloria Trevi', 'Yo soy una mujer responsable, valiente, amorosa', 49, '/static/PatriciaMoran.jpg', '5615070348', 'Comerciante / Hogar', 'Ixtapaluca', 0),
(17, 'Jorge Ramírez', '110 Jaguares Amaterasu', 'De Superhéroe Fracasado a Gaviota', 'Yo soy un hombre amoroso, poderoso, comprometido', 42, NULL, '5543450223', 'Emprendedor / maestro de meditac', 'Coyoacán', 0),
(18, 'Arlet Anaya', '110 Jaguares Amaterasu', 'De Perra a Madre Naturaleza', 'Yo soy una mujer valiente, poderosa, amorosa', 45, NULL, '5531954390', 'Enfermera', 'Texcoco', 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `extra`
--
ALTER TABLE `extra`
  ADD PRIMARY KEY (`id`),
  ADD KEY `staff_id` (`staff_id`);

--
-- Indices de la tabla `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`),
  ADD UNIQUE KEY `foto` (`foto`) USING HASH;

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `extra`
--
ALTER TABLE `extra`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `staff`
--
ALTER TABLE `staff`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `extra`
--
ALTER TABLE `extra`
  ADD CONSTRAINT `extra_ibfk_1` FOREIGN KEY (`staff_id`) REFERENCES `staff` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
