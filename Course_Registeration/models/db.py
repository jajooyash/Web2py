# -*- coding: utf-8 -*-
db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'],lazy_tables=True)

from gluon.tools import Auth, Service, PluginManager

auth = Auth(db)
service = Service()
plugins = PluginManager()

## configure email
mail = auth.settings.mailer
mail.settings.server ='smtp.gmail.com:587'
mail.settings.sender ='iiith.coursereg@gmail.com'
mail.settings.login = 'iiith.coursereg@gmail.com:dsypbydeyemutnto'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True


auth.settings.extra_fields['auth_user']= [ Field('UserType','string', requires=IS_IN_SET(['Student', 'Professor'] ))] 

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

#db.auth_user.email.editable=False
db.define_table('Professor_Profile',Field('PID', requires=[IS_NOT_EMPTY() ]),
                Field('First_name',requires=IS_NOT_EMPTY()),
                Field('Last_name',requires=IS_NOT_EMPTY()),
                Field('Gender',requires=IS_IN_SET(['Male', 'Female', 'Other'])),
                Field('Employee_Id','integer',requires=(IS_NOT_EMPTY(),IS_NOT_IN_DB(db,'Professor_Profile.Employee_Id'))),
                Field('Department',requires=IS_IN_SET(['CVEST','CVIT','LTR','RRC','CogSci','CL','SPCRC','CN','LTRC','Other'])),
                Field('Email_id'),
                Field('Mobileno','string',requires=[IS_LENGTH(10),IS_NOT_EMPTY()]),
                Field('Courses_Allocated','text'),
                Field('No_Of_Courses_Assigned','integer',default='0'),
                Field('Courses_Previously_Taken','text'),
                Field('Image_Upload', 'upload'),
                auth.signature)

db.Professor_Profile.PID.requires = IS_IN_DB(db,db.auth_user.id)

db.define_table('Academic_Office',
               Field('Course_Name',requires=IS_NOT_EMPTY()),
               Field('Course_id',requires=(IS_SLUG(),IS_LENGTH(6),IS_NOT_EMPTY(),IS_NOT_IN_DB(db,'Academic_Office.Course_id'))),
               Field('Credits','integer',requires=IS_NOT_EMPTY()),
               Field('Assigned_Professor',requires=IS_NOT_EMPTY()),
               Field('Employee_Id','integer',requires=IS_NOT_EMPTY()),
               Field('Course_Description','text'),
               Field('Min_Students','integer',requires=IS_NOT_EMPTY()),
               Field('First_name',requires=IS_NOT_EMPTY()),
               Field('Last_name',requires=IS_NOT_EMPTY()),
               auth.signature)
db.Academic_Office.Assigned_Professor.requires = IS_IN_DB(db,db.Professor_Profile.PID,'%(First_name)s %(Last_name)s(%(PID)s)' )

db.define_table('User_Profile',Field('SID', requires=[IS_NOT_EMPTY() ]),
                Field('First_name',requires=[ IS_NOT_EMPTY() ]),
                Field('Last_name',requires=[ IS_NOT_EMPTY() ]),
                Field('Rollno','integer',requires=(IS_SLUG(),IS_NOT_IN_DB(db,'User_Profile.Rollno'))),
                Field('Dob','date',requires=[ IS_NOT_EMPTY() ]),
                Field('Gender',requires=IS_IN_SET(['Male', 'Female', 'Other'])),
                Field('Email_id'),
                Field('Stream',requires=IS_IN_SET(['VLSI & CE', 'CASE','CSE','ECE','CSIS','CL','Bioinformatics','CN','CE','Other'])),
                Field('Program',requires=IS_IN_SET(['M.Tech','B.Tech', 'PhD','MS','MS-Dual','Other'])),
                Field('Years',requires=IS_IN_SET(['1', '2', '3','4','5','Other'])),
                Field('CGPA','float'),
                Field('Mobileno', 'string',requires=[IS_LENGTH(10),IS_NOT_EMPTY()]),
                Field('Place'),
                Field('Filled','boolean',default='False'),
                Field('Courses_Taken','text'),
                Field('Project_Done','text'),
                Field('Image_Upload', 'upload'),
                Field('No_Of_Courses','integer',default=0),
                Field('No_Of_Project','integer',default=0),
                Field('Course1', 'text',''),
                Field('Course1_Flag','boolean',default='False'),
                Field('Course2', 'text',''),
                Field('Course2_Flag','boolean',default='False'),
                Field('Course3', 'text',''),
                Field('Course3_Flag','boolean',default='False'),
                Field('Course4', 'text',''),
                Field('Course4_Flag','boolean',default='False'),
                Field('Course5', 'text',''),
                Field('Course5_Flag','boolean',default='False'),
                Field('Project1', 'text',''),
                Field('Project1_Title', 'text',''),
                Field('Project2', 'text',''),
                Field('Project2_Title', 'text',''),
                Field('Project3', 'text',''),
                Field('Project3_Title', 'text',''),
                Field('Project4', 'text',''),
                Field('Project4_Title', 'text',''),
                Field('Project5', 'text',''),
                Field('Project5_Title', 'text',''),
                auth.signature)
db.User_Profile.SID.requires = IS_IN_DB(db,db.auth_user.id)
#db.User_Profile.Course1.requires = IS_IN_DB(db,db.Academic_Office.Course_id,'%(First_name)s %(Last_name)s(%(Course_id)s)' )
#db.User_Profile.Course2.requires = IS_IN_DB(db,db.Academic_Office.Course_id,'%(First_name)s %(Last_name)s(%(Course_id)s)' )
#db.User_Profile.Course3.requires = IS_IN_DB(db,db.Academic_Office.Course_id,'%(First_name)s %(Last_name)s(%(Course_id)s)' )
#db.User_Profile.Course4.requires = IS_IN_DB(db,db.Academic_Office.Course_id,'%(First_name)s %(Last_name)s(%(Course_id)s)' )
#db.User_Profile.Course5.requires = IS_IN_DB(db,db.Academic_Office.Course_id,'%(First_name)s %(Last_name)s(%(Course_id)s)' )
