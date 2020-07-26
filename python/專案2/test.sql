-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2020-07-26 15:51:18
-- 伺服器版本： 10.4.11-MariaDB
-- PHP 版本： 7.2.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `test`
--

-- --------------------------------------------------------

--
-- 資料表結構 `guest_table`
--

CREATE TABLE `guest_table` (
  `id_` int(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `address` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `phone` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 傾印資料表的資料 `guest_table`
--

INSERT INTO `guest_table` (`id_`, `name`, `address`, `phone`, `email`) VALUES
(1, 'mona', '請問你住哪', '0920333666', 'cat@gmail.com'),
(2, 'aria', '偶祝你家旁邊', '093344567', 'fsfsddt@gmail.com');

-- --------------------------------------------------------

--
-- 資料表結構 `momom`
--

CREATE TABLE `momom` (
  `price` int(20) NOT NULL,
  `quantity` int(20) NOT NULL,
  `id_` int(20) NOT NULL,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 傾印資料表的資料 `momom`
--

INSERT INTO `momom` (`price`, `quantity`, `id_`, `name`) VALUES
(20, 4, 1, '桌上電腦'),
(34, 9, 2, '滑鼠'),
(17, 18, 3, '螢幕'),
(20, 20, 4, '筆電'),
(34, 213, 5, '螢幕'),
(17, 25, 6, '桌上電腦'),
(20, 6, 11, '桌上電腦'),
(30, 9, 12, '筆電'),
(1, 18, 13, '螢幕'),
(20, 6, 14, '筆電'),
(30, 15, 15, '螢幕'),
(1, 18, 16, '桌上電腦'),
(20, 10, 17, '螢幕'),
(30, 15, 18, '筆電'),
(1, 18, 19, '滑鼠'),
(20, 5, 20, '筆電'),
(30, 20, 21, '桌上電腦'),
(1, 18, 22, '筆電'),
(20, 10, 23, '滑鼠'),
(30, 20, 24, '筆電'),
(1, 13, 25, '螢幕'),
(20, 10, 26, '桌上電腦'),
(30, 20, 27, '喇叭'),
(1, 18, 28, '筆電'),
(20, 10, 29, '螢幕'),
(30, 20, 30, '筆電'),
(1, 18, 31, '筆電'),
(20, 10, 32, '筆電'),
(30, 20, 33, '筆電'),
(1, 18, 34, '筆電'),
(20, 10, 35, '筆電'),
(30, 20, 36, '筆電'),
(1, 18, 37, '筆電');

-- --------------------------------------------------------

--
-- 資料表結構 `momom2`
--

CREATE TABLE `momom2` (
  `id_` int(10) NOT NULL,
  `name` varchar(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `good` int(10) NOT NULL,
  `price` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 傾印資料表的資料 `momom2`
--

INSERT INTO `momom2` (`id_`, `name`, `good`, `price`) VALUES
(3, '電腦', 10, 10),
(4, '筆電', 20, 20),
(9, '螢幕', 15, 15),
(10, '鍵盤', 8, 8);

-- --------------------------------------------------------

--
-- 資料表結構 `orders`
--

CREATE TABLE `orders` (
  `id_` int(11) NOT NULL,
  `orderNO` int(20) NOT NULL,
  `date` date NOT NULL,
  `guest` int(20) NOT NULL,
  `goods1` int(20) NOT NULL,
  `price1` int(10) NOT NULL,
  `goods2` int(20) NOT NULL,
  `price2` int(20) NOT NULL,
  `goods3` int(20) NOT NULL,
  `price3` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- 資料表結構 `sell_list`
--

CREATE TABLE `sell_list` (
  `date` date NOT NULL,
  `price` int(10) NOT NULL,
  `quantity` int(20) NOT NULL,
  `total` int(20) NOT NULL,
  `id_` int(20) NOT NULL,
  `name` varchar(20) CHARACTER SET utf8mb4 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 傾印資料表的資料 `sell_list`
--

INSERT INTO `sell_list` (`date`, `price`, `quantity`, `total`, `id_`, `name`) VALUES
('2020-07-01', 10, 1, 10, 1, '螢幕'),
('2020-07-01', 10, 1, 10, 2, '螢幕'),
('2020-07-01', 34, 2, 68, 3, '螢幕'),
('2020-07-05', 34, 2, 68, 4, '螢幕'),
('2020-07-21', 34, 2, 68, 5, '螢幕'),
('2020-07-21', 34, 2, 68, 6, '螢幕'),
('2020-07-22', 34, 2, 68, 7, '螢幕'),
('2020-07-22', 34, 5, 170, 8, '螢幕'),
('2020-07-22', 34, 1, 34, 9, '滑鼠'),
('2020-07-25', 34, 1, 34, 10, '螢幕'),
('2020-07-25', 30, 5, 150, 11, '螢幕'),
('2020-07-26', 17, 1, 17, 12, '桌上電腦'),
('2020-07-26', 17, 2, 34, 13, '桌上電腦'),
('2020-07-26', 17, 2, 34, 14, '桌上電腦'),
('2020-07-26', 20, 5, 100, 15, '筆電'),
('2020-07-26', 34, 10, 340, 16, '螢幕');

-- --------------------------------------------------------

--
-- 資料表結構 `users`
--

CREATE TABLE `users` (
  `id_` int(11) NOT NULL,
  `accont` varchar(20) NOT NULL,
  `password` varchar(30) NOT NULL,
  `user_name` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 傾印資料表的資料 `users`
--

INSERT INTO `users` (`id_`, `accont`, `password`, `user_name`) VALUES
(1, 'root', '1234', 'administrators'),
(2, 'test01', '1234', 'test01');

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `guest_table`
--
ALTER TABLE `guest_table`
  ADD PRIMARY KEY (`id_`);

--
-- 資料表索引 `momom`
--
ALTER TABLE `momom`
  ADD PRIMARY KEY (`id_`);

--
-- 資料表索引 `momom2`
--
ALTER TABLE `momom2`
  ADD PRIMARY KEY (`id_`),
  ADD UNIQUE KEY `name` (`name`);

--
-- 資料表索引 `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id_`),
  ADD KEY `goods` (`goods1`),
  ADD KEY `goods2` (`goods2`),
  ADD KEY `goods3` (`goods3`),
  ADD KEY `guest` (`guest`);

--
-- 資料表索引 `sell_list`
--
ALTER TABLE `sell_list`
  ADD PRIMARY KEY (`id_`);

--
-- 資料表索引 `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id_`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `guest_table`
--
ALTER TABLE `guest_table`
  MODIFY `id_` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `momom`
--
ALTER TABLE `momom`
  MODIFY `id_` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `momom2`
--
ALTER TABLE `momom2`
  MODIFY `id_` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `orders`
--
ALTER TABLE `orders`
  MODIFY `id_` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `sell_list`
--
ALTER TABLE `sell_list`
  MODIFY `id_` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `users`
--
ALTER TABLE `users`
  MODIFY `id_` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- 已傾印資料表的限制式
--

--
-- 資料表的限制式 `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`goods1`) REFERENCES `momom` (`id_`),
  ADD CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`goods2`) REFERENCES `momom` (`id_`),
  ADD CONSTRAINT `orders_ibfk_3` FOREIGN KEY (`goods3`) REFERENCES `momom` (`id_`),
  ADD CONSTRAINT `orders_ibfk_4` FOREIGN KEY (`goods3`) REFERENCES `momom` (`id_`),
  ADD CONSTRAINT `orders_ibfk_5` FOREIGN KEY (`guest`) REFERENCES `guest_table` (`id_`),
  ADD CONSTRAINT `orders_ibfk_6` FOREIGN KEY (`goods1`) REFERENCES `momom2` (`id_`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
