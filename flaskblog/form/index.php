<html>
<head>
    <title>Contact us </title>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>
<body>
    <style>
        body{
            background-image: url(https://i.pinimg.com/originals/8a/68/3e/8a683eec3e6e81ca96e00a8077422996.png);
        }
    </style>
    <div class="container" style="background: #fed049;
  width: 900px;
  height: 650px;
  margin: 5% auto;
  position: relative;">
        	<h1 class="title" style="color: 1b1a17;">CONTACT US</h1>
		<h3 class="subtitle" style="color: white;">We Are Here Assist You.</h3>
        <hr class="rounded">  
        <form action="form-process.php" method="POST">
        <form action="run.py" method="post">
            <div class="form-group">
                <label for="firstname">Firstname</label>
                <input type="text" name="firstname" id="firstname" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="lastname">Lastname</label>
                <input type="text" name="lastname" id="lastname" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="phone">Phone</label>
                <input type="tel" name="phone" id="phone" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" name="email" id="email" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="message">Message</label>
                <input type="text" name="message" id="message" class="form-control" required>
            </div>
            <div class="form-group">
        <button class="btn btn-success" type="submit">Submit</button>
        <button class="btn btn-danger" type="reset">Reset</button>
    </div>
        </form>
    </div>
</body>

</html>