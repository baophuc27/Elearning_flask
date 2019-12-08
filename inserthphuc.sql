use elearning;
insert into Examination
    (eid,courseid,totalMark)
values('ex001', 1000, 0)
insert into Examination
    (eid,courseid,totalMark)
values('ex002', 1000, 0)
insert into Examination
    (eid,courseid,totalMark)
values('ex003', 1000, 0)
insert into Examination
    (eid,courseid,totalMark)
values('ex004', 1000, 0)
insert into Examination
    (eid,courseid,totalMark)
values('ex005', 1000, 0)
insert into Examination
    (eid,courseid,totalMark)
values('ex101', 1001, 0)
insert into Examination
    (eid,courseid,totalMark)
values('ex102', 1001, 0)
insert into Examination
    (eid,courseid,totalMark)
values('ex103', 1001, 0)
insert into Examination
    (eid,courseid,totalMark)
values('ex104', 1001, 0)
insert into Examination
    (eid,courseid,totalMark)
values('ex105', 1001, 0)
insert into Examination
    (eid,courseid,totalMark)
values('ex201', 1002, 0)
insert into Examination
    (eid,courseid,totalMark)
values('ex202', 1002, 0)
insert into Examination
    (eid,courseid,totalMark)
values('ex203', 1002, 0)
insert into Examination
    (eid,courseid,totalMark)
values('ex204', 1002, 0)
insert into Examination
    (eid,courseid,totalMark)
values('ex205', 1002, 0)
insert into Examination
    (eid,courseid,totalMark)
values('ex301', 1003, 0)
insert into Examination
    (eid,courseid,totalMark)
values('ex302', 1003, 0)
insert into Examination
    (eid,courseid,totalMark)
values('ex303', 1003, 0)
insert into Examination
    (eid,courseid,totalMark)
values('ex304', 1003, 0)
insert into Examination
    (eid,courseid,totalMark)
values('ex305', 1003, 0)

insert into Question
    (qid,content,mark,examid)
values
    ('Q001', N'Khi muốn nói về sóng âm, phát biểu nào sau đây là sai?', 2, 'ex001')
insert into Question
    (qid,content,mark,examid)
values
    ('Q002', N'Đối với âm cơ bản và họa âm thứ hai do cùng một cây đàn phát ra thì', 5, 'ex001')
insert into Question
    (qid,content,mark,examid)
values
    ('Q003', N'Mức cường độ âm này đạt đến ngưỡng đau, tất cả các tần số âm đều gây cho tai người cảm giác đau', 1, 'ex001')
insert into Question
    (qid,content,mark,examid)
values
    ('Q004', N'Khi muốn nói về sóng âm, phát biểu nào sau đây là sai?', 2, 'ex001')

insert into Question
    (qid,content,mark,examid)
values
    ('Q101', N' Trong chế độ khi hậu, ở miền Bắc phân chia thành 2 mùa là', 6, 'ex101')
insert into Question
    (qid,content,mark,examid)
values
    ('Q102', N'Trong chế độ khí hậu, Nam BỘ và Tây Nguyên có hai mùa rõ rệt là', 3, 'ex101')
insert into Question
    (qid,content,mark,examid)
values
    ('Q103', N'Những khi vực chịu tác động khô hạn lướn nhất ở nước ta vào mùa khô là ', 8, 'ex101')
insert into Question
    (qid,content,mark,examid)
values
    ('Q104', N'Trong chế độ khí hậu, giữa Tây Nguyên và đồng bằng ven biển Trung Trung Bộ có sự đối lập về', 1, 'ex101')
insert into Question
    (qid,content,mark,examid)
values
    ('Q201', N'Tại cùng một vị trí địa lí, nếu độ dài con lắc đơn tăng 6,25 lần, thì số dao động điều hòa của nó', 2, 'ex002')
insert into Question
    (qid,content,mark,examid)
values
    ('Q202', N'Một con lắc đơn mỗi ngày chạy chậm 1,5 phút. Cần phải điều chỉnh chiều dài con lắc như thế nào để đồng hồ chạy đúng?', 7, 'ex002')
insert into Question
    (qid,content,mark,examid)
values
    ('Q203', N' Tìm phát biểu sai về con lắc lò xo dao động trên mặt phẳng nằm ngang.', 5, 'ex002')
insert into Question
    (qid,content,mark,examid)
values
    ('Q204', N'Tìm phát biểu sai về lực kéo về tác dụng lên vật dao động điều hòa.', 4, 'ex002')

insert into Options
    (qid,onumber,content,result)
values
    ('Q001', '001', N'số proton giống nhau nhưng số nơtron khác nhau', 'T')
insert into Options
    (qid,onumber,content,result)
values
    ('Q001', '002', N'dap an sai', 'F')
insert into Options
    (qid,onumber,content,result)
values
    ('Q001', '003', N'dap an sai', 'F')
insert into Options
    (qid,onumber,content,result)
values
    ('Q002', '001', N'Mọi hạt nhân của các nguyên tử đều có chứa cả proton và nơtron.', 'T')
insert into Options
    (qid,onumber,content,result)
values
    ('Q002', '002', N'dap an sai', 'F')
insert into Options
    (qid,onumber,content,result)
values
    ('Q002', '003', N'dap an sai', 'F')
insert into Options
    (qid,onumber,content,result)
values
    ('Q003', '001', N' Tăng k ba lần, giảm m ba lần.', 'T')
insert into Options
    (qid,onumber,content,result)
values
    ('Q003', '002', N'dap an sai', 'F')
insert into Options
    (qid,onumber,content,result)
values
    ('Q003', '003', N'dap an sai', 'F')
insert into Options
    (qid,onumber,content,result)
values
    ('Q004', '001', N' 0.5Hz', 'T')
insert into Options
    (qid,onumber,content,result)
values
    ('Q004', '002', N'dap an sai', 'F')
insert into Options
    (qid,onumber,content,result)
values
    ('Q004', '003', N'dap an sai', 'F')
insert into Options
    (qid,onumber,content,result)
values
    ('Q101', '001', N'đông, hạ', 'T')
insert into Options
    (qid,onumber,content,result)
values
    ('Q101', '002', N'dap an sai', 'F')
insert into Options
    (qid,onumber,content,result)
values
    ('Q101', '003', N'dap an sai', 'F')
insert into Options
    (qid,onumber,content,result)
values
    ('Q102', '001', N'nắng mưa.', 'T')
insert into Options
    (qid,onumber,content,result)
values
    ('Q102', '002', N'dap an sai', 'F')
insert into Options
    (qid,onumber,content,result)
values
    ('Q102', '003', N'dap an sai', 'F')
insert into Options
    (qid,onumber,content,result)
values
    ('Q103', '001', N'Thời tiết', 'T')
insert into Options
    (qid,onumber,content,result)
values
    ('Q104', '003', N'nhiệt độ', 'T')
insert into Options
    (qid,onumber,content,result)
values
    ('Q201', '002', N'2 lần', 'T')
insert into Options
    (qid,onumber,content,result)
values
    ('Q202', '002', N'bỏ đi 8 mm', 'T')
insert into Options
    (qid,onumber,content,result)
values
    ('Q203', '002', N'ACBDEFGH2', 'F')
insert into Options
    (qid,onumber,content,result)
values
    ('Q204', '002', N'9.8', 'T')
insert into Options
    (qid,onumber,content,result)
values
    ('Q201', '001', N'ABCDEFGH', 'F')