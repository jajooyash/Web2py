# -*- coding: utf-8 -*-
# try something lik
        
        #foundRecord[0].No_Of_Courses=
def index(): 
        response.menu +=studentmenu
        message=(auth.user.first_name)+' '+(auth.user.last_name)
        q1 = db.User_Profile.SID == auth.user.id
        foundRecord = db(q1).select()
        StudentId = foundRecord[0].id
        q2 = db.User_Profile.id == StudentId
        return locals()
        
def take_course():
        response.menu +=studentmenu
        form = SQLFORM.factory(Field('No_Of_Courses',requires=IS_IN_SET(['1', '2', '3','4','5'])),Field('No_Of_Project',requires=IS_IN_SET(['0','1', '2', '3','4','5'])))
        if form.process().accepted:
                query=(db.User_Profile.SID == auth.user.id)
                db(query).update(No_Of_Courses=form.vars.No_Of_Courses)
                db(query).update(No_Of_Project=form.vars.No_Of_Project)
                response.flash = 'Courses Entered'
                redirect(URL('Students','fill_course'))
        elif form.errors:
                response.flash = 'Form Has Errors'
        else:
                response.flash = 'Please Fill Courses'
        return locals()

def fill_course():
        response.menu +=studentmenu
        q1 = db.User_Profile.SID == auth.user.id
        StudentRecord = db(q1).select()
        Cos=StudentRecord[0].No_Of_Courses
        Pro=StudentRecord[0].No_Of_Project
        Academic=db(db.Academic_Office).select()
        Professor=db(db.Professor_Profile).select()
        
        return locals()

