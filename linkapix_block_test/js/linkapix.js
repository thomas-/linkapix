var picking = false;
var number = 0;

function destroy_puzzle() {
    $(".linkapix").html("");
}

function json_to_puzzle(json_url) {
    console.log('build!' + json_url);
    $.getJSON(json_url, function(data) {
        console.log(data);
        $.each(data, function(key, val) {
            console.log(val);
            $.each(val, function(key, block) {
                console.log(key);
                console.log(block.number);
            });
        });
    });
    var str = '[[{"number":3,"color":{"r":0,"g":0,"b":0}},null,{"number":3,"color":{"r":0,"g":0,"b":0}},null,null],[null,null,null,{"number":1,"color":{"r":0,"g":0,"b":0}},null],[null,null,{"number":5,"color":{"r":0,"g":0,"b":0}},{"number":2,"color":{"r":0,"g":0,"b":0}},null],[null,null,null,{"number":2,"color":{"r":0,"g":0,"b":0}},null],[{"number":5,"color":{"r":0,"g":0,"b":0}},null,null,null,null]] ';
    return JSON.parse(str);
};


function build_puzzle(puzzle) {
    var table = $("<table></table>");
    $(".linkapix").append(table);
    $(".linkapix").append();
    $.each(puzzle, function(rid, row) {
        var tr = $("<tr/>")
        var blocks = [];
        $.each(row, function(cid, block) {
            number = block !== null ? block.number : "";
            blocks.push("<td>" + number + "</td>");
        });
        tr.append(blocks);
        table.append(tr)
    });
    register_game_events();

};

$("#launch_test").click(function() {
    destroy_puzzle();
    puzzle = json_to_puzzle('puzzles/5x5test.json');
    build_puzzle(puzzle);
});


function register_game_events() {
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
};