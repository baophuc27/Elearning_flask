CREATE TABLE Users(
	userid CHAR(10) NOT NULL,
	name VARCHAR(15) NOT NULL,
	sex CHAR(1),
	bdate date,
	address VARCHAR(30),
	password CHAR(32) NOT NULL,
	username VARCHAR(15) NOT NULL,
);
CREATE TABLE Phone(
	userid CHAR(10) NOT NULL,
	phone VARCHAR(11),
);
CREATE TABLE Student(
	userid CHAR(10) NOT NULL,
	loaiHV CHAR(1),
	trialID CHAR(10),
	expireddate date,
);

CREATE TABLE Teacher(
	userid CHAR(10) NOT NULL,
	balance DECIMAL (10,2),
);


CREATE TABLE Topic(
	tid CHAR(5) NOT NULL,
	tname VARCHAR(30),
	tdesc VARCHAR(200),
);

CREATE TABLE Curriculum(
	curid CHAR(5) NOT NULL,
	cuname VARCHAR(30),
	cudesc VARCHAR(200),
);

CREATE TABLE Course(
	courseid CHAR(8) NOT NULL,
	cname VARCHAR(50),
	cdesc VARCHAR(300),
	cstatus CHAR(1),
	price DECIMAL(10,2),

);

CREATE TABLE Teach(
	userid CHAR(10) NOT NULL,
	courseid CHAR(8) NOT NULL,
);

CREATE TABLE Curricourse(
	cuserid CHAR(5) NOT NULL,
	courseid CHAR(8) NOT NULL,
);

CREATE TABLE Topiccourse(
	tid CHAR(5) NOT NULL,
	courseid CHAR(8) NOT NULL,
);

CREATE TABLE Enroll(
	userid CHAR(10) NOT NULL,
	courseid CHAR(8) NOT NULL,
	epoint DECIMAL (2,2),
);

CREATE TABLE Assessment(
	userid CHAR(10) NOT NULL,
	courseid CHAR (8) NOT NULL,
	apoint DECIMAL(2,2),
);

CREATE TABLE Lesson(
	courseid CHAR(8) NOT NULL,
	lid CHAR(2) NOT NULL,
	lname NVARCHAR,
)

CREATE TABLE Document(
	courseid CHAR(8) NOT NULL,
	lid CHAR(2) NOT NULL,
	docid CHAR(2) NOT NULL,
	link VARCHAR(100),
);

CREATE TABLE Dicussion(
	dicid CHAR(5) NOT NULL,
	userid CHAR(10) NOT NULL,
	courseid CHAR(8) NOT NULL,
	startdate DATE,
	content NVARCHAR,
);

CREATE TABLE Comment(
	courseid CHAR(8) NOT NULL,
	commentid CHAR(8) NOT NULL,
	content NVARCHAR,
	ctime datetime,
);

CREATE TABLE Examination(
	eid CHAR(5) NOT NULL,
	courseid CHAR(8) NOT NULL,
);

CREATE TABLE Exam(
	examid CHAR(5) NOT NULL,
	userid CHAR(10) NOT NULL,
	takentime datetime,
);

CREATE TABLE Question(
	qid CHAR(8) NOT NULL,
	content NVARCHAR,
	point DECIMAL(2,2),
);

CREATE TABLE ExaminationQuestion(
	eid CHAR(5) NOT NULL,
	qid CHAR(8) NOT NULL,
);

CREATE TABLE Options(
	qid CHAR(8) NOT NULL,
	onumber CHAR(3),
	content NVARCHAR,
	result CHAR(1),
);