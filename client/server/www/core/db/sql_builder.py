class Sql_builder(object):
    '''build sql'''
    sql=''
    options={}
    
    def select(self,fields):
        self.sql.join(['select ',fields,' '])
    
    def fm(self,table):
        self.sql.join(['from ',table,' '])
    
    
    def where(self,seg,*args):
        if isinstance(seg,str):
            value=args[0]
            option = 'where'
            if option not in self.options.keys():
                self.options['where']= [seg+'='+value]
                self.sql.join(['where ',self.options['where'].pop(),' '])
            else:
                self.options['where']= [seg+'='+value]
                self.sql.join(['where ',self.options['where'].pop(),' '])                

            
    
    

    