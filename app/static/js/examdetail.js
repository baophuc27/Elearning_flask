$(document).ready(function() {
  fetchQuestion();
});
function deleteExam(id) {
  $.ajax({
    url: "/examDelete?id=" + id,
    type: "GET",
    dataType: "json",
    success: function(data) {
      console.log(data);
      alert(data.action);
      fetchQuestion();
    }
  });
}
function fetchQuestion() {
  examID = $("#exam-name").text();
  $("#myTable > tbody").empty();
  $.ajax({
    url: "/fetchQuestion?examID=" + examID,
    type: "GET",
    dataType: "json",
    success: function(data) {
      data.listExam.forEach(element => {
        if (element[2] == null) element[2] = "Chưa có đáp án";
        $("#myTable > tbody").append(
          "<tr><td>" +
            element[0] +
            "</td>" +
            "<td>" +
            element[1] +
            "</td>" +
            "<td>" +
            element[2] +
            "</td>" +
            "<td>" +
            element[3] +
            "</td>" +
            `<td><button class='btn btn-sm btn-primary' onclick='modifyQuestion("` +
            element[0] +
            `","` +
            element[1] +
            `",` +
            element[3] +
            `)'>Detail</button>` +
            `<td><button class='btn btn-sm btn-danger' onclick='deleteQuestion("` +
            element[0] +
            `")'>Delete</button>` +
            "</td></tr>"
        );
      });
    }
  });
}

function createQuestion(name) {
  if ($("#macauhoi").val().length > 8) {
    alert("không được quá 8 kí tự");
    return false;
  }
  if ($("#macauhoi").val().length <= 0) {
    alert("không được để trống mã câu hỏi");
    return false;
  }
  if ($("#noidung").val().length <= 0) {
    alert("không được để trống nội dung");
    return false;
  }
  if (parseInt($("#diem").val()) < 0) {
    alert("không được để điểm âm");
    return false;
  }
  $.post(
    "/insertQuestion",
    {
      examID: name,
      qid: $("#macauhoi").val(),
      mark: $("#diem").val(),
      content: $("#noidung").val()
    },
    function(data, status) {
      alert("Status: " + data.message);
      fetchQuestion();
    }
  );
  return false;
}
function modifyQuestion(id, c, m) {
  document.getElementById("myForm").style.display = "block";
  $(".main").css("opacity", "0.15");
  $("#qid").text(id);
  $("#Content").val(c);
  $("#mark").val(m);
  return false;
}
function confirmModify() {
  if ($("#Content").val().length <= 0) {
    alert("không được để trống nội dung");
    return false;
  }
  if (parseInt($("#mark").val()) < 0) {
    alert("không được để điểm âm");
    return false;
  }
  $.post(
    "/modifyQuestion",
    {
      qid: $("#qid").text(),
      mark: $("#mark").val(),
      content: $("#Content").val()
    },
    function(data, status) {
      alert("Status: " + data.message);
      document.getElementById("myForm").style.display = "none";
      $(".main").css("opacity", "1");
      fetchQuestion();
    }
  );
  return false;
}
function closeForm() {
  document.getElementById("myForm").style.display = "none";
  $(".main").css("opacity", "1");
}

function deleteQuestion(id) {
  $.ajax({
    url: "/questionDelete?id=" + id,
    type: "GET",
    dataType: "json",
    success: function(data) {
      console.log(data);
      alert(data.action);
      fetchQuestion();
    }
  });
}
