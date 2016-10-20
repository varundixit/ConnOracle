import xml.etree.ElementTree as ET
import cx_Oracle

tree = ET.parse("sql_config.xml")
root = tree.getroot()

#print('Root: ',root)
#print('root.tag:',root.tag)
#print('root.tag.tag:',root.tag)
Conn_Details=''

for child in root:
    #print('Child Tag: ', child.tag,'Child Text:', child.text)
    #print('Child Tag: ', child.tag,'Child Attrib',child.attrib['Name'],'Child Text:', child.text)
    if child.tag=='Connection':
        #print 'Inside Connection',child.tag
        for gc in child:
            #print 'child of Connections:', gc.tag, gc.text 
            if gc.tag=='username':
                username=gc.text
            if gc.tag=='password':
                password=gc.text
            if gc.tag=='hostname':
                hostname=gc.text
            if gc.tag=='port':
                port=gc.text
            if gc.tag=='service_name':
                service_name=gc.text
        Conn_Details = username+'/'+password+'@'+hostname+':'+port+'/'+service_name
                
    
    if child.tag=='Sqls':
        #print 'Inside Sqls:',child.tag
        for gc in child:
            sampleSql=gc.text.replace('\n', ' ').replace('\r', ' ').replace('  ', ' ')
            print 'Sql Query :',sampleSql 
            
            try:
                #print gc.tag
                con = cx_Oracle.connect(Conn_Details)
                #print (con.version)
                cur = con.cursor()
                cur.execute(sampleSql)
                target = open(gc.attrib['OutFileName'], 'w')
                for result in cur:
                    target.write(str(result).replace(' ','')[1:][:-1]+'\n')
                    print str(result).replace(' ','')[1:][:-1]   
                cur.close()
                target.close()
            except Exception as e:
                print("encountered error while connecting to the DB {}".format(e))
        con.close()