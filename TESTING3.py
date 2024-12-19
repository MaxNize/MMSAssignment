from Programm import Programm

p = Programm()
p.UserManager.createUser("m", "m", "m", "m@m.m", "m")
print(p.UserManager.users)
p.UserManager.active = p.UserManager.getUser("m")
p.UserManager.active.sendMail("test", "m@m.m", "m@m.m", "m@m.m", "m@m.m", "test", "test")
p.mainloop()