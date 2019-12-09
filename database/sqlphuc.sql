use company
use elearning
Go;
drop procedure danhsachCauHoiChiMotLuaChon;
delete from Options;
-- Ca Nhan 
--  1/ procedure insert options
CREATE PROCEDURE ins_option
    @QuestionID CHAR(8),
    @OptionID CHAR(3),
    @Content NVARCHAR(500),
    @res char(1)
AS
BEGIN
    IF NOT EXISTS (SELECT *
    FROM Question
    WHERE qid = @QuestionID)
        BEGIN
        RAISERROR(N'Lỗi: không có câu hỏi này trong cơ sở dữ liệu',11,1)
        Return
    END
    IF EXISTS (SELECT *
    FROM Options
    WHERE onumber = @OptionID)
    BEGIN
        RAISERROR(N'Lỗi: option này đã có trong trong cơ sở dữ liệu',11,1)
        Return
    END
    IF len(@Content)>300
    BEGIN
        RAISERROR(N'Lỗi: Đáp án quá dài, phải không quá 300 kí tự',11,1)
        Return
    END
    IF @res <> 'T' and @res <> 'F'
    BEGIN
        RAISERROR(N'Lỗi: không đúng giá trị cần nhập, phải là T hoặc F',11,1)
        Return
    END   
    ELSE 
    BEGIN
        INSERT INTO options
            (qid, onumber, content,result)
        VALUES
            (@QuestionID, @OptionID, @Content, @res);
    END
END;
GO;
EXEC ins_option  @QuestionID = 'Q501',
    @OptionID = '004',
    @Content = N'thấp dần từ Bắc xuống Nam',
    @res = 'T';
EXEC ins_option  @QuestionID = 'Q502',
    @OptionID = '005',
    @Content = N'Nằm xa Xích đạo nhất cả nước ',
    @res = 'F';
GO;

CREATE PROCEDURE ins_question
    @QuestionID CHAR(8),
    @Content NVARCHAR(500),
    @mark Int,
    @examID CHAR(5)
AS
BEGIN
    IF EXISTS (SELECT *
    FROM Question
    WHERE qid = @QuestionID)
        BEGIN
        RAISERROR(N'Lỗi: mã câu hỏi đã có trong cơ sở dữ liệu',11,1)
        Return
    END
    IF NOT EXISTS (SELECT *
    FROM Examination
    WHERE eid = @examID)
    BEGIN
        RAISERROR(N'Lỗi: Bài thi này chưa có trong trong cơ sở dữ liệu',11,1)
        Return
    END
    IF len(@Content)>300
    BEGIN
        RAISERROR(N'Lỗi:câu hỏi quá dài, phải không quá 300 kí tự',11,1)
        Return
    END
    IF @mark < 0 
    BEGIN
        RAISERROR(N'Lỗi: không đúng giá trị cần nhập, phải lớn hơn 0',11,1)
        Return
    END   
    ELSE 
    BEGIN
        insert into Question
            (qid,content,mark,examid)
        VALUES
            (@QuestionID, @Content, @mark, @examID);
    END
END;
GO;

EXEC ins_question  @QuestionID = 'Qs1',
    @Content = N'Mức cường độ âm nào đạt đến ngưỡng đau, tất cả các tần số âm đều gây cho tai người cảm giác đau',
    @mark =3,
    @examID = 'Ex001';

EXEC ins_question  @QuestionID = 'Qs2',
    @Content = N'Khi muốn nói về sóng âm, phát biểu nào sau đây là sai?',
    @mark =5,
    @examID = 'Ex002';


-- ALTER TABLE Examination add totalMark int
-- DEFAULT
-- (0);
go;
-- 2/ trigger 1
CREATE TRIGGER trg_after_ins_question
ON  Question
AFTER
INSERT,UPDATE
AS
BEGIN
    UPDATE Examination
    SET totalMark = totalMark + (
    Select mark
    FROM
        inserted
    )
    WHERE eid = (
    Select examid
    FROM
        inserted
    )
END
GO;

delete from Question where qid='Qs1'
delete from Question where qid='Qs2'
-- trigger 2
use elearning;
GO;
CREATE TRIGGER trg_before_delete_question
ON Question
INSTEAD OF
DELETE
AS
BEGIN
    UPDATE Examination
    SET totalMark = totalMark - (
    Select mark
    FROM
        deleted
    )
    WHERE eid = (
    Select examid
    FROM
        deleted
    )
    DELETE Question  FROM DELETED D
        INNER JOIN Question T ON T.qid = D.qid;
