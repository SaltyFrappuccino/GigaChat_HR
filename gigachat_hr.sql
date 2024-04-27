-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Апр 24 2024 г., 11:44
-- Версия сервера: 10.4.32-MariaDB
-- Версия PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `gigachat_hr`
--

-- --------------------------------------------------------

--
-- Структура таблицы `candidate`
--

CREATE TABLE `candidate` (
  `id` int(11) NOT NULL,
  `fio` varchar(255) NOT NULL,
  `photo_url` varchar(512),
  `phone_num` varchar(20),
  `email` varchar(255) NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `candidatevacancy`
--

CREATE TABLE `candidatevacancy` (
  `id` int(11) NOT NULL,
  `candidate_id` int(11) DEFAULT NULL,
  `vacancy_id` int(11) DEFAULT NULL,
  `inStatusTime` datetime NOT NULL,
  `status` enum('new','declined','intresting') DEFAULT 'new',
  `resumeMatching` int(11) NOT NULL DEFAULT -1,
  `teamProfileMatch` int(11) NOT NULL DEFAULT -1,
  `recruiterSelection` tinyint(1) NOT NULL DEFAULT 0,
  `noTelegram` tinyint(1) NOT NULL DEFAULT 0,
  `interviewPassed` tinyint(1) NOT NULL DEFAULT 0,
  `frequentJobChanges` tinyint(1) NOT NULL DEFAULT 0,
  `interviewFailed` tinyint(1) NOT NULL DEFAULT 0,
  `noHigherEducation` tinyint(1) NOT NULL DEFAULT 0,
  `experienceMismatch` tinyint(1) NOT NULL DEFAULT 0,
  `regionMismatch` tinyint(1) NOT NULL DEFAULT 0,
  `gigaRejected` tinyint(1) NOT NULL DEFAULT 0,
  `content` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `vacancy`
--

CREATE TABLE `vacancy` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `positionNumber` varchar(255) NOT NULL,
  `manager` varchar(255) DEFAULT NULL,
  `recrutor` varchar(255) DEFAULT NULL,
  `content` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `candidate`
--
ALTER TABLE `candidate`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `candidatevacancy`
--
ALTER TABLE `candidatevacancy`
  ADD PRIMARY KEY (`id`),
  ADD KEY `candidate_id` (`candidate_id`),
  ADD KEY `vacancy_id` (`vacancy_id`);

--
-- Индексы таблицы `vacancy`
--
ALTER TABLE `vacancy`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `candidate`
--
ALTER TABLE `candidate`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `candidatevacancy`
--
ALTER TABLE `candidatevacancy`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `vacancy`
--
ALTER TABLE `vacancy`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `candidatevacancy`
--
ALTER TABLE `candidatevacancy`
  ADD CONSTRAINT `candidatevacancy_ibfk_1` FOREIGN KEY (`candidate_id`) REFERENCES `candidate` (`id`),
  ADD CONSTRAINT `candidatevacancy_ibfk_2` FOREIGN KEY (`vacancy_id`) REFERENCES `vacancy` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
