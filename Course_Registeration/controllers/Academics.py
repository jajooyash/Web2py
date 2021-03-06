# -*- coding: utf-8 -*-
# try something like
def index():
    response.menu +=Adminmenu
    response.flash = 'Welcome Admin'
    return dict(message='Admin')
    
def faculty_registered():
    response.menu +=Adminmenu
    form = db(db.Professor_Profile).select(orderby=db.Professor_Profile.id)
    return dict(form=form)

def student_registered():
    response.menu +=Adminmenu
    form = db(db.User_Profile).select(orderby=db.User_Profile.Rollno)
    return dict(form=form)

def my_form_processing(form):
        s = form.vars.Assigned_Professor
        q1 = db.Professor_Profile.PID == s
        foundRecord = db(q1).select()
        w=foundRecord[0].Courses_Allocated
        t=foundRecord[0].No_Of_Courses_Assigned
        form.vars.Employee_Id=foundRecord[0].Employee_Id
        form.vars.First_name=foundRecord[0].First_name
        form.vars.Last_name=foundRecord[0].Last_name
        query=(db.Professor_Profile.PID == s)
        if not w:
            db(query).update(Courses_Allocated=form.vars.Course_id)
        else:
            at=w + ',' + form.vars.Course_id
            db(query).update(Courses_Allocated=at)
        tas=int(t)+1
        db(query).update(No_Of_Courses_Assigned=str(tas))
            
def course_entry():
    response.menu +=Adminmenu
    form=SQLFORM(db.Academic_Office,fields=['Course_Name','Course_id','Assigned_Professor','Credits','Course_Description','Min_Students']) 
    if form.process(onvalidation=my_form_processing).accepted:
            response.flash= 'form accepted'
            redirect(URL('Academics','index'))
    elif form.errors:
           response.flash = 'form has errors'
    else:
           response.flash = 'please fill out the form'
    return dict(form=form)

def Delete():
        response.menu +=Adminmenu
        Courses_Details=db(db.Academic_Office).select()
        return locals()
def Delete_Process():
    a1=request.vars
    a=a1['jet']
    sp1=a.split(')')
    d=sp1[0]
    Course=sp1[0]+')'
    b=sp1[1]
    sp2=b.split('(')
    Admin_Id=sp2[1]
    c=sp2[0]
    sp3=c.split(' ')
    Prof=sp3[3] +sp3[4]
    sp4=d.split('(')
    Corid=sp4[1]
    q1=db.Academic_Office.Course_id==Corid
    operation1=db(q1).delete()
    q2=db.Professor_Profile.PID==Admin_Id
    operation1=db(q2).select()
    q=operation1[0].No_Of_Courses_Assigned
    tut=int(q)-1
    query=(db.Professor_Profile.PID == Admin_Id)
    db(query).update(No_Of_Courses_Assigned=tut)
    course_have=operation1[0].Courses_Allocated
    sp5=course_have.split(',')
    up=''
    for i in range(0,len(sp5)):
        if(sp5[i]==Corid):
            pass
        else:
            if not up:
                up=up+sp5[i]
            else:
                up=up+','+sp5[i]
    opeartion2=db(q2).update(Courses_Allocated=up)
    redirect(URL('Academics','index'))
    return locals()
def View():
        response.menu +=Adminmenu
        Course_Update=db(db.Academic_Office).select()
        return locals()
    
def Sort():
         response.menu +=Adminmenu
         bc=db(db.User_Profile).select(orderby=~db.User_Profile.CGPA)
         return locals()
def Check():
    response.menu +=Adminmenu
    q1 = db.User_Profile.SID == auth.user.id
    db.User_Profile.SID.writable = False
    db.User_Profile.SID.readable = False
    db.User_Profile.id.readable = False
    db.User_Profile.Email_id.writable=False
    db.User_Profile.Rollno.writable=False
    db.User_Profile.No_Of_Courses.writable=False
    db.User_Profile.No_Of_Project.writable=False
    db.User_Profile.Filled.readable=False
    db.User_Profile.Filled.writable=False
    db.User_Profile.Courses_Taken.readable=False
    db.User_Profile.Project_Done.writable=False
    db.User_Profile.Course1.writable=False
    db.User_Profile.Course2.writable=False
    db.User_Profile.Course3.writable=False
    db.User_Profile.Course4.writable=False
    db.User_Profile.Course5.writable=False
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
    form=SQLFORM.grid(db.User_Profile, fields=[ db.User_Profile.First_name,  db.User_Profile.Last_name,  db.User_Profile.Rollno,db.User_Profile.Email_id,db.User_Profile.Stream,db.User_Profile.Program,db.User_Profile.Years,db.User_Profile.CGPA,db.User_Profile.Course1,db.User_Profile.Course1_Flag,db.User_Profile.Course2,db.User_Profile.Course2_Flag,db.User_Profile.Course3,db.User_Profile.Course3_Flag,db.User_Profile.Course4,db.User_Profile.Course4_Flag,db.User_Profile.Course5,db.User_Profile.Course5_Flag], deletable=True, csv=False, create=False, searchable=False,user_signature=False,details=False,orderby=~db.User_Profile.CGPA)
    return locals()

