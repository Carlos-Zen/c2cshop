from core.database.db  import *

class Db_mysql(object):
    '''build sql'''
    sql=''
    options={}
    
    def select(self,fields):
        select_list = fields.split(',')
        self.options['select']=select_list
        return self
    
    def fm(self,table):
        
        self.options['from'] = table
        return self
    
    def where(self,seg,*args):
        '''
        sql query of where tag
        '''
        try:
           self.options['where']
        except:
            where_list=[]
        if isinstance(seg,str):
            try:
                where_list.append({'key':seg,'val':args[0],'type':args[1]})
            except:
                where_list.append({'key':seg,'val':args[0],'type':False})
        elif isinstance(seg,dict):
            for key in dict.keys():
                where_list.append({'key':key,'val':dict[key]})

        self.options['where']= where_list
        return self
    def where_in(self,key,val):
        if not isinstance(self.options['where'],list):
            self.options['where']=[]
        self.options['where'].append({'key':key,'val':str(val),'type':'in'})

            
        return self
    def join(self,table,on,type='left'):
        self.options['join']= {'table':table,'on':on,'type':type}
        return self
    
    def limit(self,offset=0,size=0):
        offset = int(offset)
        size = int(size)
        if size == 0:
            size=offset
            offset=0
        self.options['limit']= {'offset':str(offset),'size':str(size)}
        return self
    def order(self,oby,desc='desc'):
        self.options['order']={'order':str(oby),'desc':str(desc)}
        return self
    def combile_sql(self):
        '''
        combile select sql
        '''
        if not isinstance(self.options['select'],list):
            self.options['select']=['*']
            
        self.sql=''.join(['select '])
        length = len(self.options['select'])
        for i in range(length):
            fields = self.options['select'][i]
            if i==length-1:
                self.sql=''.join([self.sql,fields,' '])
                break
            self.sql=''.join([self.sql,fields,', '])
        '''
        combile from sql
        '''        
        self.sql=''.join([self.sql,' from ',self.options['from'],' '])
        '''
        combile join sql
        '''  
        try:
            if isinstance(self.options['join'],dict):
                join_str = self.options['join']
        except:
            pass
        else:
            self.sql=''.join([self.sql,join_str['type'],' join ',join_str['table'],' on ',join_str['on'],' '])
        '''
        combile where sql and where in sql
        '''        
        
        try:
            where_list = self.options['where']
        except:
            where_list = []
        else:
            self.sql=''.join([self.sql,' where '])
            count=0
            for item in where_list:
                if count is 0:
                    segment = ' '
                else:
                    segment = ' AND '
                count=count+1
                if not item['type']:
                    self.sql=''.join([self.sql,segment,item['key'],'=',str(item['val'])])
                elif item['type'] is 'in':
                    self.sql=''.join([self.sql,segment,item['key'],' in (',str(item['val']),') '])
        
        '''
        combile order sql
        '''
        try:
            order_dict = self.options['order']
            if isinstance(order_dict,dict):
                self.sql=''.join([self.sql,' order by ',order_dict['order'],' ',order_dict['desc']])   
        except:
            pass
                     
        '''
        combile limit sql
        '''
        try:
            self.sql=''.join([self.sql,' limit ',self.options['limit']['offset'],',',self.options['limit']['size']])
            self.options = {}
        except KeyError:
            pass
        
        return self

   
    def get(self,table=False):
        if not isinstance(table,bool):
            self.options['from']
        self.combile_sql()
        try:
            rs = fetchone(self.sql)
        except:
            print self.sql
        return rs
    
    def all(self,table=False):
        if not isinstance(table,bool):
            self.options['from']
        self.combile_sql()
        try:
            rs = fetchall(self.sql)
        except:
            print self.sql
        return rs

DB = Db_mysql()
DB.select('attr_id,attr_name').fm('hr_attribute').where('attr_type',0).where_in('attr_id','3,4,6').join('goods as g','g.id=a.id','left').order('attr_id').limit(3,5);
DB.get()
