
create database elearning;
use elearning;
delete from options;
CREATE TABLE Users
(
	userid int IDENTITY(1,1) NOT NULL,
	uname VARCHAR(20) NOT NULL,
	sex CHAR(1),
	bdate date,
	address NVARCHAR(30),
	password CHAR(32) NOT NULL,
	username NVARCHAR(30) NOT NULL,
	PRIMARY KEY (userid),
);

<<<<<<< HEAD
CREATE TABLE Phone(
<<<<<<< HEAD:database/createass2.sql
=======
CREATE TABLE Phone
(
>>>>>>> origin/HPhuc
	userid int NOT NULL,
=======
	phoneid INT IDENTITY(1,1) NOT NULL,
	userid INT NOT NULL,
>>>>>>> trucdatabase:createass2.sql
	phone VARCHAR(11),
	PRIMARY KEY (phoneid),
);

CREATE TABLE Student
(
	studentid int NOT NULL,
	studenttype CHAR(1),
	trialid int,
	expireddate date,
	PRIMARY KEY (studentid),
);

CREATE TABLE Teacher
(
	teacherid int NOT NULL,
	balance DECIMAL (10,2),
	PRIMARY KEY (teacherid),
);


CREATE TABLE Topic
(
	tid int IDENTITY(1,1) NOT NULL,
	tname NVARCHAR(30),
	tdesc NVARCHAR(200),
	PRIMARY KEY (tid),
);

CREATE TABLE Curriculum
(
	curriid int IDENTITY(1,1) NOT NULL,
	curriname NVARCHAR(30),
	curridesc NVARCHAR(200),
	PRIMARY KEY (curriid),
);

CREATE TABLE Course
(
	courseid int NOT NULL,
	cname NVARCHAR(50),
	cdesc NVARCHAR(300),
	rate DECIMAL(1,1),
	price DECIMAL(8,2),
	PRIMARY KEY (courseid),
);

CREATE TABLE Teach
(
	teacherid int NOT NULL,
	courseid int NOT NULL,
	PRIMARY KEY (teacherid,courseid),
);

CREATE TABLE Curricourse
(
	curid int NOT NULL,
	courseid int NOT NULL,
	PRIMARY KEY(curid,courseid),
);

CREATE TABLE Topiccourse
(
	topicid int NOT NULL,
	courseid int NOT NULL,
	PRIMARY KEY (topicid,courseid),
);

CREATE TABLE Enroll
(
	studentid int NOT NULL,
	courseid int NOT NULL,
	epoint DECIMAL (2,2),
	PRIMARY KEY(studentid,courseid),
);

CREATE TABLE Assessment
(
	studentid int NOT NULL,
	courseid int NOT NULL,
	apoint DECIMAL(2,2),
	PRIMARY KEY(studentid,courseid),
);

CREATE TABLE Lesson
(
	courseid int NOT NULL,
	lid int IDENTITY(1,1) NOT NULL,
	lname NVARCHAR(300),
	PRIMARY KEY(courseid,lid),
)

CREATE TABLE Document
(
	courseid int NOT NULL,
	lid int NOT NULL,
	docid int IDENTITY(1,1) NOT NULL,
	link VARCHAR(100),
	PRIMARY KEY (courseid,lid,docid),
);

CREATE TABLE Dicussion
(
	dicid int IDENTITY(1,1) NOT NULL,
	userid int NOT NULL,
	courseid int NOT NULL,
	startdate DATE,
	content NVARCHAR(500),
	PRIMARY KEY (dicid),
);

CREATE TABLE Comment
(
	dicid int NOT NULL,
	commentid int IDENTITY(1,1) NOT NULL,
	content NVARCHAR(500),
	ctime datetime,
	PRIMARY KEY(dicid,commentid),
);
CREATE TABLE Examination
(
	eid CHAR(5) NOT NULL,
	courseid Int NOT NULL,
	totalMark INT,
	PRIMARY KEY (eid),
);
CREATE TABLE Exam
(
	examid CHAR(5) NOT NULL,
	userid int NOT NULL,
	takentime datetime DEFAULT GETDATE(),
	PRIMARY KEY (examid,userid),
);


CREATE TABLE Question
(
	qid CHAR(8) NOT NULL,
	content NVARCHAR(300),
	mark INT,
	examid CHAR(5) NOT NULL,
	PRIMARY KEY (qid),
);
<<<<<<< HEAD
ALTER TABLE question ADD CONSTRAINT fk_exam FOREIGN KEY (examid) REFERENCES Examination(eid);

=======
>>>>>>> origin/HPhuc

CREATE  INDEX question_index
ON Question(qid);

CREATE TABLE Options
(
	qid CHAR(8) NOT NULL,
	onumber CHAR(3),
	content NVARCHAR(300),
	result CHAR(1),
	PRIMARY KEY (qid,onumber),
);




CREATE TABLE ExamOption
(
	eid CHAR(5) NOT NULL,
	studentid int NOT NULL,
	onumber CHAR(3),
	qid CHAR(8),
	mark INT,
	PRIMARY KEY (eid,studentid,onumber,qid),
);

<<<<<<< HEAD

=======
ALTER TABLE Exam ADD CONSTRAINT fk_user_exam FOREIGN KEY (examid) REFERENCES Examination(eid);
ALTER TABLE question ADD CONSTRAINT fk_exam FOREIGN KEY (examid) REFERENCES Examination(eid) ON DELETE CASCADE;
ALTER TABLE Options ADD CONSTRAINT fk_op_question FOREIGN KEY (qid) REFERENCES Question(qid)  ON DELETE CASCADE;
ALTER TABLE ExamOption ADD CONSTRAINT fk_EO_exam FOREIGN KEY (eid,studentid) REFERENCES Exam(examid,userid);
ALTER TABLE ExamOption ADD CONSTRAINT fk_EO_question FOREIGN KEY (qid,onumber) REFERENCES Options(qid,onumber);
>>>>>>> origin/HPhuc
