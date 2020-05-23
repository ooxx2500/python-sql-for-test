-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2020-05-14 10:23:54
-- 伺服器版本： 10.4.11-MariaDB
-- PHP 版本： 7.4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `mona_db`
--

-- --------------------------------------------------------

--
-- 資料表結構 `guest_table`
--

CREATE TABLE `guest_table` (
  `cid` int(11) NOT NULL,
  `cname` varchar(30) DEFAULT NULL,
  `cSex` varchar(10) DEFAULT NULL,
  `cPhone` varchar(10) DEFAULT NULL,
  `cEmail` varchar(30) DEFAULT NULL,
  `cBirth` date DEFAULT NULL,
  `caddress` varchar(50) DEFAULT '未輸入'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `guest_table`
--

INSERT INTO `guest_table` (`cid`, `cname`, `cSex`, `cPhone`, `cEmail`, `cBirth`, `caddress`) VALUES
(1, 'judy', NULL, '0920555522', 'iasdasdx@gmail', '1999-09-09', '忠孝東路4段200號'),
(2, 'aria', NULL, '930333541', 'asdasdasd@fdsas.asd', '2000-05-06', '新店市'),
(3, '韓國瑜', NULL, '958556750', '0', '0000-00-00', '忠孝東路'),
(4, '默在剛', NULL, NULL, NULL, '1989-08-09', '忠孝東路4段200號99999'),
(5, '奇奇', NULL, '985888666', NULL, '1980-03-03', '忠孝東路2段100號'),
(6, '黑武4', NULL, '0920224455', NULL, NULL, '未輸入'),
(7, '綠巨人', NULL, NULL, NULL, NULL, '未輸入'),
(8, '大隻老', NULL, NULL, NULL, NULL, '未輸入');

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `guest_table`
--
ALTER TABLE `guest_table`
  ADD PRIMARY KEY (`cid`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `guest_table`
--
ALTER TABLE `guest_table`
  MODIFY `cid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
