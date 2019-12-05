CREATE TABLE Users(
	userid CHAR(7) NOT NULL,
	uname VARCHAR(20) NOT NULL,
	sex CHAR(1),
	bdate date,
	address NVARCHAR(30),
	password CHAR(32) NOT NULL,
	username NVARCHAR(30) NOT NULL,
	PRIMARY KEY (userid),
);

CREATE TABLE Phone(
	userid CHAR(7) NOT NULL,
	phone VARCHAR(11),
	PRIMARY KEY (userid),
);

CREATE TABLE Student(
	studentid CHAR(7) NOT NULL,
	studenttype CHAR(1),
	trialID CHAR(5),
	expireddate date,
	PRIMARY KEY (studentid),
);

CREATE TABLE Teacher(
	teacherid CHAR(7) NOT NULL,
	balance DECIMAL (10,2),
	PRIMARY KEY (teacherid),
);


CREATE TABLE Topic(
	tid CHAR(5) NOT NULL,
	tname NVARCHAR(30),
	tdesc NVARCHAR(200),
	PRIMARY KEY (tid),
);

CREATE TABLE Curriculum(
	curriid CHAR(5) NOT NULL,
	curriname NVARCHAR(30),
	curridesc NVARCHAR(200),
	PRIMARY KEY (curriid),
);

CREATE TABLE Course(
	courseid CHAR(5) NOT NULL,
	cname NVARCHAR(50),
	cdesc NVARCHAR(300),
	cstatus CHAR(1),
	price DECIMAL(8,2),
	PRIMARY KEY (courseid),
);

CREATE TABLE Teach(
	teacherid CHAR(7) NOT NULL,
	courseid CHAR(5) NOT NULL,
	PRIMARY KEY (teacherid,courseid),
);

CREATE TABLE Curricourse(
	curid CHAR(5) NOT NULL,
	courseid CHAR(5) NOT NULL,
	PRIMARY KEY(curid,courseid),
);

CREATE TABLE Topiccourse(
	topicid CHAR(5) NOT NULL,
	courseid CHAR(5) NOT NULL,
	PRIMARY KEY (topicid,courseid),
);

CREATE TABLE Enroll(
	studentid CHAR(7) NOT NULL,
	courseid CHAR(5) NOT NULL,
	epoint DECIMAL (2,2),
	PRIMARY KEY(studentid,courseid),
);

CREATE TABLE Assessment(
	studentid CHAR(7) NOT NULL,
	courseid CHAR (5) NOT NULL,
	apoint DECIMAL(2,2),
	PRIMARY KEY(studentid,courseid),
);

CREATE TABLE Lesson(
	courseid CHAR(5) NOT NULL,
	lid CHAR(2) NOT NULL,
	lname NVARCHAR(300),
	PRIMARY KEY(courseid,lid),
)

CREATE TABLE Document(
	courseid CHAR(5) NOT NULL,
	lid CHAR(2) NOT NULL,
	docid CHAR(2) NOT NULL,
	link VARCHAR(100),
	PRIMARY KEY (courseid,lid,docid),
);

CREATE TABLE Dicussion(
	dicid CHAR(5) NOT NULL,
	userid CHAR(7) NOT NULL,
	courseid CHAR(5) NOT NULL,
	startdate DATE,
	content NVARCHAR(500),
	PRIMARY KEY (dicid),
);

CREATE TABLE Comment(
	dicid CHAR(5) NOT NULL,
	commentid CHAR(5) NOT NULL,
	content NVARCHAR(500),
	ctime datetime,
	PRIMARY KEY(dicid,commentid),
);

CREATE TABLE Examination(
	eid CHAR(5) NOT NULL,
	courseid CHAR(5) NOT NULL,
	PRIMARY KEY (eid),
);

CREATE TABLE Exam(
	examid CHAR(5) NOT NULL,
	userid CHAR(7) NOT NULL,
	takentime datetime,
	PRIMARY KEY (examid,userid),
);

CREATE TABLE Question(
	qid CHAR(8) NOT NULL,
	content NVARCHAR(500),
	point DECIMAL(2,2),
	PRIMARY KEY (qid),
);

CREATE TABLE ExaminationQuestion(
	eid CHAR(5) NOT NULL,
	qid CHAR(8) NOT NULL,
	PRIMARY KEY (eid,qid),
);


CREATE TABLE Options(
	qid CHAR(8) NOT NULL,
	onumber CHAR(3),
	content NVARCHAR(500),
	result CHAR(1),
	PRIMARY KEY (qid,onumber),
);

CREATE TABLE ExamOption(
	eid CHAR(5) NOT NULL,
	studentid CHAR(7) NOT NULL,
	onumber CHAR(3),
	qid CHAR(8),
	examresult DECIMAL(2,2),
	PRIMARY KEY (eid,studentid,onumber,qid),
);