def Check():
        response.menu +=studentmenu
        a=request.vars
        Projects=a['project']
        Courses=a['courses']
        Title=a['title']
        q1 = db.User_Profile.SID == auth.user.id
        StudentRecord = db(q1).select()
        Cos=StudentRecord[0].No_Of_Courses
        Pro=StudentRecord[0].No_Of_Project
        email=StudentRecord[0].Email_id
        cour_send='Hi\nYou have Registered for the following Courses & Projects\n\n'
        end='\nFinal Course Allocation would be done later. \nFor any enquiry contact admin@iiit.ac.in\n\nRegards\nAdmin'
        add1=''
        add2=''
        if(Cos==1):
                 p1=Courses.split(')')
                 p=p1[0]+')'
                 add1=add1+'\t1. '+ Courses+'\n'
                 db(q1).update(Course1=p)
                 db(q1).update(Course2='')
                 db(q1).update(Course3='')
                 db(q1).update(Course4='')
                 db(q1).update(Course5='')
        elif(Cos==2):
                 p1=Courses[0].split(')')
                 p=p1[0]+')'
                 add1=add1+'\t1. '+ Courses[0]+'\n'
                 db(q1).update(Course1=p)
                 p1=Courses[1].split(')')
                 p=p1[0]+')'
                 add1=add1+'\t2. '+ Courses[1]+'\n'
                 db(q1).update(Course2=p)
                 db(q1).update(Course3='')
                 db(q1).update(Course4='')
                 db(q1).update(Course5='')
        elif(Cos==3):
                 p1=Courses[0].split(')')
                 p=p1[0]+')'
                 add1=add1+'\t1. '+ Courses[0]+'\n'
                 db(q1).update(Course1=p)
                 p1=Courses[1].split(')')
                 p=p1[0]+')'
                 add1=add1+'\t2. '+ Courses[1]+'\n'
                 db(q1).update(Course2=p)
                 p1=Courses[2].split(')')
                 p=p1[0]+')'
                 add1=add1+'\t3. '+ Courses[2]+'\n'
                 db(q1).update(Course3=p)
                 db(q1).update(Course4='')
                 db(q1).update(Course5='')
        elif(Cos==4):
                 p1=Courses[0].split(')')
                 p=p1[0]+')'
                 add1=add1+'\t1. '+ Courses[0]+'\n'
                 db(q1).update(Course1=p)
                 p1=Courses[1].split(')')
                 p=p1[0]+')'
                 add1=add1+'\t2. '+ Courses[1]+'\n'
                 db(q1).update(Course2=p)
                 p1=Courses[2].split(')')
                 p=p1[0]+')'
                 add1=add1+'\t3. '+ Courses[2]+'\n'
                 db(q1).update(Course3=p)
                 p1=Courses[3].split(')')
                 p=p1[0]+')'
                 add1=add1+'\t4. '+ Courses[3]+'\n'
                 db(q1).update(Course4=p)
                 db(q1).update(Course5='')
        elif(Cos==5):
                 p1=Courses[0].split(')')
                 p=p1[0]+')'
                 add1=add1+'\t1. '+ Courses[0]+'\n'
                 db(q1).update(Course1=p)
                 p1=Courses[1].split(')')
                 p=p1[0]+')'
                 add1=add1+'\t2. '+ Courses[1]+'\n'   
                 db(q1).update(Course2=p)
                 p1=Courses[2].split(')')
                 p=p1[0]+')'
                 add1=add1+'\t3. '+ Courses[2]+'\n'   
                 db(q1).update(Course3=p)
                 p1=Courses[3].split(')')
                 p=p1[0]+')'
                 add1=add1+'\t4. '+ Courses[3]+'\n'
                 db(q1).update(Course4=p)
                 p1=Courses[4].split(')')
                 p=p1[0]+')'
                 add1=add1+'\t5. '+ Courses[4]+'\n'
                 db(q1).update(Course5=p)
        else:
                 db(q1).update(Course1='')
                 db(q1).update(Course2='')
                 db(q1).update(Course3='')
                 db(q1).update(Course4='')
                 db(q1).update(Course5='')
        
        if(Pro==1):
                 db(q1).update(Project1=Projects)
                 if Title:
                         add2='\ta. '+'Title :'+Title+'\tunder '+ Projects+'\n'
                 else:
                        add2='\ta. '+ Projects+'\n'
                 db(q1).update(Project1_Title=Title)
                 db(q1).update(Project2='')
                 db(q1).update(Project2_Title='')
                 db(q1).update(Project3='')
                 db(q1).update(Project3_Title='')
                 db(q1).update(Project4='')
                 db(q1).update(Project4_Title='')
                 db(q1).update(Project5='')
                 db(q1).update(Project5_Title='')
        elif(Pro==2):
                 db(q1).update(Project1=Projects[0])
                 if Title[0]:
                         add2='\ta. '+'Title :'+Title[0]+'\tunder '+ Projects[0]+'\n'
                 else:
                        add2='\ta. '+ Projects[0]+'\n'
                 db(q1).update(Project1_Title=Title[0])
                 db(q1).update(Project2=Projects[1])
                 if Title[1]:
                         add2=add2+'\tb. '+'Title :'+Title[1]+'\tunder '+ Projects[1]+'\n'
                 else:
                        add2=add2+'\tb. '+ Projects[1]+'\n'
                 db(q1).update(Project2_Title=Title[1])
                 db(q1).update(Project3='')
                 db(q1).update(Project3_Title='')
                 db(q1).update(Project4='')
                 db(q1).update(Project4_Title='')
                 db(q1).update(Project5='')
                 db(q1).update(Project5_Title='')
        elif(Pro==3):
                 db(q1).update(Project1=Projects[0])
                 if Title[0]:
                         add2='\ta. '+'Title :'+Title[0]+'\tunder '+ Projects[0]+'\n'
                 else:
                        add2='\ta. '+ Projects[0]+'\n'
                 db(q1).update(Project1_Title=Title[0])
                 db(q1).update(Project2=Projects[1])
                 if Title[1]:
                         add2=add2+'\tb. '+'Title :'+Title[1]+'\tunder '+ Projects[1]+'\n'
                 else:
                        add2=add2+'\tb. '+ Projects[1]+'\n'
                 db(q1).update(Project2_Title=Title[1])
                 db(q1).update(Project3=Projects[2])
                 if Title[2]:
                         add2=add2+'\tc. '+'Title :'+Title[2]+'\tunder '+ Projects[2]+'\n'
                 else:
                        add2=add2+'\tc. '+ Projects[2]+'\n'
                 db(q1).update(Project3_Title=Title[2])
                 db(q1).update(Project4='')
                 db(q1).update(Project4_Title='')
                 db(q1).update(Project5='')
                 db(q1).update(Project5_Title='')
        elif(Pro==4):
                 db(q1).update(Project1=Projects[0])
                 if Title[0]:
                         add2='\ta. '+'Title :'+Title[0]+'\tunder '+ Projects[0]+'\n'
                 else:
                        add2='\ta. '+ Projects[0]+'\n'
                 db(q1).update(Project1_Title=Title[0])
                 db(q1).update(Project2=Projects[1])
                 if Title[1]:
                         add2=add2+'\tb. '+'Title :'+Title[1]+'\tunder '+ Projects[1]+'\n'
                 else:
                        add2=add2+'\tb. '+ Projects[1]+'\n'
                 db(q1).update(Project2_Title=Title[1])
                 db(q1).update(Project3=Projects[2])
                 if Title[2]:
                         add2=add2+'\tc. '+'Title :'+Title[2]+'\tunder '+ Projects[2]+'\n'
                 else:
                        add2=add2+'\tc. '+ Projects[2]+'\n'
                 db(q1).update(Project3_Title=Title[2])
                 db(q1).update(Project4=Projects[3])
                 if Title[3]:
                         add2=add2+'\td. '+'Title :'+Title[3]+'\tunder '+ Projects[3]+'\n'
                 else:
                        add2=add2+'\td. '+ Projects[3]+'\n'
                 db(q1).update(Project4_Title=Title[3])
                 db(q1).update(Project5='')
                 db(q1).update(Project5_Title='')
        elif(Pro==5):
                 db(q1).update(Project1=Projects[0])
                 if Title[0]:
                         add2='\ta. '+'Title :'+Title[0]+'\tunder '+ Projects[0]+'\n'
                 else:
                        add2='\ta. '+ Projects[0]+'\n'
                 db(q1).update(Project1_Title=Title[0])
                 db(q1).update(Project2=Projects[1])
                 if Title[1]:
                         add2=add2+'\tb. '+'Title :'+Title[1]+'\tunder '+ Projects[1]+'\n'
                 else:
                        add2=add2+'\tb. '+ Projects[1]+'\n'
                 db(q1).update(Project2_Title=Title[1])
                 db(q1).update(Project3=Projects[2])
                 if Title[2]:
                         add2=add2+'\tc. '+'Title :'+Title[2]+'\tunder '+ Projects[2]+'\n'
                 else:
                        add2=add2+'\tc. '+ Projects[2]+'\n'
                 db(q1).update(Project3_Title=Title[2])
                 db(q1).update(Project4=Projects[3])
                 if Title[3]:
                         add2=add2+'\td. '+'Title :'+Title[3]+'\tunder '+ Projects[3]+'\n'
                 else:
                        add2=add2+'\td. '+ Projects[3]+'\n'
                 db(q1).update(Project4_Title=Title[3])
                 db(q1).update(Project5=Projects[4])
                 if Title[4]:
                         add2=add2+'\te. '+'Title :'+Title[4]+'\tunder '+ Projects[4]+'\n'
                 else:
                        add2=add2+'\te. '+ Projects[4]+'\n'
                 db(q1).update(Project5_Title=Title[4])
        else:
                 db(q1).update(Project1='')
                 db(q1).update(Project1_Title='')
                 db(q1).update(Project2='')
                 db(q1).update(Project2_Title='')
                 db(q1).update(Project3='')
                 db(q1).update(Project3_Title='')
                 db(q1).update(Project4='')
                 db(q1).update(Project4_Title='')
                 db(q1).update(Project5='')
                 db(q1).update(Project5_Title='')        
        
        if(Cos>0 & Cos<6):
                cour_send=cour_send +'Courses Taken : '+str(Cos)+'\n\n'+ add1 +'\n' 
        if(Pro>0 & Pro<6):
                cour_send=cour_send +'Project Under\n\n' +add2 +'\n'
        cour_send=cour_send+end
        mail.send(to=[email],subject="Courses Registered",message=cour_send)
        redirect(URL('default','index'))
        return locals()

