$(document).ready(function() {
  $.ajax({
    url: "/fetchExam",
    type: "GET",
    dataType: "json",
    success: function(data) {
      data.listExam.forEach(element => {
        console.log(element);
        $("#myTable tr:last").after(
          "<tr><td>" +
            element[0] +
            "</td>" +
            "<td>" +
            element[2] +
            "</td>" +
            "<td><button class='btn btn-sm btn-primary'><a href='/examDetail?id=" +
            element[0] +
            "'>Detail</a></button></td>" +
            "<td><button class='btn btn-sm btn-warning'><a href='/examModify?id=" +
            element[0] +
            "'>Modify</a></button></td>" +
            "<td><button class='btn btn-sm btn-danger' onclick='deleteExam('" +
            element[0] +
            "')'>Delete</button></td>" +
            "</tr>"
        );
      });
    }
  });
  $("#menu1").click(function() {
    $.ajax({
      url: "/fetchExam",
      type: "GET",
      dataType: "json",
      success: function(data) {
        console.log(data);
      }
    });
  });
});
function deleteExam(id) {
  $.ajax({
    url: "/deleteExam?id=" + id,
    type: "GET",
    dataType: "json",
    success: function(data) {
      console.log(data);
    }
  });
}
