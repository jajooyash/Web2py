# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################
@auth.requires_login()
def index():
    type=auth.user.UserType
    if type=='Student':
        response.menu +=studentmenu
        q1 = db.User_Profile.SID == auth.user.id
        StudentRecord = db(q1).select()
        if not StudentRecord:
            redirect(URL('Students','profile1'))
        else:
             response.menu +=studentmenu
             redirect(URL('Students','index'))
    elif type=='Professor':
        response.menu +=professormenu
        q1 = db.Professor_Profile.PID == auth.user.id
        ProfessorRecord = db(q1).select()
        if not ProfessorRecord:
            redirect(URL('Professor','profile1'))
        else:
            redirect(URL('Professor','index'))
    else:
        response.menu +=Adminmenu
        redirect(URL('Academics','index'))
        
    return dict(message=(auth.user.first_name)+' '+(auth.user.last_name))

def institute():
            response.flash = T("Welcome To IIIT")
            if auth.user:
                type=auth.user.UserType
                if type=='Student':
                        response.menu +=studentmenu
                elif type=='Professor':
                        response.menu +=professormenu
                elif type=='Admin':
                        response.menu +=Adminmenu
            return locals()
    
def contact():
            #response.flash = T("Hello World")
            if auth.user:
                type=auth.user.UserType
                if type=='Student':
                        response.menu +=studentmenu
                elif type=='Professor':
                        response.menu +=professormenu
                elif type=='Admin':
                        response.menu +=Adminmenu
            return locals()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
