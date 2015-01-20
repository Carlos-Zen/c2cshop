Phonegap+Django B2C shop
        Using ember.js with phonegap. This share to study for reference purposes only, does not guarantee the availability of the source code.

Intro
        This is the development of a B2C mall system, application and development of application on mobile terminal. A began to plan to use Android, IOS, native language development. But not hire the right person (wages can not afford), so think of phonegap, a development, multiple use. The hardships of the journey has begun.

However, finally completed, although the experience is not very good. (the project eventually not on-line, not encrypt data transmission, without strict test)

The scheme is, through the ember.js to render the front view, data interface not comes with ember.js, because this should be the standard of good data interface specification and data interface has been a mess of our own. Then using the HTTP interface to the server requests the way data.

The server data model using python, in response to the access data through HTTP interface, the transmission of JSON data format.

Usage
	There is one file named sql.sql under the mysql directory,import this file by phpmyadmin or other system could rec .sql file.

        /client
Phonegap project
        /client/www/common/common.js
Api config in line 2:

        ws_server_url="http://192.168.2.118/open.php/service/server/";
