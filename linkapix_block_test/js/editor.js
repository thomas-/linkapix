var Color = function(r, g, b) {
  this.r = r;
  this.g = g;
  this.b = b;
};
var Block = function(number, color) {
  this.number = typeof number !== 'undefined' ? number : 0;
  this.color = typeof color !== 'undefined' ? color : new Color(0, 0, 0);
};

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
            number = block !== null || undefined ? block.number : "";
            blocks.push("<td>" + number + "</td>");
        });
        tr.append(blocks);
        table.append(tr)
    });
    register_editor_events();

};

function load_empty_puzzle(rows, cols) {
    puzzle = new Array(cols);
    for (i=0; i<cols; i++) {
        puzzle[i] = new Array(rows);
        for (j=0; j<cols; j++) {
            puzzle[i][j] = null;
        }
    }
    console.log(puzzle);
    return puzzle;
}

$("#launch_editor").click(function() {
    destroy_puzzle();
    var rows = $("#puzzle_rows").val();
    var cols = $("#puzzle_cols").val();
    puzzle = load_empty_puzzle(rows, cols);
    build_puzzle(puzzle);
});

function generate_puzzle_json() {
    puzzle = new Array()
    $("tr").each(function(row) {
        puzzle[row] = new Array();
        $(this).find("td").each(function(col) {
            console.log($(this).html());
            puzzle[row][col] = new Block($(this).html());
        });
    });
    return JSON.stringify(puzzle);
    return "json";
};


function register_editor_events() {
    $("td").attr('contenteditable', 'true');
    $("td").on('click', function() {
        document.execCommand('selectAll', false, null);
    });

    $("#generate_json").click(function() {
        json_string = generate_puzzle_json();
        $(".puzzledata").html(json_string);
    });

};