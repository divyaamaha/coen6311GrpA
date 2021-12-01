// JavaScript source code

$(document).ready(function () {
    load();
});

function load() {
    //alert("Working...");
    $("#txtNoOfRec").focus();

    $("#btnNoOfRec").click(function () {
        $("#AddControll").empty();
        var NoOfRec = $("#txtNoOfRec").val();

        //alert("" + NoOfRec);

        if (NoOfRec > 0) {
            createControll(NoOfRec);
        }
    });    
}

function createControll(NoOfRec) {
    var tbl = "";

    tbl = "<table class='table table-bordered table-hover'>"+
                "<tr>"+
                    "<th> S.No </th>"+
                    "<th> Medicine Name </th>"+
                    "<th> Quantity </th>"+
                    "<th> Price </th>"+
                   
                "</tr>";

    for (i = 1; i <= NoOfRec; i++) {
        tbl += "<tr>" +
                    "<td>" + i + "</td>" +

                    "<td>"+
                        "<input type='text' id='txtFName' placeholder='Medicine Name' autofocus />"+
                    "</td>"+

                    "<td>"+
                        "<input type='text' id='txtLName' placeholder='Quantity' />"+
                    "</td>"+

                    "<td>"+
                        "<input type='text' id='txtLName' placeholder='Price' />"+
                    "</td>"+

                    
                "</tr>";
    }
    tbl += "</table>";

    $("#AddControll").append(tbl);
}