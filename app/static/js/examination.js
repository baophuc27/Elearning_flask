$(document).ready(function() {
  var close = document.getElementsByClassName("closebtn");
  close[0].onclick = function() {
    $("#alert-box").hide();
  };
  close[1].onclick = function() {
    $("#warning-box").hide();
  };
  close[2].onclick = function() {
    $("#danger-box").hide();
  };
  fetchExam();
});
function deleteExam(id) {
  $.ajax({
    url: "/examDelete?id=" + id,
    type: "GET",
    dataType: "json",
    success: function(data) {
      console.log(data);
      $("#warning-box").show();
      $("#alert-warning").text(data.action);
      fetchExam();
    }
  });
}
function fetchExam() {
  courseID = $("#course-name").text();
  $("#myTable > tbody").empty();
  $.ajax({
    url: "/fetchExam?courseID=" + courseID,
    type: "GET",
    dataType: "json",
    success: function(data) {
      data.listExam.forEach(element => {
        console.log(element);
        $("#myTable > tbody").append(
          "<tr><td>" +
            element[0] +
            "</td>" +
            "<td>" +
            element[2] +
            "</td>" +
            "<td><button class='btn btn-sm btn-primary'><a href='/examDetail?id=" +
            element[0] +
            "'>Detail</a></button>" +
            `<td><button class='btn btn-sm btn-danger' onclick='deleteExam("` +
            element[0] +
            `")'>Delete</button></td>` +
            "</tr>"
        );
      });
    }
  });
}

function createExam(name) {
  if ($("#mabaithi").val().length > 5 && $("#mabaithi").val().length <= 0) {
    $("#warning-box").show();
    $("#alert-warning").text("phải có từ 1 - 5 kí tự");
    return false;
  }
  $.post(
    "/insertExam",
    {
      courseID: name,
      examID: $("#mabaithi").val()
    },
    function(data, status) {
      $("#alert-box").show();
      $("#alert-info").text(data.message);
      fetchExam();
    }
  );
  return false;
}
