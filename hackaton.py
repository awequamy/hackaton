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
    def update_data(cls,id, **kwargs):
        data=cls.get_data()
        car = cls.get_one_car(data,id)
        index = data.index(car)
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

def main():
    print('1)Create a car\n2)Get data about all the cars\n3)Retrieve data about one car\n4)Update car\n5)Delete car')
    a=int(input('Choose an action:'))
    if a == 1:
        brand=input('Brand:')
        model=input('Model:')
        year=int(input('Year of issue:'))
        volume=float(input('Engine volume:'))
        color=input('Color:')
        body=int(input('Body type:1-sedan,\n2-universal,\n3-coupe,\n4-hatchback,\n5-minivan,\n6-sport ututity vehicle,\n7-pickup\n'))
        if body==1:
            body='Sedan'
        elif body==2:
            body='Universal'
        elif body==3:
            body='Coupe'
        elif body==4:
            body='Hatchback'
        elif body==5:
            body='Minivan'
        elif body==6:
            body='Sport utility vehicle'
        elif body==7:
            body='Pickup'
        mileage=int(input('Milage:'))
        price=float(input('Price:'))
        Cars(brand, model, year, volume,color, body, mileage, price).send_car_to_json
        q=input('do u want to continue?(1-yes,2-no)')
        if q=='1':
            main()
        elif q=='2':
            print('Okay bye bye!')
        else:
            print('Error')
            main()
    elif a==2:
        print(Cars.get_data())
        q=int(input('do u want to continue?(1-yes,2-no)'))
        if q=='1':
            main()
        elif q=='2':
            print('Okay bye bye!')
        else:
            print('Error')
            main()
    elif a==3:
        object=int(input('Enter object index:'))
        print(Cars.retrieve_data(object))
        q=int(input('do u want to continue?(1-yes,2-no)'))
        if q=='1':
            main()
        elif q=='2':
            print('Okay bye bye!')
        else:
            print('Error')
            main()
        
    elif a==4:
        id=int(input('Enter object index:'))
        kwargs = {}
        obj = input('What do you want to change?')
        val = input('What value do you want to change: ')
        kwargs[obj] = val
        print(Cars.update_data(id, **kwargs))
        q=int(input('do u want to continue?(1-yes,2-no)'))
        if q=='1':
            main()
        elif q=='2':
            print('Okay bye bye!')
        else:
            print('Error')
            main()
        
    elif a==5:
        object=int(input('Enter object index:'))
        print(Cars.delete_data(object))
        q=int(input('do u want to continue?(1-yes,2-no)'))
        if q=='1':
            main()
        elif q=='2':
            print('Okay bye bye!')
        else:
            print('Error')
            main()
        
    else:
        print('Error')
        q=int(input('do u want to continue?(1-yes,2-no)'))
        if q=='1':
            main()
        elif q=='2':
            print('Okay bye bye!')
        else:
            print('Error')
            main()

main()