def Sortbybranch():
    response.menu +=Adminmenu
    q1 = db.User_Profile.SID == auth.user.id
    db.User_Profile.SID.writable = False
    db.User_Profile.SID.readable = False
    db.User_Profile.id.readable = False
    db.User_Profile.Email_id.writable=False
    db.User_Profile.Rollno.writable=False
    db.User_Profile.No_Of_Courses.writable=False
    db.User_Profile.No_Of_Project.writable=False
    db.User_Profile.Filled.readable=False
    db.User_Profile.Filled.writable=False
    db.User_Profile.Courses_Taken.readable=False
    db.User_Profile.Project_Done.writable=False
    db.User_Profile.Course1.writable=False
    db.User_Profile.Course2.writable=False
    db.User_Profile.Course3.writable=False
    db.User_Profile.Course4.writable=False
    db.User_Profile.Course5.writable=False
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
    form=SQLFORM.grid(db.User_Profile, fields=[ db.User_Profile.First_name,  db.User_Profile.Last_name,  db.User_Profile.Rollno,db.User_Profile.Email_id,db.User_Profile.Stream,db.User_Profile.Program,db.User_Profile.Years,db.User_Profile.CGPA,db.User_Profile.Course1,db.User_Profile.Course1_Flag,db.User_Profile.Course2,db.User_Profile.Course2_Flag,db.User_Profile.Course3,db.User_Profile.Course3_Flag,db.User_Profile.Course4,db.User_Profile.Course4_Flag,db.User_Profile.Course5,db.User_Profile.Course5_Flag], deletable=True, csv=False, create=False, searchable=False,user_signature=False,details=False,orderby=db.User_Profile.Stream)
    return locals()
def Sortbyprogram():
    response.menu +=Adminmenu
    q1 = db.User_Profile.SID == auth.user.id
    db.User_Profile.SID.writable = False
    db.User_Profile.SID.readable = False
    db.User_Profile.id.readable = False
    db.User_Profile.Email_id.writable=False
    db.User_Profile.Rollno.writable=False
    db.User_Profile.No_Of_Courses.writable=False
    db.User_Profile.No_Of_Project.writable=False
    db.User_Profile.Filled.readable=False
    db.User_Profile.Filled.writable=False
    db.User_Profile.Courses_Taken.readable=False
    db.User_Profile.Project_Done.writable=False
    db.User_Profile.Course1.writable=False
    db.User_Profile.Course2.writable=False
    db.User_Profile.Course3.writable=False
    db.User_Profile.Course4.writable=False
    db.User_Profile.Course5.writable=False
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
    form=SQLFORM.grid(db.User_Profile, fields=[ db.User_Profile.First_name,  db.User_Profile.Last_name,  db.User_Profile.Rollno,db.User_Profile.Email_id,db.User_Profile.Stream,db.User_Profile.Program,db.User_Profile.Years,db.User_Profile.CGPA,db.User_Profile.Course1,db.User_Profile.Course1_Flag,db.User_Profile.Course2,db.User_Profile.Course2_Flag,db.User_Profile.Course3,db.User_Profile.Course3_Flag,db.User_Profile.Course4,db.User_Profile.Course4_Flag,db.User_Profile.Course5,db.User_Profile.Course5_Flag], deletable=True, csv=False, create=False, searchable=False,user_signature=False,details=False,orderby=db.User_Profile.Program)
    return locals()
def Edit():
    response.menu +=Adminmenu
    form=SQLFORM.grid(db.Academic_Office,fields=[db.Academic_Office.Course_Name,db.Academic_Office.Course_id,db.Academic_Office.Assigned_Professor,db.Academic_Office.Credits,db.Academic_Office.Course_Description,db.Academic_Office.Min_Students],csv=False, create=False, searchable=False,user_signature=False) 
    return locals()
