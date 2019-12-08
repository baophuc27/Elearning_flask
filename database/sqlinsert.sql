use elearning;
insert into Exam
    (examid,userid)
values
    ('exam3', 'ABCD000004')

insert into Examination
    (eid,courseid,totalMark)
values('exam5', 1012345, 0)



insert into Examination
    (eid,courseid,totalMark)
values('exam6', 'Java0001', 0)



insert into Question
    (qid,content,mark,examid)
values
    ('cauhoi12', N'Noji dudnsdadng uefwier', 4, 'exam3')

insert into Question
    (qid,content,mark,examid)
values
    ('cauhoi14', N'Noji dudnsdadng uefwier', 3, 'exam3')

insert into Question
    (qid,content,mark,examid)
values
    ('cauhoi15', N'Noji dudnsdadng uefwier', 2, 'exam3')

insert into Question
    (qid,content,mark,examid)
values
    ('cauhoi16', N'Noji dudnsdadng uefwier', 10, 'exam3')


insert into Options
    (qid,onumber,content,result)
values
    ('cauhoi11', '001', N'Noji dudnsdadng uefwier', 'F')
insert into Options
    (qid,onumber,content,result)
values
    ('cauhoi11', '002', N'Noji dudnsdadng uefwier', 'T')
insert into Options
    (qid,onumber,content,result)
values
    ('cauhoi11', '003', N'Noji dudnsdadng uefwier', 'F')


insert into ExamOption
    (eid,studentid,onumber,qid)
values
    ('exam3', 'ABCD000001', '002', 'cauhoi13')
insert into ExamOption
    (eid,studentid,onumber,qid)
values
    ('exam3', 'ABCD000001', '003', 'cauhoi14')

insert into ExamOption
    (eid,studentid,onumber,qid)
values
    ('exam3', 'ABCD000001', '001', 'cauhoi15')
insert into ExamOption
    (eid,studentid,onumber,qid)
values
    ('exam3', 'ABCD000001', '001', 'cauhoi16')
insert into ExamOption
    (eid,studentid,onumber,qid)
values
    ('exam3', 'ABCD000001', '001', 'cauhoi15')
insert into ExamOption
    (eid,studentid,onumber,qid)
values
    ('exam3', 'ABCD000001', '001', 'cauhoi11')
insert into ExamOption
    (eid,studentid,onumber,qid)
values
    ('exam3', 'ABCD000001', '002', 'cauhoi13')

use elearning
insert into ExamOption
    (eid,studentid,onumber,qid)
values
    ('exam3', 'ABCD000001', '003', 'cauhoi14')
insert into ExamOption
    (eid,studentid,onumber,qid)
values
    ('exam3', 'ABCD000001', '002', 'cauhoi15')
insert into ExamOption
    (eid,studentid,onumber,qid)
values
    ('exam3', 'ABCD000001', '001', 'cauhoi12')

insert into Exam
    (examid,userid,takentime)
values
    ('exam3', 'ABCD000003', '2019-12-08 12:35:29')

select dbo.tinhDiemTruocThoiDiem('exam5', 'ABCD000003', '2019-12-08 12:35:29')

insert into ExamOption
    (eid,studentid,onumber,qid)
values
    ('exam3', 'ABCD000003', '001', 'cauhoi12')
insert into ExamOption
    (eid,studentid,onumber,qid)
values
    ('exam3', 'ABCD000003', '002', 'cauhoi15')