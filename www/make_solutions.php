<?php

include('conn.php');

// php by default limits exec execution time
ini_set('max_execution_time', 300000);

$rs = mysql_query("SELECT * FROM Puzzle WHERE id>19");
while ($row = mysql_fetch_assoc($rs)) {
    echo "<br>";
    $id = $row['id'];
    $puzzle = json_decode($row['data']);
    $height = count($puzzle);
    $width = count($puzzle[0]);
    echo $row['name'];

    $cachefilename = "$id.json";
    $cachepath = "/home/thomas/gp13-jaa/final/puzzles/$cachefilename";

    file_put_contents($cachepath, $row['data']);

    $result = exec("cd /home/thomas/gp13-jaa/final/; /usr/bin/python solver.py $width $height $cachefilename");

    $solution = file_get_contents($cachepath, $row['data']);

    mysql_query("UPDATE Puzzle SET solution='$solution' WHERE id=$id");

    echo "SUCCESS!";

};

exit;


// hash the puzzle data so we have a unique hash that we can use to store 
// temporary files
$md5 = md5($data);

// build path for generator and for where we store stuff
$cachefilename = $width."x".$height."x".$difficulty."-".$md5.".json";
$cachepath = "/home/thomas/gp13-jaa/final/puzzles/$cachefilename";

// this does mean we can cache results to save time and cpu usage if identical puzzles are 
// required to be generated
//
if(!file_exists("cache/puzzles/".$cachefilename)) {
    // however if we can't find anything in cache, we need to generate a new 
    // puzzle. we first put the data in a file on the system

    file_put_contents($cachepath, $data);

    // then we run the python generator using data from POST as input and the 
    // filename
    $result = exec("cd /home/thomas/gp13-jaa/final/; /usr/bin/python generator.py $width $height $cachefilename $difficulty");

    // copy the result into our cache
    copy("/home/thomas/gp13-jaa/final/puzzles/".$cachefilename, "cache/puzzles/".$cachefilename);

    // do the same thing but for generate a solution
    $result = exec("cd /home/thomas/gp13-jaa/final/; /usr/bin/python solver.py $width $height $cachefilename $difficulty");

    // and copy the solution into our cache
    copy("/home/thomas/gp13-jaa/final/puzzles/".$cachefilename, "cache/solutions/".$cachefilename);

}

// get the data to be sent to the user
$puzzledata = file_get_contents("cache/puzzles/".$cachefilename);
$solutiondata = file_get_contents("cache/solutions/".$cachefilename);

// build an array to be sent back to the client
$result = Array(
    "cachefilename" => $cachefilename,
    "puzzledata" => $puzzledata,
    "solutiondata" => $solutiondata
);

// json encode and print
echo json_encode($result);
