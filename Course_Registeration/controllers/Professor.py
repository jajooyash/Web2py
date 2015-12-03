# -*- coding: utf-8 -*-
# try something like
import string
string.ascii_uppercase


def index(): 
        response.menu +=professormenu
        message=(auth.user.first_name)+' '+(auth.user.last_name)
        q1 = db.Professor_Profile.PID == auth.user.id
        foundRecord = db(q1).select()
        ProfessorId = foundRecord[0].id
        q2 = db.Professor_Profile.id == ProfessorId
        form=db(q2).select(db.Professor_Profile.Image_Upload)
        return locals()

def Courses_Assigned():
        response.menu +=professormenu
        message=(auth.user.first_name)+' '+(auth.user.last_name)
        q1 = db.Professor_Profile.PID == auth.user.id
        foundRecord = db(q1).select()
        t1=foundRecord[0].Courses_Allocated
        t2=foundRecord[0].No_Of_Courses_Assigned
        aer=[]
        t2=t1.upper()
        t=t2.split(',')
        for i in t:
            ads=i.lower()
            q2=db.Academic_Office.Course_id==ads
            forw=db(q2).select()
            aer.append(str(forw[0].Course_Description))
        return locals()
    
def Courses_Description_edit():
        response.menu +=professormenu
        message=(auth.user.first_name)+' '+(auth.user.last_name)
        q1 = db.Academic_Office.Assigned_Professor == auth.user.id
        q2= db.Professor_Profile.PID==auth.user.id
        form1=db(q2).select()
        atd=form1[0].No_Of_Courses_Assigned
        if(int(atd)>0):
            form=db(q1).select()
        else:
              redirect(URL('Professor','index'))
        return locals()
def Enrolled():
        response.menu +=professormenu
        b1=request.args
        b2=b1[0]
        b=b2.lower()
        q1 = db.Academic_Office.Course_id == b
        foundRecord = db(q1).select()
        a3=foundRecord[0].Course_Name
        a=a3 + '('+ b + ')'
        q2 = db.User_Profile.Course1 == a
        q21= db.User_Profile.Course1_Flag==True
        q3 = db.User_Profile.Course2 == a
        q31= db.User_Profile.Course2_Flag==True
        q4 = db.User_Profile.Course3 == a
        q41= db.User_Profile.Course3_Flag==True
        q5 = db.User_Profile.Course4 == a
        q51= db.User_Profile.Course4_Flag==True
        q6 = db.User_Profile.Course5 == a
        q61= db.User_Profile.Course5_Flag==True
        SearchRecord= db((q2 & q21)| (q3 & q31)|(q4 & q41)|(q5 & q51)|(q6 & q61)).select(orderby=~db.User_Profile.CGPA)
        return locals()

def profile():
    response.menu +=professormenu
    q1 = db.Professor_Profile.PID == auth.user.id
    form = db(q1).select()
    return locals()

def profile1():
    type=auth.user.UserType
    if type=='Student':
        response.menu +=studentmenu
    else:
        response.menu +=professormenu
        
    if auth.user.UserType == 'Professor':
        q1 = db.Professor_Profile.PID == auth.user.id
        foundRecord = db(q1).select()

        if not foundRecord:
            form = SQLFORM(db.Professor_Profile,fields=['Employee_Id', 'Department','Gender','Mobileno','Courses_Previously_Taken','Image_Upload'])
            form.vars['PID'] = auth.user.id
            form.vars['First_name']=auth.user.first_name
            form.vars['Last_name']=auth.user.last_name
            form.vars['Email_id']=auth.user.email
            if form.process().accepted:
                response.flash = 'form accepted'
                redirect(URL('Professor','index'))
            elif form.errors:
                response.flash = 'form has errors'
            else:
                response.flash = 'please fill out the form'
        
            return dict(form=form)
        else:
            ProfessorId = foundRecord[0].id
            q1 = db.Professor_Profile.id == ProfessorId
            form=db(q1).select()
            return dict(form=form)
        
def profile_view():   
    response.menu +=professormenu
    q1 = db.Professor_Profile.PID == auth.user.id
    db.Professor_Profile.PID.writable = False
    db.Professor_Profile.PID.readable = False
    db.Professor_Profile.id.readable = False
    db.Professor_Profile.id.writable = False
    db.Professor_Profile.Employee_Id.writable=False
    db.Professor_Profile.Email_id.writable=False
    db.Professor_Profile.Courses_Allocated.readable=False
    db.Professor_Profile.Courses_Allocated.writable=False
    db.Professor_Profile.No_Of_Courses_Assigned.readable=False
    db.Professor_Profile.No_Of_Courses_Assigned.writable=False
    
    q2=db(q1).select()
    form=SQLFORM.grid(q1, fields=[ db.Professor_Profile.First_name,  db.Professor_Profile.Last_name,  db.Professor_Profile.Employee_Id,db.Professor_Profile.Gender,db.Professor_Profile.Email_id,db.Professor_Profile.Courses_Previously_Taken,db.Professor_Profile.Mobileno,db.Professor_Profile.Image_Upload], deletable=False, csv=False, create=False, searchable=False)
    return locals()

def Check():
        a=request.vars
        ins=a['gets']
        response.menu +=professormenu
        message=(auth.user.first_name)+' '+(auth.user.last_name)
        q1 = db.Academic_Office.Assigned_Professor == auth.user.id
        ao=[]
        form=db(q1).select()
        for i in form:
            df=i.Course_id
            df=df.lower()
            ao.append(str(df))
        l=len(ao)
        if(l==1):
            if ins:
                   for i in range(0,len(ao)):
                          dg=db.Academic_Office.Course_id==ao[i]
                          db(dg).update(Course_Description=str(ins))
        else:
              if ins:
                    for i in range(0,len(ao)):
                          dg=db.Academic_Office.Course_id==ao[i]
                          db(dg).update(Course_Description=str(ins[i]))
        
        redirect(URL('Professor','index'))
        return dict(form=form,ins=ins)
