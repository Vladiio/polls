$(document).ready( function() {

    $('.vote').click( function() {
        var url = $(this).attr('data-url'),
            me = this;
        

        $.ajax({
            url: url,
            type: "POST",
            dataType: "json",
        })

        .done( function(json) {
            $("#vote_" + json.answer_id).html('Total ' + json.votes);
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
