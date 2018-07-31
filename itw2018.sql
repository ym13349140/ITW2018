-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: itw2018
-- ------------------------------------------------------
-- Server version	8.0.11

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `reservations`
--

DROP TABLE IF EXISTS `reservations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `reservations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `affiliation` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `checkin_date` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `checkout_date` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `identity_num` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `room_type` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservations`
--

LOCK TABLES `reservations` WRITE;
/*!40000 ALTER TABLE `reservations` DISABLE KEYS */;
/*!40000 ALTER TABLE `reservations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rooms`
--

DROP TABLE IF EXISTS `rooms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `rooms` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_num` int(11) NOT NULL,
  `type_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `total_num` int(11) NOT NULL,
  `available_num` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `in_date` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rooms`
--

LOCK TABLES `rooms` WRITE;
/*!40000 ALTER TABLE `rooms` DISABLE KEYS */;
INSERT INTO `rooms` VALUES (1,1,'City View Room',17,17,460,24),(2,2,'City View Room',14,14,460,24),(3,3,'River View Room',1,1,525,25),(4,4,'River View Room',23,23,525,25),(5,5,'Business Suit',8,8,725,24),(6,6,'River View Suit',17,17,880,24),(7,5,'Business Suit',13,13,725,25),(8,2,'City View Room',19,19,460,25),(9,6,'River View Suit',6,6,880,26);
/*!40000 ALTER TABLE `rooms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `random_id` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `cname` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ename` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `country` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `pid` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `affiliation` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `edas1` varchar(256) COLLATE utf8_unicode_ci DEFAULT NULL,
  `edas2` varchar(256) COLLATE utf8_unicode_ci DEFAULT NULL,
  `edas3` varchar(256) COLLATE utf8_unicode_ci DEFAULT NULL,
  `receipt` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `receipt_title` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL,
  `receipt_id` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `email` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `vip_num` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `reg_type` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `tutorial` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `tutorial_item` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `need_invite` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `excursion` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `food_preference` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `goto_talk` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `total_fee` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-07-31 17:12:07
