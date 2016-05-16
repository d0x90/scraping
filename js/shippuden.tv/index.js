var request = require('request'),
    cheerio = require('cheerio'),    
    fs = require('fs'),
    async = require('async')
    urls = Array();

var urls = [ 'http://www.shippuden.tv/online-sub-espanol-capitulos-hd']
var urls2 = []

async.eachSeries(urls, function (url, next) {
  request(url, function (e, r, b) {
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
                    if ( url_item.nombre.toString().indexOf("Fecha de Publicación") == -1) 
                    {
                        urls2.push(url_item);   
                    }
                    
                 }
                
            });        
                   
        });
    }
    next() 
  })
}, onFinished)

function onFinished (err) {
  async.eachSeries(urls2, function (url, next) {
  	console.log(url.nombre)
  request(url, function (e, r, b) {
  	if (e) next(e) // handle error
    if ( !e && r.statusCode == 200 )
    {            
        // if(err) return console.error(err);
         var $ = cheerio.load(b);   
         e = $('#st_content_1').find('iframe').attr('src');
         console.log(e)
    }
    next() 
  })
},nada())
}
nada = function ()
{
	console.log("Que miras hijo de tu puta madre")
}