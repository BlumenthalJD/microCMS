#!/usr/bin/perl

# index.cgi

use CGI qw(:standard);


#start page
print header;
print "<html><head><title>BES Web Pages</title></head><body>";
print "<h1 style='text-align: center;'>Boger Elementary School Web Pages</h1>";
print "<div style='text-align: center;'>";
opendir(stuff, "data");

#open and read in users
while(defined($file=readdir(stuff)))
{
	if(!($file eq ".") && !($file eq ".."))
	{
		open (dir, "data/$file/user.dat");
		chomp(@list=<dir>);
		print "<h2>$list[0] $list[1]</h2>";
		print "<a href='view.cgi?user=$file'>View Page</a><br>";
		print "<a href='edit.cgi?user=$file'>Edit Page</a>";
	}
}
close(dir);
closedir(stuff);
print "</div>";

print "<div style='text-align: center;'>";
print "<a href='new.html'><h2>New User</h2></a>";
print "</div>";

print "</body></html>";