def profile():
    response.menu +=studentmenu
    q1 = db.User_Profile.SID == auth.user.id
    form = db(q1).select()
    return locals()
def course_taken():
        response.menu +=studentmenu
        q1 = db.User_Profile.SID == auth.user.id
        StudentRecord = db(q1).select()
        Cos=StudentRecord[0].No_Of_Courses
        Pro=StudentRecord[0].No_Of_Project
        a=[]
        b=[]
        c=[]
        if(Cos==1):
            a.append( StudentRecord[0].Course1)
        elif(Cos==2):
            a.append( StudentRecord[0].Course1)
            a.append( StudentRecord[0].Course2)
        elif(Cos==3):
            a.append( StudentRecord[0].Course1)
            a.append( StudentRecord[0].Course2)
            a.append( StudentRecord[0].Course3)
        elif(Cos==4):
            a.append( StudentRecord[0].Course1)
            a.append( StudentRecord[0].Course2)
            a.append( StudentRecord[0].Course3)
            a.append( StudentRecord[0].Course4)
        elif(Cos==5):
            a.append( StudentRecord[0].Course1)
            a.append( StudentRecord[0].Course2)
            a.append( StudentRecord[0].Course3)
            a.append( StudentRecord[0].Course4)
            a.append( StudentRecord[0].Course5)
        if(Pro==1):
            b.append( StudentRecord[0].Project1)
            c.append( StudentRecord[0].Project1_Title)
        elif(Pro==2):
            b.append( StudentRecord[0].Project1)
            b.append( StudentRecord[0].Project2)
            c.append( StudentRecord[0].Project1_Title)
            c.append( StudentRecord[0].Project2_Title)
        elif(Pro==3):
            b.append( StudentRecord[0].Project1)
            b.append( StudentRecord[0].Project2)
            b.append( StudentRecord[0].Project3)
            c.append( StudentRecord[0].Project1_Title)
            c.append( StudentRecord[0].Project2_Title)
            c.append( StudentRecord[0].Project3_Title)
        elif(Pro==4):
            b.append( StudentRecord[0].Project1)
            b.append( StudentRecord[0].Project2)
            b.append( StudentRecord[0].Project3)
            b.append( StudentRecord[0].Project)
            c.append( StudentRecord[0].Project1_Title)
            c.append( StudentRecord[0].Project2_Title)
            c.append( StudentRecord[0].Project3_Title)
            c.append( StudentRecord[0].Project_Title)
        elif(Pro==5):
            b.append( StudentRecord[0].Project1)
            b.append( StudentRecord[0].Project2)
            b.append( StudentRecord[0].Project3)
            b.append( StudentRecord[0].Project4)
            b.append( StudentRecord[0].Project5)
            c.append( StudentRecord[0].Project1_Title)
            c.append( StudentRecord[0].Project2_Title)
            c.append( StudentRecord[0].Project3_Title)
            c.append( StudentRecord[0].Project4_Title)
            c.append( StudentRecord[0].Project5_Title)
        return locals()

