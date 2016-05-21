//dependencias
var request = require('sync-request'),
	cheerio = require('cheerio'),
	fs = require('fs');
	
	// parametros 
	var metodo = "GET",
	url  ="http://autos.mercadolibre.com.pe/#D[H:true]",
	cantidadPaginas = 1;

	// método para extraer las páginas
	function crawler_ml_pe_sub(uri)
	{
		/*var req = request("GET",uri);
		if (req.statusCode >= 300) {
		    var err = new Error('Server responded with status code ' + req.statusCode + ':\n' + req.body.toString(encoding));
		    err.statusCode = req.statusCode;
		    err.headers = req.headers;
		    err.body = req.body;
		    throw err;
		  }
		  console.log(req.body.toString("UTF-8")) 

		//body = req.getBody();
		//var $ = cheerio.load(body);
		//$('#thumbsList > li.ch-thumbnail-on').each(function()
		//{	
			//console.log('hey')
			//var href = $(this).find("img");
			//console.log("hey."+href)
		//});
		*/

	}
	function crawler_ml_pe(metodo,url,cantidadPaginas)
	{
		var req = request(metodo,url);
		body = req.getBody()		
		var $ = cheerio.load(body);
		$('li.article','ol#searchResults').each(function()
		{	
		    	var titulo = $(this).find("a","list-view-item-title").text();
		    	var precio = $(this).find("span","costs").text();
		    	var destaque = $(this).find("strong","destaque").text();
		    	var imgUrl = $(this).find("li","ch-carousel-item").find("img").attr("src");
		    	crawler_ml_pe_sub(imgUrl)
		    	console.log(titulo + " - " + precio + " - " + destaque + " - "+ imgUrl)
		});
		//obtener el link de la siguiente página
		link= $('a:contains("Siguiente >")').attr("href");

		console.log('Página siguiente ..... ' + link)
		if ( cantidadPaginas == 1 ) return;
		crawler_ml_pe(metodo,link,cantidadPaginas-1)
	}

	crawler_ml_pe("GET",url,1);


	
