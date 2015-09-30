CREATE DATABASE  IF NOT EXISTS `etldb` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `etldb`;
-- MySQL dump 10.13  Distrib 5.6.25, for debian-linux-gnu (x86_64)
--
-- Host: 127.0.0.1    Database: etldb
-- ------------------------------------------------------
-- Server version	5.6.25-0ubuntu0.15.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `file_status`
--

DROP TABLE IF EXISTS `file_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `file_status` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `file_name` varchar(32) DEFAULT NULL,
  `stream_id` int(11) NOT NULL,
  `ref_date` date DEFAULT NULL,
  `record_count` int(11) DEFAULT NULL,
  `generate_session_id` int(11) NOT NULL,
  `load_session_id` int(11) DEFAULT NULL,
  `size` int(11) DEFAULT NULL,
  `archived` tinyint(1) DEFAULT NULL,
  `gen_file_name` varchar(45) DEFAULT NULL,
  `file_created_time` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_file_status_stream1_idx` (`stream_id`),
  KEY `fk_file_status_generate_session1_idx` (`generate_session_id`),
  KEY `fk_file_status_load_session1_idx` (`load_session_id`),
  CONSTRAINT `fk_file_status_generate_session1` FOREIGN KEY (`generate_session_id`) REFERENCES `generate_session` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_file_status_load_session1` FOREIGN KEY (`load_session_id`) REFERENCES `load_session` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_file_status_stream1` FOREIGN KEY (`stream_id`) REFERENCES `stream` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=4331 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `file_status`
--

LOCK TABLES `file_status` WRITE;
/*!40000 ALTER TABLE `file_status` DISABLE KEYS */;
/*!40000 ALTER TABLE `file_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ftp_table`
--

DROP TABLE IF EXISTS `ftp_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ftp_table` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stream_id` int(11) NOT NULL,
  `ftp_type` varchar(32) DEFAULT NULL,
  `ip` varchar(32) DEFAULT NULL,
  `username` varchar(32) DEFAULT NULL,
  `password` varchar(32) DEFAULT NULL,
  `remote_dir` varchar(100) DEFAULT NULL,
  `local_dir` varchar(100) DEFAULT NULL,
  `search_query` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_ftp_table_stream_idx` (`stream_id`),
  CONSTRAINT `fk_ftp_table_stream` FOREIGN KEY (`stream_id`) REFERENCES `stream` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ftp_table`
--

LOCK TABLES `ftp_table` WRITE;
/*!40000 ALTER TABLE `ftp_table` DISABLE KEYS */;
/*!40000 ALTER TABLE `ftp_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `generate_history`
--

DROP TABLE IF EXISTS `generate_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `generate_history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `timestamp` datetime DEFAULT NULL,
  `stage` varchar(200) DEFAULT NULL,
  `generate_session_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_generate_history_generate_session1_idx` (`generate_session_id`),
  CONSTRAINT `fk_generate_history_generate_session1` FOREIGN KEY (`generate_session_id`) REFERENCES `generate_session` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `generate_history`
--

LOCK TABLES `generate_history` WRITE;
/*!40000 ALTER TABLE `generate_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `generate_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `generate_session`
--

DROP TABLE IF EXISTS `generate_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `generate_session` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ref_date` date DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `status` varchar(32) DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  `stream_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_generate_session_stream1_idx` (`stream_id`),
  CONSTRAINT `fk_generate_session_stream1` FOREIGN KEY (`stream_id`) REFERENCES `stream` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=240 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `generate_session`
--

LOCK TABLES `generate_session` WRITE;
/*!40000 ALTER TABLE `generate_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `generate_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `generate_thread_control`
--

DROP TABLE IF EXISTS `generate_thread_control`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `generate_thread_control` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stream_id` int(11) NOT NULL,
  `thread` int(11) DEFAULT NULL,
  `status` varchar(32) DEFAULT NULL,
  `message` varchar(200) DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_generate_thread_control_stream1_idx` (`stream_id`),
  CONSTRAINT `fk_generate_thread_control_stream1` FOREIGN KEY (`stream_id`) REFERENCES `stream` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `generate_thread_control`
--

LOCK TABLES `generate_thread_control` WRITE;
/*!40000 ALTER TABLE `generate_thread_control` DISABLE KEYS */;
/*!40000 ALTER TABLE `generate_thread_control` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `load_session`
--

DROP TABLE IF EXISTS `load_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `load_session` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stream_id` int(11) NOT NULL,
  `ref_date` date DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `status` varchar(32) DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_load_session_stream1_idx` (`stream_id`),
  CONSTRAINT `fk_load_session_stream1` FOREIGN KEY (`stream_id`) REFERENCES `stream` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `load_session`
--

LOCK TABLES `load_session` WRITE;
/*!40000 ALTER TABLE `load_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `load_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `load_thread_control`
--

DROP TABLE IF EXISTS `load_thread_control`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `load_thread_control` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stream_id` int(11) NOT NULL,
  `thread` int(11) DEFAULT NULL,
  `status` varchar(32) DEFAULT NULL,
  `message` varchar(200) DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_load_thread_control_stream1_idx` (`stream_id`),
  CONSTRAINT `fk_load_thread_control_stream1` FOREIGN KEY (`stream_id`) REFERENCES `stream` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `load_thread_control`
--

LOCK TABLES `load_thread_control` WRITE;
/*!40000 ALTER TABLE `load_thread_control` DISABLE KEYS */;
/*!40000 ALTER TABLE `load_thread_control` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loading_history`
--

DROP TABLE IF EXISTS `loading_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `loading_history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `load_session_id` int(11) NOT NULL,
  `timestamp` datetime DEFAULT NULL,
  `stage` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_loading_history_load_session1_idx` (`load_session_id`),
  CONSTRAINT `fk_loading_history_load_session1` FOREIGN KEY (`load_session_id`) REFERENCES `load_session` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loading_history`
--

LOCK TABLES `loading_history` WRITE;
/*!40000 ALTER TABLE `loading_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `loading_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stream`
--

DROP TABLE IF EXISTS `stream`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stream` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `sample_filename` varchar(45) DEFAULT NULL,
  `in_dir` varchar(100) DEFAULT NULL,
  `compressed` tinyint(1) DEFAULT NULL,
  `ftp` tinyint(1) DEFAULT NULL,
  `files_per_session` int(11) DEFAULT NULL,
  `no_threads` int(11) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stream`
--

LOCK TABLES `stream` WRITE;
/*!40000 ALTER TABLE `stream` DISABLE KEYS */;
INSERT INTO `stream` VALUES (1,'voice',NULL,NULL,NULL,NULL,100,10,NULL);
/*!40000 ALTER TABLE `stream` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-09-30 11:33:03
