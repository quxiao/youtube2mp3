$def with (task_id, task_status, task_result) 

<html>
    <head>
        <link href="static/css/bootstrap.min.css" rel="stylesheet">
        <title>Youtube2MP3</title>
    </head>
    <body>
        <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="https://code.jquery.com/jquery.js"></script>
        <!-- Include all compiled plugins (below), or include individual files as needed -->
        <script src="static/js/bootstrap.min.js"></script>

        <div class="page-header">
            <h1 class="text-center">Youtube2MP3</h1>
        </div>
        <div class="container">
            <strong>Please refresh page to watch status</strong><br/><br/>
            TaskID: $task_id            <br/>
            TaskStatus: $task_status    <br/>
            URL: $task_result           <br/>
        </div>
</html>
