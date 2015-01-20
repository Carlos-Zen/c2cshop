//ws_server_url="http://192.168.2.100:8000/api";
ws_server_url="http://192.168.2.118/open.php/service/server/";
function get_ws_data(ws_method,ws_params){
	try{
	if(typeof(ws_method)!='string')
		throw new Error(2,'first param dataType get error');
	if(typeof(ws_params)!='object')
		throw new Error(2,'second param dataType get error');
	}
	catch(e){
		console.log(e);
		}
	ws_request_data={authkey:'',method:ws_method,params:JSON.stringify(ws_params)};
//	for(i in ws_params){
//			ws_request_data[i]=ws_params[i];
//		}	
	
	var str=escape((ws_method+JSON.stringify(ws_params)));
	var outdata = localStorage.getItem(str);
	if(outdata!=null){
	return outdata.data=JSON.parse(outdata)	
	
	}else{
	
	var outdata;
	 $.ajax({  
        type : "get",
		async:false,
		dataType:"json",
        url : ws_server_url,
		data:ws_request_data,  
        success : function(data){
		 outdata = data; 
		},  
        error:function(e){  
				alert('ajax error');
        }  
    });
	
		localStorage.setItem(str,JSON.stringify(outdata.data));
		return outdata.data;
}}



	/*清除本地存储*/
	var xiantime = new Date().getTime();
		localStorage.setItem("xiantime",xiantime)
	function _time(){
		var  xiantime=localStorage.getItem("xiantime")
		var cleartime=parseInt(xiantime)+10800000		;  //三个小时候后
		var nowstime =new Date().getTime();
		if((nowstime-cleartime)>0){
			var inf=localStorage.getItem('userinfo')
			var lo=localStorage.getItem('login')
			//localStorage.removeItem("activity");//清除activity的值
			//localStorage.setItem("xiantime",'')
			localStorage.clear();
			localStorage.setItem("userinfo",inf);
			localStorage.setItem("login",lo);
		
		}
	}
	
	_time()
	setInterval(_time,10980000);   //三小时三分钟执行一次