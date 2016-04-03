#!/usr/bin/perl

# index.cgi

use CGI qw(:standard);

#start page
print header;
print "<html><head><title>User Saved</title></head>";
print "<body><a href='index.cgi'><h3 style='text-align: center;'>Home</h3></a><h1 style='text-align: center;'>User Successfully Saved</h1>";

#gets all parameters
$firstName=param('fname');
$lastName=param('lname');
$userName=lc substr($firstName, 0, 1).lc $lastName;
$backColor=param('bcolor');
$textColor=param('tcolor');
$linkColor=param('lcolor');
$vLinkColor=param('vlcolor');
$linkNum=param('numLinks');

#uploads links
foreach $i (1..$linkNum)
{
	@favoriteSite[$i]=param('fweb'.$i);
	@favoriteSiteDesc[$i]=param('fweb'.$i.'desc');
}

#uploads picture names
$picNum=param('numPics');
foreach $i (1..$picNum)
{
	@pic[$i]=param('pic'.$i);
	
}
$email=param('email');

#encrypts password
$pwd="dg";
$password=crypt(param('password'), $pwd);

#creates directory for user
mkdir "data/$userName";
system ("chmod 707 data/$userName");

#creates user.dat
open(dat, ">data/$userName/user.dat");
#outputs start of file
printf dat "$firstName\n$lastName\n$backColor $textColor $linkColor $vLinkColor\n$linkNum\n";

#outputs sites
foreach $i (1..$linkNum)
{
	printf dat "@favoriteSite[$i]\n@favoriteSiteDesc[$i]\n";
}

#outputs pictures and uploads
printf dat "$picNum\n";
foreach $i (1..$picNum)
{
	open UPLOADFILE, ">data/$userName/@pic[$i]";
	$uploadHandle=upload('pic'.$i); 
	while ( <$uploadHandle> ) 
	{ 
		print UPLOADFILE $_;
 	}
 	close UPLOADFILE; 
	printf dat "@pic[$i]\n";
	system ("chmod 707 data/$userName/@pic[$i]");
}

#outputs rest
printf dat "$email\n$password";
close (dat);
system ("chmod 707 data/$userName/user.dat");

#ends page
print "</body></html>";