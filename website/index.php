<?php include('includes/header.php'); 
session_start();
?>

<div class="container">
    <div class="row">
    </div>

    <div class="col-md-12 mt-5">
        <div class="card">
            <div class="card-body">
                
                <div class="table-responsive">
                    <table class="table table-border">
                        <thead>
                            <tr>
                                <th>alert</th>
                                <th>date</th>
                                <th>person</th>
                                <th>time</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php
                                include('includes/dbconfig.php');
                                $ref= "";
                                $fetchdata= $database->getReference($ref)->getValue();

                                foreach($fetchdata as $key => $row)
                                {

                                
                            ?>
                            <tr>
                                <td><?php echo $row['alert']; ?></td>
                                <td><?php echo $row['date']; ?></td>
                                <td><?php echo $row['person']; ?></td>
                                <td><?php echo $row['time']; ?></td>
                            </tr>
                            <?php
                                }

                            ?>

                        </tbody>
                        
                            
                        

                    </table>
                </div>

    </div>
</div>

        

<?php 
include('includes/footer.php');
$sec=3;
$page = $_SERVER['PHP_SELF'];
?>
<html>
    <head>
    <meta http-equiv="refresh" content="<?php echo $sec?>;URL='<?php echo $page?>'">
    </head>
    <body>
    
    </body>
</html>