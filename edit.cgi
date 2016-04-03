#!/usr/bin/perl

# index.cgi

use CGI qw(:standard);

#file setup
$user=param('user');
open (data, "data/$user/user.dat");
chomp(@info=<data>);
close (data);
@colors=split(/ /, @info[2]);

#gets password info
$pwd="dg";
$password = @info[@info-1];
$word=param('password');

#checks password
if (crypt($word, $pwd) ne $password)
{
	#start page
	print header;
	print "<html><head><title>Editing @info[0] @info[1]</title>";
	
	#declares styles
	print "<style> body{text-align: center;} </style>";
	print "</head><body>";
	print "<h1>Editing @info[0] @info[1]</h1>";
	print "<form action='edit.cgi' method='get'>";
	print "<input id='user' name='user' type='hidden' value='$user'>";
	print "<label>Password: </label><input id='password' type='password' name='password'><br><br><input id='submit' type='submit' name='submit'><br>";
	print "</form>";
	print "</body></html>";
}

#prints edit options if password is correct	
else
{	
	#start page
	print header;
	print "<html><head><title>Editing @info[0] @info[1]</title>
	<style type='text/css' media='screen'>
			input[type='text']
			{
				height: 26px;
			}
			input[type='file']
			{
				height: 25px;
			}
			form label
			{
				font-size: 22px;
			}
			select
			{
				-webkit-appearance: menulist-button;
				height: 27px;
			}
		</style>
		<script>
			function updateLinkNum(select) 
			{
				var selectedLinkNum=select.value;
				for (var i=1; i<=selectedLinkNum; i++)
				{
					document.getElementById('fweb'+i+'label').style.visibility='visible';
					document.getElementById('fweb'+i+'desclabel').style.visibility='visible';
					document.getElementById('fweb'+i).style.visibility='visible';
					document.getElementById('fweb'+i+'desc').style.visibility='visible';
				}
				for (var j=i; j<4; j++)
				{
					document.getElementById('fweb'+j+'label').style.visibility='hidden';
					document.getElementById('fweb'+j+'desclabel').style.visibility='hidden';
					document.getElementById('fweb'+j).style.visibility='hidden';
					document.getElementById('fweb'+j+'desc').style.visibility='hidden';
				}
			}
			
			function updatePicNum(select) 
			{
				var selectedPicNum=select.value;
				for (var i=1; i<=selectedPicNum; i++)
				{
					document.getElementById('pic'+i).style.visibility='visible';
					document.getElementById('pic'+i+'label').style.visibility='visible';
				}
				for (var j=i; j<4; j++)
				{
					document.getElementById('pic'+j).style.visibility='hidden';
					document.getElementById('pic'+j+'label').style.visibility='hidden';
				}	
			}
		</script>
	</head>
	<body>
		<h1 style='text-align: center;'>Editing @info[0] @info[1]</h1>
			<form action='savepage.cgi' method='post' enctype='multipart/form-data'>
				<div style='width: 49.5%; float: left; text-align: right;'>
					<label for='fname'>First Name</label><br>
					<label for='lname'>Last Name</label><br>
					<label for='bcolor'>Background Color</label><br>
					<label for='tcolor'>Text Color</label><br>
					<label for='lcolor'>Link Color</label><br>
					<label for='vlcolor'>Visited Link Color</label><br>
					<label>Number of Favorite Websites</label><br>
					<label id='fweb1label' for='fweb1'>Favorite Website 1</label><br>
					<label id='fweb1desclabel' for='fweb1desc'>Favorite Website 1 Description</label><br>
					<label id='fweb2label' for='fweb2'>Favorite Website 2</label><br>
					<label id='fweb2desclabel' for='fweb2desc'>Favorite Website 2 Description</label><br>
					<label id='fweb3label' for='fweb3'>Favorite Website 3</label><br>
					<label id='fweb3desclabel' for='fweb3desc'>Favorite Website 3 Description</label><br>
					<label>Number of Favorite Pictures</label><br>
					<label id='pic1label' for='pic1'>Picture 1</label><br>
					<label id='pic2label' for='pic2'>Picture 2</label><br>
					<label id='pic3label' for='pic3'>Picture 3</label><br>
					<label for='email'>Email Address</label><br>
					<label for='password'>Password</label><br>
				</div>
				<div style='width: 49.5%; margin-left: 10px; float:left;'>
					<input id='fname' type='text' name='fname' value='@info[0]'><br>		
					<input id='lname' type='text' name='lname' value='@info[1]'><br>
					<input id='bcolor' type='text' name='bcolor' value='@colors[0]'><br>					
					<input id='tcolor' type='text' name='tcolor' value='@colors[1]'><br>					
					<input id='lcolor' type='text' name='lcolor' value='@colors[2]'><br>
					<input id='vlcolor' type='text' name='vlcolor' value='@colors[3]'><br>
					<select name='numLinks' id='numLinks' onchange='updateLinkNum(this)'>
						<option value='1'>1</option>
						<option value='2'>2</option>
						<option value='3' selected='selected'>3</option>
					</select><br>";
					
					#decides how many links should come out
					$numLink=@info[3];
					$startNum=4;
					for($i=1; $i<=$numLink; $i++)
					{
						print "<input id='fweb$i' type='text' name='fweb$i' value='@info[$startNum]'><br>";
						print "<input id='fweb$i\desc' type='text' name='fweb$i\desc' value='@info[$startNum+1]'><br>";
						$startNum+=2;
					}
					for ($j=$i; $j<4; $j++)
					{
						print "<input id='fweb$j' type='text' name='fweb$j'><br>";
						print "<input id='fweb$j\desc' type='text' name='fweb$j\desc'><br>";
					}
					
					#continues printing
					print "
					<select name='numPics' id='numPics' onchange='updatePicNum(this)'>
						<option value='1'>1</option>
						<option value='2'>2</option>
						<option value='3' selected='selected'>3</option>
					</select><br>";
					
					#decides how many pics should come out
					$numPic=@info[$startNum];
					
					$startNum++;
					for($i=1; $i<=$numPic; $i++)
					{
						print "<input id='pic$i' type='file' name='pic$i' value='data/$user/@info[$startNum]' placeholder='data/$user/@info[$startNum]'><br>";
						$startNum++;
					}
					for ($j=$i; $j<4; $j++)
					{
						print "<input id='pic$j' type='file' name='pic$j'><br>";
					}
					
					#prints remainder
					print"
					<input id='email' type='text' name='email' value='@info[$startNum]'><br>	
					<input id='password' type='password' name='password' value='$word'><br><br>
					<input id='submit' type='submit' name='submit'><br>	
				</div>
			</form>
	</body>
</html>";
}