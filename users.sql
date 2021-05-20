-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: May 20, 2021 at 07:17 PM
-- Server version: 5.6.17
-- PHP Version: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `admin`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES
(1, 'TAP[AS KUMAR4 DAS', 'tdas951341@gmail.com', '$2b$12$CO4eiBkJB8bYI/sFQPJJm.66OIy.Wqd9bYnIIcr2gk7QY/xsWgtfK'),
(2, 'fd', 'tirtha@gmail.com', '$2b$12$u8j0aILTGgu7V6WymOZD7eflegNJRryNmQxe9hBi/0.I7UrhNvUyq'),
(3, 'Tirtharaj Das', 'tirtha@gmail.com', '$2b$12$4rVT/RsFltZjki5kiytJbe4yLXUGkFldsx9jpI8ziq9MhfaYAnWxe'),
(4, 'sunny', 'sunny@gmail.com', '$2b$12$jm56r69E8U5qIqDGayG.XOzEDT5uyF3bTjGylLP436TUHIKgxjl2m'),
(5, 'sunny', 'sunn@gmail.com', '$2b$12$43tLIo1orITsr7J/SjMlueok8Oxp4dbQd2edicrtvJy3M6rWmChcm');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
