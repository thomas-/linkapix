var picking = false;
var number = 0;

$("td").mousedown(function() {
    if ($(this).is(':empty')) {
        return;
    }
    else if ($(this).html() == '1') {
        $(this).css('background-color', '#222');
    }
    else {
        console.log($(this).html());
        number = $(this).html();
        picking = true;
        $(this).css('background-color', '#999').addClass('picking');
    }
});

$("td").mouseover(function() {
    if (picking) {
        $(this).css('background-color', '#999').addClass('picking');
    }
});

$("td").mouseup(function() {
    if (picking) {
        if ($(this).html() == number && $("td.picking").length == number) {
            $("td.picking").css('background-color', '#222').removeClass('picking');
            $(this).css('background-color', '#222');
        }
        $("td.picking").css('background-color', '#fff').removeClass('picking');
        picking = false;
    }
});