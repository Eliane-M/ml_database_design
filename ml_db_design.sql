-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: mysql-mldesign-ml-database-design.e.aivencloud.com    Database: ml_db_design
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '63a678e7-fc71-11ef-900d-ba0ec6186aed:1-49';

--
-- Table structure for table `Academic_Details`
--

DROP TABLE IF EXISTS `Academic_Details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Academic_Details` (
  `Student_ID` varchar(10) NOT NULL,
  `Department` varchar(50) DEFAULT NULL,
  `Attendance_Percentage` decimal(5,2) DEFAULT NULL,
  `Midterm_Score` decimal(5,2) DEFAULT NULL,
  `Final_Score` decimal(5,2) DEFAULT NULL,
  `Assignments_Avg` decimal(5,2) DEFAULT NULL,
  `Quizzes_Avg` decimal(5,2) DEFAULT NULL,
  `Participation_Score` decimal(5,2) DEFAULT NULL,
  `Projects_Score` decimal(5,2) DEFAULT NULL,
  `Total_Score` decimal(5,2) DEFAULT NULL,
  `Grade` char(2) DEFAULT NULL,
  PRIMARY KEY (`Student_ID`),
  CONSTRAINT `Academic_Details_ibfk_1` FOREIGN KEY (`Student_ID`) REFERENCES `Students` (`Student_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Academic_Details`
--

LOCK TABLES `Academic_Details` WRITE;
/*!40000 ALTER TABLE `Academic_Details` DISABLE KEYS */;
/*!40000 ALTER TABLE `Academic_Details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Extracurriculars`
--

DROP TABLE IF EXISTS `Extracurriculars`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Extracurriculars` (
  `Student_ID` varchar(10) NOT NULL,
  `Extracurricular_Activities` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`Student_ID`),
  CONSTRAINT `Extracurriculars_ibfk_1` FOREIGN KEY (`Student_ID`) REFERENCES `Students` (`Student_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Extracurriculars`
--

LOCK TABLES `Extracurriculars` WRITE;
/*!40000 ALTER TABLE `Extracurriculars` DISABLE KEYS */;
/*!40000 ALTER TABLE `Extracurriculars` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Family_Background`
--

DROP TABLE IF EXISTS `Family_Background`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Family_Background` (
  `Student_ID` varchar(10) NOT NULL,
  `Internet_Access_at_Home` tinyint(1) DEFAULT NULL,
  `Parent_Education_Level` varchar(50) DEFAULT NULL,
  `Family_Income_Level` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Student_ID`),
  CONSTRAINT `Family_Background_ibfk_1` FOREIGN KEY (`Student_ID`) REFERENCES `Students` (`Student_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Family_Background`
--

LOCK TABLES `Family_Background` WRITE;
/*!40000 ALTER TABLE `Family_Background` DISABLE KEYS */;
/*!40000 ALTER TABLE `Family_Background` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Student_Audit_Log`
--

DROP TABLE IF EXISTS `Student_Audit_Log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Student_Audit_Log` (
  `Log_ID` int NOT NULL AUTO_INCREMENT,
  `Student_ID` varchar(10) DEFAULT NULL,
  `Old_Email` varchar(100) DEFAULT NULL,
  `New_Email` varchar(100) DEFAULT NULL,
  `Change_Time` datetime DEFAULT NULL,
  `Action` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Log_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Student_Audit_Log`
--

LOCK TABLES `Student_Audit_Log` WRITE;
/*!40000 ALTER TABLE `Student_Audit_Log` DISABLE KEYS */;
/*!40000 ALTER TABLE `Student_Audit_Log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Students`
--

DROP TABLE IF EXISTS `Students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Students` (
  `Student_ID` varchar(10) NOT NULL,
  `First_Name` varchar(50) DEFAULT NULL,
  `Last_Name` varchar(50) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Gender` char(1) DEFAULT NULL,
  `Age` int DEFAULT NULL,
  PRIMARY KEY (`Student_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Students`
--

LOCK TABLES `Students` WRITE;
/*!40000 ALTER TABLE `Students` DISABLE KEYS */;
/*!40000 ALTER TABLE `Students` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'REAL_AS_FLOAT,PIPES_AS_CONCAT,ANSI_QUOTES,IGNORE_SPACE,ONLY_FULL_GROUP_BY,ANSI,STRICT_ALL_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`avnadmin`@`%`*/ /*!50003 TRIGGER `LogEmailChange` BEFORE UPDATE ON `Students` FOR EACH ROW BEGIN
    -- Check if the email is being changed
    IF OLD.Email != NEW.Email THEN
        INSERT INTO Student_Audit_Log (Student_ID, Old_Email, New_Email, Change_Time, Action)
        VALUES (OLD.Student_ID, OLD.Email, NEW.Email, NOW(), 'Email Updated');
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `Study_Habits`
--

DROP TABLE IF EXISTS `Study_Habits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Study_Habits` (
  `Student_ID` varchar(10) NOT NULL,
  `Study_Hours_per_Week` int DEFAULT NULL,
  `Sleep_Hours_per_Night` decimal(3,1) DEFAULT NULL,
  `Stress_Level` int DEFAULT NULL,
  PRIMARY KEY (`Student_ID`),
  CONSTRAINT `Study_Habits_ibfk_1` FOREIGN KEY (`Student_ID`) REFERENCES `Students` (`Student_ID`),
  CONSTRAINT `Study_Habits_chk_1` CHECK ((`Stress_Level` between 1 and 10))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Study_Habits`
--

LOCK TABLES `Study_Habits` WRITE;
/*!40000 ALTER TABLE `Study_Habits` DISABLE KEYS */;
/*!40000 ALTER TABLE `Study_Habits` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'ml_db_design'
--
/*!50003 DROP PROCEDURE IF EXISTS `AddNewStudent` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'REAL_AS_FLOAT,PIPES_AS_CONCAT,ANSI_QUOTES,IGNORE_SPACE,ONLY_FULL_GROUP_BY,ANSI,STRICT_ALL_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER="avnadmin"@"%" PROCEDURE "AddNewStudent"(
    IN p_Student_ID VARCHAR(10),
    IN p_First_Name VARCHAR(50),
    IN p_Last_Name VARCHAR(50),
    IN p_Email VARCHAR(100),
    IN p_Gender CHAR(1),
    IN p_Age INT,
    IN p_Department VARCHAR(50),
    IN p_Attendance_Percentage DECIMAL(5,2),
    IN p_Midterm_Score DECIMAL(5,2),
    IN p_Final_Score DECIMAL(5,2),
    IN p_Assignments_Avg DECIMAL(5,2),
    IN p_Quizzes_Avg DECIMAL(5,2),
    IN p_Participation_Score DECIMAL(5,2),
    IN p_Projects_Score DECIMAL(5,2),
    IN p_Total_Score DECIMAL(5,2),
    IN p_Grade CHAR(2),
    IN p_Study_Hours_per_Week INT,
    IN p_Sleep_Hours_per_Night DECIMAL(3,1),
    IN p_Stress_Level INT,
    IN p_Extracurricular_Activities BOOLEAN,
    IN p_Internet_Access_at_Home BOOLEAN,
    IN p_Parent_Education_Level VARCHAR(50),
    IN p_Family_Income_Level VARCHAR(50)
)
BEGIN
    -- Declare a handler for SQL exceptions
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
        ROLLBACK;

    -- Start a transaction
    START TRANSACTION;

    -- Insert into Students table
    INSERT INTO Students (Student_ID, First_Name, Last_Name, Email, Gender, Age)
    VALUES (p_Student_ID, p_First_Name, p_Last_Name, p_Email, p_Gender, p_Age);

    -- Insert into Academic_Details table
    INSERT INTO Academic_Details (
        Student_ID, Department, Attendance_Percentage, Midterm_Score, Final_Score,
        Assignments_Avg, Quizzes_Avg, Participation_Score, Projects_Score, Total_Score, Grade
    )
    VALUES (
        p_Student_ID, p_Department, p_Attendance_Percentage, p_Midterm_Score, p_Final_Score,
        p_Assignments_Avg, p_Quizzes_Avg, p_Participation_Score, p_Projects_Score, p_Total_Score, p_Grade
    );

    -- Insert into Study_Habits table
    INSERT INTO Study_Habits (Student_ID, Study_Hours_per_Week, Sleep_Hours_per_Night, Stress_Level)
    VALUES (p_Student_ID, p_Study_Hours_per_Week, p_Sleep_Hours_per_Night, p_Stress_Level);

    -- Insert into Extracurriculars table
    INSERT INTO Extracurriculars (Student_ID, Extracurricular_Activities)
    VALUES (p_Student_ID, p_Extracurricular_Activities);

    -- Insert into Family_Background table
    INSERT INTO Family_Background (
        Student_ID, Internet_Access_at_Home, Parent_Education_Level, Family_Income_Level
    )
    VALUES (p_Student_ID, p_Internet_Access_at_Home, p_Parent_Education_Level, p_Family_Income_Level);

    -- Commit the transaction if all inserts succeed
    COMMIT;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-09  5:05:11
