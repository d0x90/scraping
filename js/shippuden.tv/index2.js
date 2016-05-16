var request = require('request'),
    cheerio = require('cheerio'),    
    fs = require('fs'),
    async = require('async'),
    mysql = require('mysql'),
    urls = Array();

var uri = 'http://www.shippuden.tv/online-sub-espanol-capitulos-hd'
urls2 = [],
connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : '',
  database : 'shippudentvdb'
});
connection.connect();
connection.query('CREATE TABLE IF NOT EXISTS `zeldas`(`id` INT AUTO_INCREMENT PRIMARY KEY, `nombre` VARCHAR(200), `zelda` VARCHAR(200) );', function(err, rows, fields) {
  if (err) throw err;
});
async.auto({
    one: function(callback){
    request(uri, function (e, r, b) {
      if (e) next(e) // handle error
      if ( !e && r.statusCode == 200 )
        {
            var $ = cheerio.load(b);
            $('ul','.page-post').each(function()
            {            
                $('li').each(function(i, elem) {
                    var url_item = Array();
                     var url_itemUrl = $(this).children().attr('href');                 
                     
                     if (url_itemUrl && url_itemUrl.indexOf('sub-espanol.html') != -1 ) 
                     {
                        url_item.url = url_itemUrl;
                        url_item.nombre = $(this).text();
                        url_item.descargar = "";
                        if ( url_item.nombre.toString().indexOf("Fecha de publicación") == -1 && url_item.nombre.toString().indexOf("Fecha de Publicación") == -1) 
                        {
                            urls2.push(url_item);   
                        }
                        
                     }
                    
                });        
                       
            });
        }
      callback(null, 1);      
    })
    }, 
    // If two does not depend on one, then you can remove the 'one' string
    //   from the array and they will run asynchronously (good for "parallel" IO tasks)
    two: ['one', function(callback, results){
      async.eachSeries(urls2, function (url, next) {
        request(url, function (e, r, b) {
            //if (e) next(e) // handle error
            if ( !e && r.statusCode == 200 )
            {            
                // if(err) return console.error(err);
                 var $ = cheerio.load(b);   
                 e = $('#st_content_1').find('iframe').attr('src');
                 if ( e != undefined )
                 {
                    //console.log(url.nombre + " .... " + e)
                    query = "INSERT INTO zeldas(nombre,zelda) VALUES('"+url.nombre+"','"+e+"');";
                      connection.query(query, function(err, rows, fields) {
                        if (err) throw err;
                      });
                      console.log(query)
                 }               
                 
            }              
          })
          next(null,2);
        })
    }],
    // Final depends on both 'one' and 'two' being completed and their results
    final: ['one', 'two',function(err, results) {
        console.log("Links migrados a la tabla zeldas de la base de datos shippudentvdb")
        connection.end();
    }]
});


