-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 12-07-2024 a las 20:47:43
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `proycodoacodo`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reserva`
--

CREATE TABLE `reserva` (
  `idReserva` int(50) NOT NULL,
  `cantidadPersonas` int(2) NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `ubicacion` varchar(10) NOT NULL,
  `ocasionEspecialCual` varchar(50) DEFAULT NULL,
  `mailUsuario` longtext NOT NULL,
  `nombreCompletoUsuario` longtext NOT NULL,
  `telefonoUsuario` bigint(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `reserva`
--

INSERT INTO `reserva` (`idReserva`, `cantidadPersonas`, `fecha`, `ubicacion`, `ocasionEspecialCual`, `mailUsuario`, `nombreCompletoUsuario`, `telefonoUsuario`) VALUES
(2, 4, '2024-07-15 00:00:00.000000', '1', '1', '', '', 0),
(3, 4, '2024-07-15 00:00:00.000000', '1', '1', '', '', 0),
(5, 1, '2024-09-20 20:00:00.000000', '0', NULL, 'domineyanina@hotmail.com', 'Yanina', 1111111111),
(6, 5, '2024-08-20 20:20:00.000000', '0', NULL, 'domineyanina@hotmail.com', 'jpña', 1111111111),
(7, 1, '2027-05-20 20:00:00.000000', '0', NULL, 'domineyanina@hotmail.com', 'f', 1111111111),
(8, 1, '2025-05-20 20:00:00.000000', '0', NULL, 'domineyanina@hotmail.com', 't', 1111111111),
(9, 1, '2025-05-20 20:00:00.000000', 'Afuera', NULL, 'domineyanina@hotmail.com', 'Yanina', 1111111111),
(10, 5, '2024-10-25 20:02:00.000000', 'Afuera', NULL, 'domineyanina@hotmail.com', 'Yanina', 1111111111),
(11, 1, '2024-10-25 20:00:00.000000', 'Salon', NULL, 'domineyanina@hotmail.com', 'g', 1111111111),
(12, 2, '2025-05-20 20:00:00.000000', 'Afuera', NULL, 'domineyanina@hotmail.com', 'f', 1111111111),
(13, 1, '2025-05-20 10:00:00.000000', 'Afuera', 'Cumpleanios', 'domineyanina@hotmail.com', 'f', 1111111111),
(14, 1, '2024-10-20 20:00:00.000000', 'Afuera', NULL, 'domineyanina@hotmail.com', 'g', 1111111111),
(15, 2, '2024-10-20 10:00:00.000000', 'Afuera', 'Cumpleanios', 'domineyanina@hotmail.com', 'f', 1111111111),
(16, 1, '2024-10-20 20:00:00.000000', 'Afuera', 'Aniversario', 'domineyanina@hotmail.com', 'b', 1111111111),
(17, 1, '2024-08-10 10:00:00.000000', 'Afuera', 'Aniversario', 'domineyanina@hotmail.com', 'g', 1111111111),
(18, 5, '2024-10-20 20:00:00.000000', 'Afuera', '', 'domineyanina@hotmail.com', 'Yanina', 1111111111),
(19, 2, '2024-10-20 20:00:00.000000', 'Afuera', '', 'domineyanina@hotmail.com', 'jdio', 1),
(20, 2, '2024-10-20 20:00:00.000000', 'Afuera', '', 'domineyanina@hotmail.com', 'jdio', 1),
(21, 2, '2024-10-20 20:00:00.000000', 'Afuera', '', 'domineyanina@hotmail.com', 'jdio', 1),
(22, 2, '2024-10-20 20:00:00.000000', 'Afuera', '', 'domineyanina@hotmail.com', 'jdio', 1),
(23, 2, '2024-10-20 20:00:00.000000', 'Afuera', '', 'domineyanina@hotmail.com', 'jdio', 1),
(24, 2, '2024-10-20 20:00:00.000000', 'Afuera', '', 'domineyanina@hotmail.com', 'jdio', 1),
(25, 2, '2024-10-20 20:00:00.000000', 'Afuera', '', 'domineyanina@hotmail.com', 'jdio', 1),
(26, 2, '2024-10-20 20:00:00.000000', 'Afuera', '', 'domineyanina@hotmail.com', 'jdio', 1),
(27, 2, '2024-10-20 20:00:00.000000', 'Afuera', '', 'domineyanina@hotmail.com', 'jdio', 1),
(28, 2, '2024-10-20 20:00:00.000000', 'Afuera', '', 'domineyanina@hotmail.com', 'jdio', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(5) NOT NULL,
  `nombreUsuario` varchar(50) NOT NULL,
  `clave` varchar(50) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `telefono` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `nombreUsuario`, `clave`, `nombre`, `apellido`, `email`, `telefono`) VALUES
(1, 'Yany', 'Yany', 'Yanina', 'Dominé', 'domineyanina@hotmail.com', 1167917030),
(3, 'hola', 'clave', 'Hola', 'Hola', 'hola@hotmail.com', 1111111111),
(13, 'userPrueba', 'clave', 'Prueba', 'Hola', 'domineyanina@hotmail.com', 1167917030),
(14, 'userPrueba', 'clave', 'Prueba', 'Hola', 'domineyanina@hotmail.com', 1167917030),
(15, 'usuario', 'clave', 'Hola', 'Hola', 'domineyanina@hotmail.com', 1567917030),
(16, 'usuario', 'clave', 'Hola', 'Hola', 'domineyanina@hotmail.com', 1567917030),
(17, 'usuario', 'clave', 'Hola', 'Hola', 'domineyanina@hotmail.com', 1567917030),
(18, 'usuario', 'clave', 'Hola', 'Hola', 'domineyanina@hotmail.com', 1567917030),
(19, 'usuario', 'clave', 'Hola', 'Hola', 'domineyanina@hotmail.com', 1567917030),
(20, 'usuario', 'clave', 'Hola', 'Hola', 'domineyanina@hotmail.com', 1567917030),
(21, 'usuario', 'clave', 'Hola', 'Hola', 'domineyanina@hotmail.com', 1567917030),
(22, 'usuario', 'clave', 'Hola', 'Hola', 'domineyanina@hotmail.com', 1567917030),
(23, 'usuario', 'clave', 'Hola', 'Hola', 'domineyanina@hotmail.com', 1567917030),
(24, 'usuario', 'clave', 'Hola', 'Hola', 'domineyanina@hotmail.com', 1567917030),
(25, 'usuario', 'clave', 'Hola', 'Hola', 'domineyanina@hotmail.com', 1567917030),
(26, 'usuario', 'clave', 'nombre', 'apellido', 'email', 0),
(27, 'Hola', 'clave', 'Yanina', 'Dominé', 'domineyanina@hotmail.com', 1111111111),
(28, 'Hola', 'Hola', 'Yanina', 'Dominé', 'domineyanina@hotmail.com', 1111111111),
(29, 'Hola', 'Hola', 'Yanina', 'Dominé', 'domineyanina@hotmail.com', 1111111111),
(30, 'Hola', 'Hola', 'Yanina', 'Dominé', 'domineyanina@hotmail.com', 1111111111),
(31, 'Hola', 'Hola', 'Yanina', 'Dominé', 'domineyanina@hotmail.com', 1111111111),
(32, 'Hola', 'Hola', 'Yanina', 'Dominé', 'domineyanina@hotmail.com', 1111111111),
(33, 'Hola', 'Hola', 'Yanina', 'Dominé', 'domineyanina@hotmail.com', 1111111111),
(34, 'Hola', 'Hola', 'Yanina', 'Dominé', 'domineyanina@hotmail.com', 1111111111),
(35, 'Hola', 'Hola', 'Yanina', 'Dominé', 'domineyanina@hotmail.com', 1111111111),
(36, 'Hola', 'Hola', 'Yanina', 'Dominé', 'domineyanina@hotmail.com', 1111111111),
(37, 'Hola', 'Hola', 'Yanina', 'Dominé', 'domineyanina@hotmail.com', 1111111111),
(38, 'Hola', 'Hola', 'Yanina', 'Dominé', 'domineyanina@hotmail.com', 1111111111),
(39, 'Hola', 'Hola', 'Yanina', 'Dominé', 'domineyanina@hotmail.com', 1111111111),
(40, 'Hola', 'Hola', 'Yanina', 'Dominé', 'domineyanina@hotmail.com', 1111111111),
(41, 'Hola', 'Hola', 'Yanina', 'Dominé', 'domineyanina@hotmail.com', 1111111111),
(42, 'Hola', 'Hola', 'Yanina', 'Dominé', 'domineyanina@hotmail.com', 1111111111),
(43, 'Hola', 'Hola', 'Yanina', 'Dominé', 'domineyanina@hotmail.com', 1111111111),
(44, 'Hola', 'Hola', 'Yanina', 'Dominé', 'domineyanina@hotmail.com', 1111111111),
(45, 'Hola', 'Hola', 'Yanina', 'Dominé', 'domineyanina@hotmail.com', 1111111111),
(46, 'Hola', 'Hola', 'Yanina', 'Dominé', 'domineyanina@hotmail.com', 1111111111),
(47, 'Hola', 'Hola', 'Yanina', 'Dominé', 'domineyanina@hotmail.com', 1111111111),
(48, 'Hola', 'Hola', 'Yanina', 'Dominé', 'domineyanina@hotmail.com', 1111111111),
(49, 'Hola', 'clave', 'Yanina', 'Dominé', 'domineyanina@hotmail.com', 1111111111),
(50, 'Hola', 'clave', 'Yanina', 'Dominé', 'domineyanina@hotmail.com', 1111111111);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `reserva`
--
ALTER TABLE `reserva`
  ADD PRIMARY KEY (`idReserva`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `reserva`
--
ALTER TABLE `reserva`
  MODIFY `idReserva` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
