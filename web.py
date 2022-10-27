<!DOCTYPE html>
<html lang="zh-TW">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>王思婷簡介</title>

	<style type="text/css">
		* {
			font-family: "標楷體"; }

		header {
			font-size: 36px;
			color: #55ff55; }

		.col-lg-4 {
			border: 1px solid; }	
	</style>

	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">

	<script>
		$(document).ready(function(){
			$("#I").hover(function(){
				$("#PICTURE").attr("src","/static/images/bubble2.jpg");
			});

			$("#PU").hover(function(){
				$("#PICTURE").attr("src","/static/images/pu.jpg");
			});

			$("#CSIM").hover(function(){
				$("#PICTURE").attr("src","/static/images/csim.jpg");
			});

			$("#PICTURE").click(function(){
				$("#PICTURE").hide();
				$("#PICTURE").fadeIn("slow")
			});
		});
	</script>
	
</head>
<body>
	<nav class="navbar navbar-expand-md bg-secondary navbar-dark">
	<a class="navbar-brand" href="#">MENU</a>

	<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
		<span class="navbar-toggler-icon"></span>
	</button>

	<div class="collapse navbar-collapse" id="collapsibleNavbar">
		<ul class="navbar-nav">
			<li class="nav-item"><a class="nav-link" href="#aboutme">關於我</a></li>
			<li class="nav-item"><a class="nav-link" href="#bookmark">喜愛佳句</a></li>
			<li class="nav-item"><a class="nav-link" href="#youtube">推薦影片</a></li>
		</ul>
	</div>
<nav>

	<main class="container-fluid bg-info text-white text-center">

		<nav>
			<h1><a href="http://www1.pu.edu.te/~s1100381/1"
				 class="text-reset text-decoration-none text-white bg-warning" target="_blank" id="I"> 王思婷 (Ssu-Ting Wang)</h1> 
			<h2><a href="https://www.pu.edu.tw/"
				 class="text-reset text-decoration-none text-white bg-info" id="PU">靜宜大學</a> 
	 		 / <a href="https://csim.pu.edu.tw/"
	 		 	 class="text-reset text-decoration-none text-white bg-info" id="CSIM"資訊管理學系</a></h2> 
		</nav> 
		
	 	<img src="me.jpg" alt="照片" class="img-fluid rounded-circle">
	 	<br><br><br>

	 	<div class="row">
			<session id="aboutme" class="col-lg-4"> 
	 			<header>關於我</header>
	 			<h3>系級: 資訊管理學系二A</h3>
	 			<h3>學號: 411003811</h3>
	 			<h3>Tel: <a href="tel:0900237427"></a></h3>
	 			<h3>E-Mail: <a href="mailto:s1100381@gm.pu.edu.tw">s1100381@gm.pu.edu.tw</a></h3>
			</session> 
	
	<article id="bookmark" class="col-lg-4">	
		<header>喜愛佳句</header>
	 	<h3>因為年輕我們一無所有，也正因為年輕我們將擁有一切<h3>
	 	<h3>預測未來的最好方法，就是創造未來<h3>
	 	<h3>自己選擇的路，跪著也要把它走完<h3>
	 	<h3>就算全世界都否定我，還有我自己相信我<h3>
	</article>
	
	<aside id="youtube" class="col-lg4"> 	
	 <header>推薦影片</header>
	 <div class="embed-responsive embed-responsive-16by9">
	 	<iframe src="https://www.youtube.com/watch?v=KSH-FVVtTf0" allowfullscreen
	 	 class="embed-responsive-item">></iframe>
	 	</div>
	</aside>
</div><br><br>	

	<footer>
	 Copyright © 王思婷. ALL Rights Reserved.
	 <footer>

	</main> 
		
</body>
</html>	 