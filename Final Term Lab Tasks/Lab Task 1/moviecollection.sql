-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 29, 2025 at 06:04 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `moviecollection`
--

-- --------------------------------------------------------

--
-- Table structure for table `movies`
--

CREATE TABLE `movies` (
  `movie_id` int(10) NOT NULL,
  `title` varchar(50) NOT NULL,
  `main_actor` varchar(50) NOT NULL,
  `director` varchar(50) NOT NULL,
  `genre` varchar(25) NOT NULL,
  `gross_sales` float NOT NULL,
  `ratings` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `movies`
--

INSERT INTO `movies` (`movie_id`, `title`, `main_actor`, `director`, `genre`, `gross_sales`, `ratings`) VALUES
(1, 'josh', 'coronel', 'renzo', 'action', 1000000, 'PG'),
(1214, 'joshua', 'coronel', 'renzo', 'action', 10000000, 'PG'),
(11233, 'josh the greate', 'renzo', 'joshua', 'action', 100000, 'PG'),
(11234, '365 josh', 'Coronel Joshua', 'Guevarra Renzo', 'Bromanse', 100000000, 'PG'),
(11235, '365 Josh', 'Coronel Joshua', 'Guevarra Renzo', 'Bromanse', 1000000000, 'X');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `movies`
--
ALTER TABLE `movies`
  ADD PRIMARY KEY (`movie_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
