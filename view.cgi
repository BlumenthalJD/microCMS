#!/usr/bin/perl

# view.cgi

use CGI qw(:standard);

#file setup
$user=param('user');
open (data, "data/$user/user.dat");
chomp(@info=<data>);
close (data);
@colors=split(/ /, @info[2]);

#start page
print header;
print "<html><head><title>@info[0] @info[1]\'s Homepage</title>";

#declares styles
print "<style> body{background-color: @colors[0]; color: @colors[1]; text-align: center; align-content: center;} a:link{color: @colors[2];} a:visited{color: @colors[3];}</style>";
print "</head><body>";

#starts body
print "<a href='index.cgi'><h3 style='text-align: center;'>Home</h3></a><h1>@info[0] @info[1]\'s Homepage</h1>";

#outputs favorite sites
print "<h2>Favorite Sites</h2>";
$numLink=@info[3];
$startNum=4;
foreach(1..$numLink)
{
	print "<a href='http://@info[$startNum]'>@info[$startNum+1]</a><br>";
	$startNum+=2;
}

#outputs pics
print "<h2>Favorite Pictures</h2>";
$numPic=@info[$startNum];
$startNum++;
foreach (1..$numPic)
{
	print "<img src='data/$user/@info[$startNum]' height='300' width='400'><br>";
	$startNum++;
}
print "Contact me at: <a href='mailto:@info[$startNum]?Subject=Directed From Your Website' target='_top'>@info[$startNum]</a>";
print "</body></html>";