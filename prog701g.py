from Cl701g import Person
from Cl701g import Student
from Cl701g import Teacher
from Cl701g import Admin

def main():
  people = []
  try:
    with open("Dat/Langdat/prog701g.dat", "r") as f:
      num = 0
      while num!=99:
        num = int(f.readline())
        fn = f.readline()
        ln = f.readline()
        if num==1:
          gpa = float(f.readline())
          p=Student(fn,ln,gpa)
          people.append(p)
        if num==2:
          nstu = int(f.readline())
          p=Teacher(fn,ln,nstu)
          people.append(p)
        if num==3:
          fw = f.readline().strip()
          p=Admin(fn,ln,fw)
          people.append(p)
    tot = 0.0
    count = 0
    totstus = 0
    large = ""
    small = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent in ornare tortor, id euismod nunc. Integer faucibus quam sed mollis consectetur. Pellentesque elit nunc, auctor et auctor finibus, vestibulum tempus eros. Mauris auctor lorem in est gravida, sit amet feugiat lacus lacinia. Quisque vulputate, tellus et semper eleifend, dui urna scelerisque nulla, id suscipit erat lorem at nisi. Maecenas nunc odio, porta nec tristique vel, finibus ac mi. Praesent sit amet mi ipsum. Proin est libero, dignissim finibus dolor eu, imperdiet lacinia diam. Nulla condimentum gravida ex consequat imperdiet. Mauris mauris nisl, aliquam in elementum id, dapibus nec tortor. Aenean sit amet facilisis odio. Etiam eget tortor diam. Interdum et malesuada fames ac ante ipsum primis in faucibus. Phasellus viverra eget leo ac condimentum. Integer neque diam, rutrum vitae augue ac, porttitor blandit neque. Quisque ac purus bibendum, convallis libero et, egestas orci. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Vestibulum at ipsum nec leo accumsan dictum vitae eget eros. Phasellus volutpat elementum laoreet. Maecenas volutpat augue id dui volutpat varius. Morbi et consequat ligula. Nullam non urna nulla. In pulvinar, purus at fermentum volutpat, leo est pretium quam, a efficitur diam lorem non odio. Integer hendrerit, mauris at eleifend elementum, purus libero aliquam lacus, eget imperdiet augue lacus at felis. In lectus est, fringilla et mauris vitae, mollis commodo turpis. Aliquam ut ligula at erat cursus elementum porttitor id orci. Nam cursus convallis tellus quis pretium. Ut non fermentum purus. Aliquam erat volutpat. Nulla finibus massa id erat viverra, non maximus odio porta. Aenean sit amet euismod lectus. Cras convallis nunc dapibus suscipit pretium. Morbi ultricies tempus porta. Suspendisse potenti. Quisque vel vulputate lacus. Vestibulum at quam non ipsum tristique scelerisque sed nec libero. Duis pharetra sem a sem dapibus pharetra. Proin aliquam egestas blandit. Mauris sagittis nisi sit amet dignissim imperdiet. Nam tempor eget tellus in mattis. Aenean nec dui leo. Aenean in ex ex. Aenean facilisis diam vitae eros convallis, a venenatis velit posuere. Etiam congue massa a nibh euismod mattis. Donec id posuere leo, eu malesuada arcu. Integer vitae nulla libero. Vivamus lacinia, nulla eu tincidunt tempor, purus dolor tincidunt diam, vitae cursus urna magna non quam. Morbi eu lorem condimentum, cursus dolor in, tristique diam. Phasellus egestas, erat eu porta condimentum, tortor velit porta tortor, a suscipit ante sapien in diam. Aliquam vitae neque nec urna semper vulputate. Proin viverra orci quis est egestas, quis eleifend velit condimentum. Aenean lacus neque, porttitor vel rhoncus consequat, lobortis et nisi. Nulla egestas tincidunt faucibus. Suspendisse in turpis libero. Duis ut dui risus. Maecenas tincidunt eros sit amet odio vestibulum, nec interdum urna auctor. Praesent malesuada mi ut egestas tincidunt. Maecenas cursus neque mi, id rhoncus erat lacinia at. Sed aliquam erat elit, non pellentesque massa ultricies eget. Etiam non purus enim. Cras sem ante, auctor at scelerisque at, consequat nec libero. Suspendisse quis neque cursus, sodales velit et, faucibus lorem. Curabitur aliquet dui non dolor pharetra suscipit. Donec vulputate accumsan malesuada."

    for person in people:
      if isinstance(person, Student):
        
        tot += person.gpa
        count += 1
        
      elif isinstance(person, Teacher):
        
        totstus += person.numStudents
        
      elif isinstance(person,Admin):
        
        fw = person.word
        if len(fw)>len(large):
          
          large = fw
          
        if len(fw)<len(small):
          
          small = fw
    
    print(f"Average Student GPA: {round(tot/count, 2)}")
    print(f"Total Students: {totstus}")
    print("Largest: "+large)
    print("Smallest: "+small)
  
  except Exception as e:

    print("Error", e)


if __name__=="__main__":
  main()