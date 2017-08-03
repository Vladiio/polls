$(document).ready( function() {

    $('.vote').click( function() {
        var answer_id = $(this).attr('data-answer'),
              me = this;

        $.ajax({
            url: "vote",
            data: {
                answer_id: answer_id,
            },
            type: "GET",
            dataType: "json",
        })

        .done( function(json) {
            $("#vote_" + answer_id).html('Total ' + json.votes);
            $(".vote").fadeOut(1000);
        })

        .fail( function(xhr, status, errorThrown) {
            alert("There was a problem");
            console.log("Error: " + errorThrown);
            console.log("Status: " + status);
            console.dir( xhr );
        })

    });

});