END
GO;
-- trigger 3
use elearning;
GO;
CREATE TRIGGER trg_after_insert_examop
ON ExamOption
AFTER
INSERT,UPDATE
AS
BEGIN
    DECLARE @result INT
    SELECT @result = dbo.tinhDiemCauTraLoi(inserted.studentid,inserted.eid,inserted.qid,inserted.onumber)
    from inserted
    UPDATE ExamOption
    SET mark = @result
    from inserted
    WHERE ExamOption.studentid=inserted.studentid and ExamOption.eid=inserted.eid and ExamOption.qid=inserted.qid and ExamOption.onumber=inserted.onumber
;
END
GO;

-- DROP TRIGGER trg_after_insert_examop;  
DELETE FROM Question where qid='cauhoi10'; 
Go;
-- 3/ procedure 1 xem danh sách đáp án thí sinh chọn
create procedure danhsachCauTraLoi(@makythi CHAR(5),
    @mahocvien int)
as
begin
    select eid, studentid, Question.qid, Question.content as CauHoi, Options.content as DapAn
    from Question join ExamOption
        on Question.qid=ExamOption.qid
        left join Options on ExamOption.onumber=Options.onumber and ExamOption.qid=Options.qid
    Where ExamOption.studentid=@mahocvien and ExamOption.eid = @makythi
    ORDER BY Question.qid
end;
GO;
EXEC danhsachCauTraLoi @makythi='ex001',
@mahocvien = 100002
,
@mahocvien=312314214
GO;

-- procedure 2 xem danh sách đáp án của bài thi
create procedure danhsachCauHoiChiMotLuaChon(@makythi CHAR(5))
as
begin
    select Question.qid, COUNT(Options.onumber) as soLuaChon
    from Question JOIN Options on Question.qid=Options.qid
    WHERE Question.examid=@makythi
    GROUP BY Question.qid
    HAVING COUNT(Options.onumber)<2
end
GO;
EXEC danhsachCauHoiChiMotLuaChon @makythi='ex001'
GO;

-- procedure 3 xem danh sách đáp án của bài thi
create procedure danhsachCauHoiCuaKiThi(@makythi CHAR(5))
as
begin

    select Question.qid, Question.content as question, Options.content as answer, Question.mark as mark
    from Question Full outer JOIN Options on Question.qid=Options.qid
    WHERE Question.examid=@makythi and (Options.result='T' or Options.result is NULL)
end
Go;
EXEC danhsachCauHoiCuaKiThi @makythi='ex001';
GO;

select Question.qid, Question.content as question, Options.content as answer, Question.mark as mark
from Question Full outer JOIN Options on Question.qid=Options.qid
WHERE Question.examid='ex001' and (Options.result='T' or Options.result is NULL)
-- 4/ Create Function  1
CREATE FUNCTION tinhDiemCauTraLoi
( @masv int , @makithi CHAR(5),@macauhoi CHAR(8), @madapan CHAR(3))
RETURNS INT
AS
BEGIN
    DECLARE @markReceive INT
    DECLARE @result CHAR(1)
    SELECT @result = result
    from
        (Select *
        From ExamOption
        WHERE eid=@makithi and studentid=@masv and qid =@macauhoi and onumber = @madapan) a inner join OPTIONs b on (a.onumber=b.onumber and a.qid=b.qid)
    IF @result = 'T'
    BEGIN
        select @markReceive=mark
        from Question
        WHERE qid=@macauhoi
    END
    ELSE
    BEGIN
        SET @markReceive=0
    END
    return @markReceive
END;
GO;







select dbo.tinhDiemCauTraLoi(100002,'ex001','Q501','004');
select dbo.tinhDiemCauTraLoi(100002,'ex001','Q502','005');








GO;

drop FUNCTION tinhDiemTruocThoiDiem
go;
-- function 2
CREATE FUNCTION tinhDiemTruocThoiDiem
(@mauser int,@makithi CHAR(5),@hanchot DATETIME)
RETURNS int
AS
BEGIN
    DECLARE @thoigiannopbai datetime
    DECLARE @result int
    select @thoigiannopbai = takentime
    from Exam
    where userid=@mauser and examid=@makithi
    if DATEDIFF(DAY, @thoigiannopbai,@hanchot) > 0
    BEGIN
        set @result = -1
    END
    else 
    BEGIN
        IF EXISTS (SELECT *
        from ExamOption
        Where ExamOption.eid=@makithi and ExamOption.studentid=@mauser)
        BEGIN
            SELECT @result=sum(mark)
            from ExamOption
            Where ExamOption.eid=@makithi and ExamOption.studentid=@mauser
        END
        ELSE
        BEGIN
            set @result=0
        END
    END
    return @result
END;
GO;




select dbo.tinhDiemTruocThoiDiem(100002, 'ex001', '2019-12-12 5:40:29')

















use elearning
SELECT *
from dbo.Examination
where courseid=1012345

select *
from Examination
where courseid=1012345

select *
from Examination
where courseid=1012345