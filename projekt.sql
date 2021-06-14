-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 14 Cze 2021, 13:41
-- Wersja serwera: 10.1.36-MariaDB
-- Wersja PHP: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `projekt`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `grupa`
--

CREATE TABLE `grupa` (
  `ID` int(11) NOT NULL,
  `Nazwa GRUPY` varchar(20) NOT NULL,
  `UPRAWNIENIA` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Zrzut danych tabeli `grupa`
--

INSERT INTO `grupa` (`ID`, `Nazwa GRUPY`, `UPRAWNIENIA`) VALUES
(1, 'Administrator', 5),
(2, 'Trener', 3),
(3, 'Gracz Profesjonalny', 2),
(4, 'Zwyk?y Gracz', 2);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `users`
--

CREATE TABLE `users` (
  `ID` int(11) NOT NULL,
  `Login` varchar(20) NOT NULL,
  `Haslo` varchar(20) NOT NULL,
  `Email` varchar(40) NOT NULL,
  `Imie` varchar(20) NOT NULL,
  `Nazwisko` varchar(20) NOT NULL,
  `Wiek` int(11) NOT NULL,
  `Grupa` int(11) NOT NULL,
  `Elo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Zrzut danych tabeli `users`
--

INSERT INTO `users` (`ID`, `Login`, `Haslo`, `Email`, `Imie`, `Nazwisko`, `Wiek`, `Grupa`, `Elo`) VALUES
(1, 'Admin', 'Admin1', 'admin@gmail.com', 'admin', 'admin', 31, 5, 0),
(2, 'Login1', 'Haslo1', '1@gmai.com', 'a', 'b', 1, 1, 1),
(3, 'Login', 'Haslo', '2@gmai.com', 'a', 'b', 1, 1, 0),
(4, 'Logingdf', 'Haslogdf', 'Emailgdf', 'Imiegdf', 'Nazwiskogdf', 0, 1, 0),
(5, 'Login432432', 'Haslo', 'Email', 'Imie', 'Nazwisko', 0, 1, 0),
(6, 'Login321312', 'Haslo', 'Email', 'Imie', 'Nazwisko', 0, 1, 0),
(7, 'yLoginfd', 'Haslogrdf', 'Email', 'Imie', 'Nazwisko', 0, 1, 0),
(14, 'user2', 'user2', 'user2@gmai.com', 'user2', 'user2', 22, 1, 0);

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `users`
--
ALTER TABLE `users`
  ADD UNIQUE KEY `ID` (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `users`
--
ALTER TABLE `users`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
