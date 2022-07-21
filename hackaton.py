import json

class Cars():

    id=0
    FILE='car_list.json'

    def __init__(self,marka,model,year,volume_of_engine,color,body_type,mileage,price):
        self.marka=marka
        self.model=model
        self.year=year
        self.volume_of_engine=volume_of_engine
        self.color=color
        self.body_type=body_type
        self.mileage=mileage
        self.price=price
        self.send_car_to_json()

    @classmethod
    def get_car_id(cls):
        cls.id+=1
        return cls.id

    @classmethod
    def get_data(cls):
        with open(cls.FILE) as file:
            return json.load(file)
    
    @staticmethod
    def get_one_car(data,id):
        car=list(filter(lambda x:x['id']==id,data))
        if not car:
            return 'There is no such a product'
        return car[0]

    @classmethod
    def send_data_to_json(cls,data):
        with open(cls.FILE,'w') as file:
            json.dump(data,file)

    def send_car_to_json(self):
        data=Cars.get_data()
        car={
            'id':Cars.get_car_id(),
            'marka':self.marka,
            'model':self.model, 
            'year':self.year, 
            'volume_of_engine':self.volume_of_engine, 
            'color':self.color, 
            'body_type':self.body_type, 
            'mileage':self.mileage, 
            'price':self.price
            }
        data.append(car)
        
        with open(Cars.FILE,'w') as file:
            json.dump(data,file)
        return {'status':'201','msg':car}

    @classmethod
    def retrieve_data(cls,id):
        data=cls.get_data()
        car=cls.get_one_car(data,id)
        return car

    @classmethod
    def update_data(cls,id, **kwargs):
        data=cls.get_data()
        car=cls.get_one_car(data,id)
        if type(car)!=dict:
            return car
        index=data.index(car)
        data[index].update(**kwargs)
        cls.send_data_to_json(data)
        return{'status':'200','msg':'Updated'}

    @classmethod
    def delete_data(cls,id):
        data=cls.get_data()
        car=cls.get_one_car(data,id)
        if type(car)!=dict:
            return car

        index=data.index(car)
        data.pop(index)
        cls.send_data_to_json(data)
        return{'status':'204','msg':'Deleted'}

    @classmethod
    def update(cls,**kwargs):
            data=cls.get_car_list()


    @classmethod
    def update_data(cls,id, **kwargs):
        data=cls.get_data()
        car=cls.get_one_car(data,id)
        if type(car)!=dict:
            return car
        index=data.index(car)
        data[index].update(**kwargs)
        cls.send_data_to_json(data)
        return{'status':'200','msg':'Updated'}

    @classmethod
    def delete_data(cls,id):
        data=cls.get_data()
        product=cls.get_one_car(data,id)
        if type(product)!=dict:
            return product

        index=data.index(product)
        data.pop(index)
        cls.send_data_to_json(data)
        return{'status':'204','msg':'Deleted'}


with open(Cars.FILE,'w') as file:
    json.dump([], file)

obj=Cars('marka','model',2007,20,'pink','universal',800,100000)
print('все продукты:\n', Cars.get_data())
print(Cars.retrieve_data(3))
print(Cars.update_data(3,model='model2'))
print(Cars.retrieve_data(3))
print(Cars.delete_data(3))
print('все продукты:\n', Cars.get_data())

    

        
