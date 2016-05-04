var request = require('request'),
    cheerio = require('cheerio'),    
    fs = require('fs'),
    urls = Array();
   
require('events').EventEmitter.prototype._maxListeners = 0;

var waiting = 1;

request('http://www.shippuden.tv/online-sub-espanol-capitulos-hd', function ( err, resp, body ) 
{
    if ( !err && resp.statusCode == 200 )
    {
        var $ = cheerio.load(body);
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
                    if ( url_item.nombre.toString().indexOf("Fecha de Publicación") == -1) 
                    {
                        urls.push(url_item);   
                    }
                    
                 }
                
            });        
                   
        });
    }
     if(--waiting == 0) callback();
        
});
/*
function callback()
{
for ( var count = 0 ; count < urls.length ; count ++)
{
    
    request(urls[count].url, function ( err, resp, body) 
    {

        
    //var uri_uri = urls[count].url.toString();
    //var nombre_uri = urls[count].nombre.toString();
    if ( !err && resp.statusCode == 200 )
        {            
            // if(err) return console.error(err);
             var $ = cheerio.load(body);   
             e = $('#st_content_1').find('iframe').attr('src');
             console.log(e)
        }

    });

}
}*/