$(document).ready(function() {
  fetchExam();
});
function deleteExam(id) {
  $.ajax({
    url: "/examDelete?id=" + id,
    type: "GET",
    dataType: "json",
    success: function(data) {
      console.log(data);
      alert(data.action);
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
  if ($("#mabaithi").val().length > 5) {
    alert("phải có đúng 5 kí tự");
    return false;
  }
  $.post(
    "/insertExam",
    {
      courseID: name,
      examID: $("#mabaithi").val()
    },
    function(data, status) {
      alert("Status: " + data.message);
      fetchExam();
    }
  );
  return false;
}
