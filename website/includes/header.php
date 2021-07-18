<?php
     
     require __DIR__.'/vendor/autoload.php';

     use Kreait\Firebase\Factory;
     use Kreait\Firebase\ServiceAccount;

     $serviceAccount = ServiceAccount::fromJsonFile(__DIR__ . '/securities_6969.json');
     $firebase = (new Factory)
        ->withServiceAccount($serviceAccount)
        ->withDataBaseUri('https://home-security-87542-default-rtdb.asia-southeast1.firebasedatabase.app')
        ->create();
    
    $database = $firebase->getDatabase();
    
    


?>
