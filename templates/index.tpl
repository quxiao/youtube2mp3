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
        <form action="/transform" method="post" class="form-horizontal" role="form">
            <div class="form-group">
                <label class="col-sm-2 control-label">Youtbe URL</label>
                <div class="col-sm-10">
                    <input type="text" class="form-control" name="url">
                </div>
            </div>
            <div class="form-group">
                <div class="col-sm-offset-2 col-sm-10">
                    <input type="submit" class="btn btn-primary" value="Convert">
                </div>
            </div>
        </form>
        </div>
    </body>

</html>
