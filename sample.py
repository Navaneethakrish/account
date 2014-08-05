print 'naresh'
for i in range(8):
    print i
print 'enddddddd'

print 'naresh'
for i in range(8):
    print i
print 'enddddddd'

print 'naresh'
for i in range(8):
    print i
print 'enddddddd'
 sale_order_name = context["active_id"]
        sale_uid = context["uid"]        
        if file_name == 'Quotation / Order':
            dbname = req.session._db
            db = sql_db.db_connect(dbname) 
            cr = db.cursor()            
            pool =  pooler.get_pool(cr.dbname)
            sale_order_obj = pool['sale.order'].browse(cr,sale_uid, sale_order_name, context)            
            so_name=sale_order_obj.name
            sql_db.close_db(dbname)  
            file_name = dbname+'_QO-'+ so_name[3:] 
