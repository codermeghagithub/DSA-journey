class Dog:
    name="bool"
    def __init__(self):
        self.name_type="animal"
        self.eyecol="black"

p1=Dog()
p2=Dog() 
p2.name_type="jiolnk"

p2.eyecol="brown"
# Dog.name="small"   #if i clall by class so this is update form first
p2.name="jjj"        #WHEN I CALL BY OBJECT NAME IN THAT TIME VALUE UPDATE FROM SECOND TIME
print(p1.name,p1.name_type,p1.eyecol)  
print(p2.name,p2.name_type,p2.eyecol)  