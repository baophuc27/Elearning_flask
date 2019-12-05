CREATE TABLE Users(
	userid int NOT NULL,
	uname VARCHAR(20) NOT NULL,
	sex CHAR(1),
	bdate date,
	address NVARCHAR(30),
	password CHAR(32) NOT NULL,
	username NVARCHAR(30) NOT NULL,
	PRIMARY KEY (userid),
);

CREATE TABLE Phone(
	userid int NOT NULL,
	phone VARCHAR(11),
	PRIMARY KEY (userid),
);

CREATE TABLE Student(
	studentid int NOT NULL,
	studenttype CHAR(1),
	trialid int,
	expireddate date,
	PRIMARY KEY (studentid),
);

CREATE TABLE Teacher(
	teacherid int NOT NULL,
	balance DECIMAL (10,2),
	PRIMARY KEY (teacherid),
);


CREATE TABLE Topic(
	tid int NOT NULL,
	tname NVARCHAR(30),
	tdesc NVARCHAR(200),
	PRIMARY KEY (tid),
);

CREATE TABLE Curriculum(
	curriid int NOT NULL,
	curriname NVARCHAR(30),
	curridesc NVARCHAR(200),
	PRIMARY KEY (curriid),
);

CREATE TABLE Course(
	courseid int NOT NULL,
	cname NVARCHAR(50),
	cdesc NVARCHAR(300),
	cstatus CHAR(1),
	price DECIMAL(8,2),
	PRIMARY KEY (courseid),
);

CREATE TABLE Teach(
	teacherid int NOT NULL,
	courseid int NOT NULL,
	PRIMARY KEY (teacherid,courseid),
);

CREATE TABLE Curricourse(
	curid int NOT NULL,
	courseid int NOT NULL,
	PRIMARY KEY(curid,courseid),
);

CREATE TABLE Topiccourse(
	topicid int NOT NULL,
	courseid int NOT NULL,
	PRIMARY KEY (topicid,courseid),
);

CREATE TABLE Enroll(
	studentid int NOT NULL,
	courseid int NOT NULL,
	epoint DECIMAL (2,2),
	PRIMARY KEY(studentid,courseid),
);

CREATE TABLE Assessment(
	studentid int NOT NULL,
	courseid int NOT NULL,
	apoint DECIMAL(2,2),
	PRIMARY KEY(studentid,courseid),
);

CREATE TABLE Lesson(
	courseid int NOT NULL,
	lid int NOT NULL,
	lname NVARCHAR(300),
	PRIMARY KEY(courseid,lid),
)

CREATE TABLE Document(
	courseid int NOT NULL,
	lid int NOT NULL,
	docid int NOT NULL,
	link VARCHAR(100),
	PRIMARY KEY (courseid,lid,docid),
);

CREATE TABLE Dicussion(
	dicid int NOT NULL,
	userid int NOT NULL,
	courseid int NOT NULL,
	startdate DATE,
	content NVARCHAR(500),
	PRIMARY KEY (dicid),
);

CREATE TABLE Comment(
	dicid int NOT NULL,
	commentid int NOT NULL,
	content NVARCHAR(500),
	ctime datetime,
	PRIMARY KEY(dicid,commentid),
);

CREATE TABLE Examination(
	eid int NOT NULL,
	courseid int NOT NULL,
	PRIMARY KEY (eid),
);

CREATE TABLE Exam(
	examid int NOT NULL,
	userid int NOT NULL,
	takentime datetime,
	PRIMARY KEY (examid,userid),
);

CREATE TABLE Question(
	qid int NOT NULL,
	content NVARCHAR(500),
	point DECIMAL(2,2),
	PRIMARY KEY (qid),
);

CREATE TABLE ExaminationQuestion(
	eid int NOT NULL,
	qid int NOT NULL,
	PRIMARY KEY (eid,qid),
);


CREATE TABLE Options(
	qid int NOT NULL,
	onumber CHAR(3),
	content NVARCHAR(500),
	result CHAR(1),
	PRIMARY KEY (qid,onumber),
);

CREATE TABLE ExamOption(
	eid int NOT NULL,
	studentid int NOT NULL,
	onumber CHAR(3),
	qid int,
	examresult DECIMAL(2,2),
	PRIMARY KEY (eid,studentid,onumber,qid),
);