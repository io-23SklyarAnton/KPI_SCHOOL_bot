# KPI_SCHOOL_bot

## Bot issues
- ### mysql-connector-python lib isn't async
this bot isn't complete asynchronous, because I didn't find async MySQL lib :D
- ### you can't write descriptions separated by spaces
because it will break the order of arguments
- ### you need a user id to send file
constantly searching for user ID can be a bit annoying

<i>**I promise to fix this soon :)**</i>

<i>if you find any more problems, please, feedback <a href=https://t.me/Antntipo>me<a/></i>

## Bot description

### This bot can take documents,photos,videos,etc

It gives you a commands to take back your files or to send it to the other guy.
You can give a description to your file,just write a caption for it (without spaces)

<b>Main Instructions</b>

<i>/get_last_files <u>&lt;amount&gt;</u></i> - this command returns recent files,
where &lt;amount&gt; is the number of recent files (default value is 1)

<i>/send_file <u>&lt; description &gt; &lt;addressee id&gt;</u> </i> - this command can send files to others.It has
required argument <u>&lt; description &gt;</u> to identify the file you want to send and <u>&lt; addressee_id &gt;
</u>to identify an addressee (default value is your id)