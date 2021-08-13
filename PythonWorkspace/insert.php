<?php
$conn = mysqli_connect("localhost","root","a135790","opentutorials")
//mysqli connect
//mysql이 설치되있는 컴퓨터에 연결 자신 컴퓨터면 127.0.0.1 or localhost
//1.address 2.id 3.password 4.databasename
$sql ="
    INSERT INTO topic
        (title, description, created)
        VALUE(
            'MySQL',
            'MySQL is..',
            NOW()
        )
)";
echo $sql;
mysqli_query($conn,$sql);


?>