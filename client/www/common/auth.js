//auth¿‡∂®“Â
auth = function(){
    this.lstore = window.localStorage;
    is_login=false;
    if(this.check_login())
        is_login=true;
    else 
        is_login=false;
};
auth.prototype = {
    login:function(login_fields){
        var rs=get_ws_data('user_login',
        {
            a:login_fields
//    demo:     {
//                username:'duucoo',
//                password:'lianme',
//                from:'mobile'
//            }
        });
        console.log(rs);
		if(rs.user_id){
        this.set_user_login(rs);
		if(this.check_login())
			is_login=true;
		else 
			is_login=false;
		}
    },
    out_login:function (){
        this.lstore.setItem('login','');
        this.lstore.setItem('userinfo','');
    
    }
    ,
    set_user_login:function (user_info){
        var lstore=window.localStorage;
        this.lstore.setItem('login',1);
        this.lstore.setItem('userinfo',JSON.stringify(user_info));
    
    }
    ,
    get_userinfo:function (){
		var info=this.lstore.getItem('userinfo');	
		return JSON.parse(info);
    
    }
    ,
    check_login:function (){
        var log=this.lstore.getItem('login');
        if(log==1)
            return true;
        else 
            return false;
    }
    ,
    register:function(reg_fields) {
        
        var rs=get_ws_data('user_register',
        {
            a:reg_fields
//    demo:     {
//                user_name:'duucoo',
//                password:'lianme',
//                from:'mobile',
				
//            }
        });
        return rs;
    }
    
}

ath = new auth();