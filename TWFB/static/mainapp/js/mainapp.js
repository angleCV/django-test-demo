jQuery(function($){
    get_zblist();
});

var curlastid = parseInt('106');

function get_zblist(){
    var postdata = {
        lastid : curlastid
    }
    $.ajax({
        type			: 'get',
			// url				: './?a=zblist',
			dataType		: 'json',
			data			: postdata,
			success			: function(response){
				curlastid = parseInt(response.lastid);
				//console.dir(response);

				if(response.zblist.length > 0){
					(function(i){
						var callee = arguments.callee;
						if(i < response.zblist.length){
							var row = response.zblist[i];
							var li = [
								'		<li>',
								'			<dl class="clearfix">',
								'				<dt>'+row.realname+'</dt>',
								'				<dd>'+row.content+'</dd>',
								'			</dl>',
								'		</li>'
							].join('');
							$('#zblist').prepend(li);

							setTimeout(callee, 100);
						}

					})(0);
				}

				setTimeout(function(){
					trigger_refresh();
				}, 10000);
			}
		});
	}
