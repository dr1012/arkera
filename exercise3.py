class Table:
    def __init__(self, tableName):
        '''
        Constructor of Table class.
        Parameters
        ----------
        tableName : str
            The name of the table on which to operate.
        '''

        self.tableName = tableName
        self.queries = []  
        self.allowed_operators = {'id':['>','<','=','IN','NOTIN'], 'url':['='], 'date':['>','<','='], 'rating':['>','<','=']} 

    def add_query(self, query_list):
        '''
        Adds a query to the list of queries to be converted to SQL.
        Parameters 
        ----------
        query_list: list(str)
            A list of length 3 containing a column name as the first element, an allowed operator as the second element and an argument as the third operator.
        '''

        if(len(query_list)!=3):
            raise Exception('The length of the query list should be 3')
        else:
            if((query_list[0] in self.allowed_operators.keys()) and (query_list[1] in self.allowed_operators[query_list[0]])):
                sql_query =    str(query_list[0]) + ' ' +  str(query_list[1]) + ' ' + str(query_list[2])   
                self.queries.append(sql_query)
            else:
                raise Exception('Your query is wrong, the query list has to be in the format [column name, operator, argument] and should contain appropriate values')

    def to_sql(self):
        '''
        Converts the list of queries for the specific table into SQL.
        '''

        if(len(self.queries)>0 and len(self.queries)<2):
            print('SELECT * FROM ' + self.tableName + ' WHERE ' + self.queries[0] + ';')

        elif(len(self.queries)>1):
            total = 'SELECT * FROM ' + self.tableName + ' WHERE '
            for element in self.queries[:-1]:
                total = total + element + ' AND '
            total = total + self.queries[-1] + ';'
            print(total)

        else:
            raise Exception('There needs to be a least one query to convert to SQL')
            


######### test ##############
myquery = Table('test_table')
myquery.add_query(['id','>','5'])
myquery.add_query(['date','=','20 Jan 2018'])
myquery.add_query(['url','=','"hackernoon.com"'])
myquery.to_sql()