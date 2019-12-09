
ALTER TABLE Lesson
 ADD CONSTRAINT fk_lesson_course_couseid FOREIGN KEY (courseid)
 REFERENCES course (courseid) 

 ALTER TABLE topiccourse
 ADD CONSTRAINT fk_topiccourse_course_courseid FOREIGN KEY (courseid)
 REFERENCES course (courseid)

 ALTER TABLE curricourse
 ADD CONSTRAINT fk_curricourse_course_courseid FOREIGN KEY (courseid)
 REFERENCES course(courseid)
 
 ALTER TABLE curricourse
 ADD CONSTRAINT fk_curricourse_curriculum_curid FOREIGN KEY (curid)
 REFERENCES curriculum(curriid)

 ALTER TABLE topiccourse
 ADD CONSTRAINT fk_curricourse_topic_tid FOREIGN KEY (topicid)
 REFERENCES topic(tid)

/*ALTER TABLE course
 ADD CONSTRAINT checkPrice 
 CHECK (price >= 0)

 ALTER TABLE course
 ADD CONSTRAINT checkRate 
 CHECK (rate >= 0.0 AND rate <= 5.0)*/

  /*INSERT INTO Course VALUES (1000,N'Python cơ bản',N'Làm quen và nắm bắt những kiến thức căn bản của Python',0.0,300000.00)
  INSERT INTO Course VALUES (1001,N'Thuật toán trong Machine Learning',N'Giới thiệu các thuật toán phổ biến trong Machine Learning dành cho newbie',0.0,900000.00)
  INSERT INTO Course VALUES (1002,N'Model trong Deep Learning',N'Nhập môn Deep Learning bằng việc làm quen với các model như CNN, RNN, LSTM',0.0,650000.00)
  INSERT INTO Course VALUES (1003,N'Xử lý và phân tích data',N'Học xử lý data bằng Pandas và analysis bằng Matplot hay Seaborn',0.0,500000.00)
  INSERT INTO Course VALUES (1004,N'Phát âm như người bản xứ',N'Học phát âm tiếng Anh chuẩn xác và tự nhiên với giáo viên là người bản địa',0.0,750000.00)
  INSERT INTO Course VALUES (1005,N'Ngữ pháp tiếng Anh căn bản',N'Tổng hợp ngữ pháp Tiếng Anh sử dụng phổ biến',0.0,300000.00)
  INSERT INTO Course VALUES (1006,N'AI cho Robotics',N'Học cách lập trình AI cho robot',0.0,999999.99)
  INSERT INTO Course VALUES (1007,N'600 từ vựng căn bản',N'600 từ vựng cần thiết và căn bản phải biết trong Toeic',0.0,400000.00)
  INSERT INTO Course VALUES (1008,N'Luyện phát âm căn bản',N'Học phát âm 44 âm cơ bản tự nhiên và chuẩn xác',0.0,400000.00)
  INSERT INTO Course VALUES (1009,N'Nghe tiếng Anh căn bản',N'Hướng dẫn kĩ năng nghe và luyện nghe những đoạn hội thoại về những chủ đề phổ biến',0.0,600000.00)
  INSERT INTO Course VALUES (1010,N'Nhập môn Machine Learning',N'Giới thiệu và làm quen các kiến thức căn bản một cách tổng quát về Machine Learning',0.0,999999.99)
  INSERT INTO Course VALUES (1011,N'Từ vựng theo chủ đề Kinh tế',N'Nắm vững các từ vựng liên quan đến kinh tế thị trường và cách sử dụng phù hợp trong môi trường làm việc',0.0,300000.00)*/

  --Select * from course
  

  /*INSERT INTO Lesson VALUES (1001,N'Linear Regression')
  INSERT INTO Lesson VALUES (1001,N'Linear Discriminant Analysis')
  INSERT INTO Lesson VALUES (1002,N'Giới thiệu model CNN')
  INSERT INTO Lesson VALUES (1000,N'Array trong Python')
  INSERT INTO Lesson VALUES (1000,N'Numpy trong Python')
  INSERT INTO Lesson VALUES (1003,N'Xử lý data bằng Pandas')
  INSERT INTO Lesson VALUES (1003,N'Phân tích data bằng Matplot')
  INSERT INTO Lesson VALUES (1005,N'Thì hiện tại đơn')
  INSERT INTO Lesson VALUES (1005,N'Comparison')
  INSERT INTO Lesson VALUES (1011,N'Từ vựng lĩnh vực Chứng khoán')
  INSERT INTO Lesson VALUES (1011,N'Từ vựng lĩnh vực Bất động sản')
  INSERT INTO Lesson VALUES (1005,N'Câu bị động')
  INSERT INTO Lesson VALUES (1000,N'Matrix trong Python')
  INSERT INTO Lesson VALUES (1002,N'Giới thiệu model RNN')
  INSERT INTO Lesson VALUES (1002,N'Giới thiệu model LSTM')
  INSERT INTO Lesson VALUES (1000,N'Naive Bayes') */

  --Select * from lesson

  /*INSERT INTO Curriculum VALUES (N'Lộ trình học Machine Learning',N'Một cách học Machine learning thật hiệu quả cho các bạn không có kinh nghiệm nghiên cứu khoa học')
  INSERT INTO Curriculum VALUES (N'Lộ trình học Toeic 300+',N'Lộ trình học Toeic hiệu quả dành cho những bạn mất gốc tiếng Anh')

  INSERT INTO Topic VALUES (N'Trí tuệ nhân tạo',N'Những trí tuệ có thể tư duy, suy nghĩ, học hỏi như trí tuệ con người; xử lý dữ liệu ở mức rộng lớn hơn, quy mô hơn, hệ thống, khoa học và nhanh hơn so với con người')
  INSERT INTO Topic VALUES (N'Ngoại ngữ Anh-Mỹ',N'Một trong những ngôn ngữ thông dụng nhất quốc tế, phương tiện giao tiếp của những con người đến từ những quốc gia khác nhau') */
  
  --Select * from topic

  --Select * from curriculum

  /*INSERT INTO Curricourse VALUES (1,1000)
  INSERT INTO Curricourse VALUES (1,1001)
  INSERT INTO Curricourse VALUES (1,1002)
  INSERT INTO Curricourse VALUES (1,1003)

  INSERT INTO Curricourse VALUES (2,1005)
  INSERT INTO Curricourse VALUES (2,1007)
  INSERT INTO Curricourse VALUES (2,1008)
  INSERT INTO Curricourse VALUES (2,1009)

  INSERT INTO Topiccourse VALUES (1,1002)
  INSERT INTO Topiccourse VALUES (1,1003)
  INSERT INTO Topiccourse VALUES (1,1006)
  INSERT INTO Topiccourse VALUES (1,1010)
 
  INSERT INTO Topiccourse VALUES (2,1004)
  INSERT INTO Topiccourse VALUES (2,1005)
  INSERT INTO Topiccourse VALUES (2,1011)*/

  
  --select * from curricourse
  --select * from topiccourse

  -- PHẦN RIÊNG
  --- TẠO PROCEDURE INSERT COURSE 
   CREATE PROC Insert_Data_to_Course (
  @cname NVARCHAR(50) ,
  @cdesc NVARCHAR(300),
  @price NVARCHAR(30)
  )
  AS
	BEGIN TRY
		DECLARE @courseid int;
		SELECT @courseid = max(courseid) from Course;
		SELECT @courseid = @courseid + 1;
		DECLARE @temp DECIMAL(8,2);
		SET @temp = CONVERT(DECIMAL(8,2),@price)
		IF len(@cname) < 5 OR len(@cdesc) < 5
			BEGIN
			RAISERROR('LENGTH OF YOUR NAME (OR YOUR DESCRIPTION) IS TOO SHORT ',1,1)
			RETURN
			END
		INSERT INTO Course VALUES (@courseid,@cname,@cdesc,@temp,0.0);
	END TRY
	BEGIN CATCH
		SELECT ERROR_MESSAGE() AS ERROR_MESS
	END CATCH
  /*CREATE PROC Insert_Data_to_Course (
  @cname NVARCHAR(50) ,
  @cdesc NVARCHAR(300),
  @price DECIMAL(8,2)
  )
  AS
	BEGIN TRY
		
		DECLARE @courseid int;
		SELECT @courseid = max(courseid) from Course;
		SELECT @courseid = @courseid + 1;
		INSERT INTO Course VALUES (@courseid,@cname,@cdesc,0.0,@price);
	END TRY
	BEGIN CATCH
		SELECT ERROR_MESSAGE() AS ERROR_MESS
	END CATCH
	*/

	--EXEC Insert_Data_to_Course N'Python nâng cao', N'Học kiến thức nâng cao của Python','999999.99'
	

	--EXEC Insert_Data_to_Course N'Ngữ pháp tiếng anh nâng cao', N'Tiếp cận những ngữ pháp Tiếng Anh sử dụng trong kì thi IELTS','900000.00'
	--Select * from course

	--------------------------------------------------------------------------------------------------------------
	-- TẠO TRIGGER
	--1. Tạo trigger kiểm soát giá trong khóa học, nếu insert hoặc update giá khóa học thấp hơn 100000.00, không cho update hoặc insert.
	/*CREATE TRIGGER abc ON course after insert as
	begin
	if (exists(select * from inserted as i join course as t on i.cname = t.cname))
	begin
	raiserror ('hihihi',1,1)
	end
	end */

	--drop trigger abc;
	--2. Tạo trigger kiểm soát rate, nếu số lượng học viên enroll khóa học đó trên 20 học viên, rate tự động tăng lên 1.0

	----------------------------------------------------------------------------------------------------------------

	-- TẠO PROCEDURE INCLUDING QUERY
	--(tham số đầu vào lấy giá trị nằm trong where)
	--1. Tạo query sắp xếp những khóa học trong Chủ đề theo giá tiền giảm dần. (input là chủ đề)
	/*CREATE PROC Query_1(
	@tname NVARCHAR(30)
	)
	AS
	BEGIN
	DECLARE @idTopic int;
	SELECT @idTopic = tid from Topic WHERE	tname = @tname;
	SELECT cname, price from Course WHERE courseid IN (Select courseid from Topiccourse where topicid = @idTopic) 
	ORDER BY price DESC;
	END */
	--SELECT tid from Topic where tname = N'Trí tuệ nhân tạo';
	--DROP PROC Query_1
	--EXEC Query_1 N'Trí tuệ nhân tạo';

	--2. Tạo query hiển thị những lộ trình có nhiều hơn Input khóa học  (Input: số lượng khóa học ).
	/*CREATE PROC Query_2(
	@number int)
	AS
	BEGIN
	SELECT curriname, COUNT(*) as num_of_course from Curriculum, Course, Curricourse 
	WHERE Curriculum.curriid = Curricourse.curid and Course.courseid = Curricourse.courseid
	GROUP BY Curriculum.curriname
	HAVING COUNT(*) > @number;
	END */

	/*SELECT curriname, Count(*) as num_course from Curriculum, Course, Curricourse where Curriculum.curriid = Curricourse.curid and Course.courseid = Curricourse.courseid
	GROUP BY Curriculum.curriname
	HAVING COUNT(*) >= 4*/

	--EXEC Query_2 5;


	/*CREATE PROC Query_3(
	@curriname NVARCHAR(30)
	)
	AS
	BEGIN
	DECLARE @idCurriculum int;
	SELECT @idCurriculum = curriid from Curriculum WHERE curriname = @curriname;
	SELECT cname, price from Course WHERE courseid IN (Select courseid from Curricourse where curid = @idCurriculum) 
	ORDER BY price DESC;
	END */

	--DROP PROC Query_3
	--EXEC Query_3 N'Lộ trình học TOEIC 300+';
	


	--------------------------------------------------------------------------------------------------------------------
	
	-- TẠO FUNCTION
	--1. Function tính tổng giá tiền cần chi để hoàn thành 1 lộ trình. (Input: Tên lộ trình) 
	/*CREATE FUNCTION dbo.count_fee(@curriname NVARCHAR(50)) 

	RETURNS	NVARCHAR(300) 
	AS

	BEGIN
		DECLARE @countSum DECIMAL(10,2);
		DECLARE @amount int;
		DECLARE @notice NVARCHAR(300);
		DECLARE @idCurriculum int;
		SELECT @idCurriculum = curriid from Curriculum WHERE curriname = @curriname;

		SELECT @amount = COUNT(*) FROM Course, Curricourse, Curriculum 
		WHERE Curriculum.curriname = @curriname AND Curricourse.curid = Curriculum.curriid 
		AND Course.courseid = Curricourse.courseid; 

		IF (@amount = 0)
			BEGIN
				SET @notice = N'Hiện tại lộ trình này chưa cập nhật khóa học, bạn vui lòng tìm kiếm lộ trình khác nhé'; 
			END
		ELSE
			BEGIN
				SELECT @countSum = SUM(price) from Course WHERE courseid IN (SELECT courseid FROM Curricourse WHERE curid = @idCurriculum);  
				SET @notice = N'Bạn sẽ đầu tư tổng cộng ' + CONVERT(nvarchar(30),@countSum) + N'vnđ để hoàn thành lộ trình này';
			END
		RETURN @notice;
	END 
	*/
	--EXEC Query_3 N'Lộ trình học TOEIC 300+';

	--SELECT dbo.count_fee(N'Lộ trình học bảng chữ cái Nhật');
	--SELECT dbo.count_fee(N'Lộ trình học TOEIC 300+');
	--INSERT INTO Curriculum VALUES (N'Lộ trình học bảng chữ cái Nhật',N'Làm quen 3 bảng chữ cái truyền thống của Nhật');
	--DROP FUNCTION dbo.count_fee;


	/*SELECT COUNT(*) FROM Course, Curricourse, Curriculum 
	where Curriculum.curriname = N'Lộ trình học TOEIC 300+' AND Curricourse.curid = Curriculum.curriid 
	AND Course.courseid = Curricourse.courseid;  */
	 

	--2. Function tính thời gian tối thiểu để hoàn thành một khóa học, giả sử trung bình mỗi lesson kéo dài 45 phút (Input: Tên course) 
	 /*CREATE FUNCTION dbo.Calculate_Time (@coursename NVARCHAR(100))
	RETURNS NVARCHAR(300)
	AS 
	BEGIN
		DECLARE @notice NVARCHAR(300);
		DECLARE @idCourse int;
		SELECT @idCourse = Course.courseid from Course WHERE Course.cname = @coursename;

		DECLARE @total_lesson int;
		SELECT @total_lesson = COUNT(*) FROM Course, Lesson 
		WHERE Course.cname = @coursename AND Course.courseid = Lesson.courseid; 
		IF @total_lesson = 0
			BEGIN
				SET @notice = N'Khóa học này hiện tại chưa cập nhật các bài học, vui lòng truy cập khóa học khác';
				RETURN @notice;
			END
		ELSE
			DECLARE @time_consuming INT;
			SET @time_consuming = 0;
			DECLARE @temp INT;
			SET @temp = 0;
	
			WHILE @temp < @total_lesson
				BEGIN
					SET @time_consuming = @time_consuming + 45;
					SET @temp = @temp + 1;
				END 

			IF (@time_consuming < 60) 
				SET @notice = N'Mất ' + CONVERT(NVARCHAR(20),@time_consuming) + N' phút để hoàn thành khóa học này';
			ELSE 
				BEGIN
					DECLARE @hour int;
					DECLARE @minute int;
					SET @hour = @time_consuming / 60;
					SET @minute = @time_consuming - 60 * @hour;
					SET @notice = N'Mất ' + CONVERT(NVARCHAR(20),@hour) + N' giờ ' + CONVERT(NVARCHAR(20),@minute) + N' phút để hoàn thành khóa học này';
				END
		RETURN @notice;
	END */
	
	--DROP FUNCTION dbo.Calculate_Time;

	--select * from users
	--insert into Users VALUES ()

	/*SELECT COUNT(*) as count_of_lesson FROM Course, Lesson 
		WHERE Course.cname = N'Thuật toán trong Machine Learning' AND Course.courseid = Lesson.courseid; */
	
	--SELECT dbo.Calculate_Time(N'Thuật toán trong Machine Learning');
	---------------------------------------------------------------------------------------------------------------------
