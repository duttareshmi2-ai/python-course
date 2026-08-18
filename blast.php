<?php
$dsn = "mysql:host=localhost;dbname=blastdb;charset=utf8mb4";
$user = "root";
$pass = "";

$pdo = new PDO($dsn, $user, $pass);
$stmt = $pdo->query("SELECT * FROM blasts ORDER BY timestamp DESC");
echo "<h1 style='color:red;font-family:DS-Digital'>Blast History</h1>";
echo "<table border='1' style='color:white;background:black'>";
echo "<tr><th>ID</th><th>Timestamp</th></tr>";
foreach ($stmt as $row) {
    echo "<tr><td>{$row['id']}</td><td>{$row['timestamp']}</td></tr>";
}
echo "</table>";
?>