def profile1():
        type=auth.user.UserType
        if type=='Student':
            response.menu +=studentmenu
        else:
            response.menu +=professormenu
        q1 = db.User_Profile.SID == auth.user.id
        foundRecord = db(q1).select()
        if not foundRecord:
            form = SQLFORM(db.User_Profile, fields=[ 'Rollno', 'Dob','Gender','Stream','Program','Years','CGPA','Mobileno','Place','Courses_Taken','Project_Done','Image_Upload'])
            form.vars['SID'] = auth.user.id
            form.vars['First_name']=auth.user.first_name
            form.vars['Last_name']=auth.user.last_name
            form.vars['Email_id']=auth.user.email
            if form.process().accepted:
                response.flash = 'form accepted'
                redirect(URL('index'))
            elif form.errors:
                response.flash = 'form has errors'
            else:
                response.flash = 'please fill out the form'
    
            return dict(form=form)               

        else:
            StudentId = foundRecord[0].id
            query=db.User_Profile.id==StudentId
            form=db(query).select()
            return dict(form=form)

def profile_view():
    response.menu +=studentmenu
    q1 = db.User_Profile.SID == auth.user.id
    db.User_Profile.SID.writable = False
    db.User_Profile.SID.readable = False
    db.User_Profile.id.readable = False
    db.User_Profile.Email_id.writable=False
    db.User_Profile.Rollno.writable=False
    db.User_Profile.No_Of_Courses.readable=False
    db.User_Profile.No_Of_Courses.writable=False
    db.User_Profile.No_Of_Project.readable=False
    db.User_Profile.No_Of_Project.writable=False
    db.User_Profile.Filled.readable=False
    db.User_Profile.Filled.writable=False
    db.User_Profile.Courses_Taken.readable=False
    db.User_Profile.Courses_Taken.writable=False
    db.User_Profile.Project_Done.readable=False
    db.User_Profile.Project_Done.writable=False
    db.User_Profile.Course1.readable=False
    db.User_Profile.Course1.writable=False
    db.User_Profile.Course2.readable=False
    db.User_Profile.Course2.writable=False
    db.User_Profile.Course3.readable=False
    db.User_Profile.Course3.writable=False
    db.User_Profile.Course4.readable=False
    db.User_Profile.Course4.writable=False
    db.User_Profile.Course5.readable=False
    db.User_Profile.Course5.writable=False
    db.User_Profile.Course1_Flag.readable=False
    db.User_Profile.Course1_Flag.writable=False
    db.User_Profile.Course2_Flag.readable=False
    db.User_Profile.Course2_Flag.writable=False
    db.User_Profile.Course3_Flag.readable=False
    db.User_Profile.Course3_Flag.writable=False
    db.User_Profile.Course4_Flag.readable=False
    db.User_Profile.Course4_Flag.writable=False
    db.User_Profile.Course5_Flag.readable=False
    db.User_Profile.Course5_Flag.writable=False
    db.User_Profile.Project1.readable=False
    db.User_Profile.Project1.writable=False
    db.User_Profile.Project2.readable=False
    db.User_Profile.Project2.writable=False
    db.User_Profile.Project3.readable=False
    db.User_Profile.Project3.writable=False
    db.User_Profile.Project4.readable=False
    db.User_Profile.Project4.writable=False
    db.User_Profile.Project5.readable=False
    db.User_Profile.Project5.writable=False
    db.User_Profile.Project1_Title.readable=False
    db.User_Profile.Project1_Title.writable=False
    db.User_Profile.Project2_Title.readable=False
    db.User_Profile.Project2_Title.writable=False
    db.User_Profile.Project3_Title.readable=False
    db.User_Profile.Project3_Title.writable=False
    db.User_Profile.Project4_Title.readable=False
    db.User_Profile.Project4_Title.writable=False
    db.User_Profile.Project5_Title.readable=False
    db.User_Profile.Project5_Title.writable=False
    form=SQLFORM.grid(q1, fields=[ db.User_Profile.First_name,  db.User_Profile.Last_name,  db.User_Profile.Rollno,db.User_Profile.Dob,db.User_Profile.Gender,db.User_Profile.Email_id,db.User_Profile.Stream,db.User_Profile.Program,db.User_Profile.Years,db.User_Profile.CGPA,db.User_Profile.Mobileno,db.User_Profile.Place,db.User_Profile.Image_Upload], deletable=False, csv=False, create=False, searchable=False)
    return locals()
def course_Des():
        response.menu +=studentmenu
        form=db(db.Academic_Office).select(orderby=~db.Academic_Office.Course_id)
        return locals()
